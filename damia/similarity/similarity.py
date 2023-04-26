import pandas as pd
import itertools
import argparse
from typing import List, Tuple

def read_tsv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, sep='\t')

def preprocess_table(df: pd.DataFrame, residues_only: bool, remove_duplicate_residues: bool) -> pd.DataFrame:
    if residues_only:
        if 'res1_num' in df.columns and 'res2_num' in df.columns:
            df = df[['res1_num', 'res2_num']]  # Keep only the residue number columns
            if remove_duplicate_residues:
                df = df.drop_duplicates()  # Remove duplicate residues
        else:
            raise ValueError("The input DataFrame must have 'res1_num' and 'res2_num' columns to process residues_only.")
    else:
        df = df.drop(['index', 'alpha_distance', 'beta_distance'], axis=1)  # Remove unnecessary columns
        df = df.drop_duplicates()  # Remove duplicate rows

    return df

def jaccard_index(df1: pd.DataFrame, df2: pd.DataFrame) -> float:
    intersection = pd.merge(df1, df2, how='inner').shape[0]
    union = pd.concat([df1, df2]).drop_duplicates().shape[0]
    return intersection / union

def multi_table_jaccard(file_paths: List[str], residues_only: bool, remove_duplicate_residues: bool) -> Tuple[pd.DataFrame, pd.Series]:
    # Read and preprocess tables
    tables = [preprocess_table(read_tsv(file_path), residues_only, remove_duplicate_residues) for file_path in file_paths]

    # Calculate pairwise Jaccard Index
    pairwise_results = []
    for t1, t2 in itertools.combinations(enumerate(tables), 2):
        index1, table1 = t1
        index2, table2 = t2
        similarity = jaccard_index(table1, table2)
        pairwise_results.append((f"Table {index1 + 1} - Table {index2 + 1}", similarity))

    # Store results in a DataFrame
    results_df = pd.DataFrame(pairwise_results, columns=['Pairwise Matchup', 'Similarity Score'])

    # Calculate average, median, minimum, and maximum scores
    avg_score = results_df['Similarity Score'].mean()
    median_score = results_df['Similarity Score'].median()
    min_score = results_df['Similarity Score'].min()
    max_score = results_df['Similarity Score'].max()

    summary = pd.Series({
        'Average Score': avg_score,
        'Median Score': median_score,
        'Minimum Score': min_score,
        'Maximum Score': max_score
    })

    return results_df, summary

# Set up argument parsing
parser = argparse.ArgumentParser(description="Calculate Jaccard Index similarity between TSV files.")
parser.add_argument('file_paths', metavar='file_paths', type=str, nargs='+', help='Paths to TSV files')
parser.add_argument('--residues_only', action='store_true', help='Keep only the third column (residues)')
parser.add_argument('--remove_duplicate_residues', action='store_true', help='Remove duplicate residues from the third column')
args = parser.parse_args()

# Use command-line provided file paths and options
file_paths = args.file_paths
residues_only = args.residues_only
remove_duplicate_residues = args.remove_duplicate_residues

results_df, summary = multi_table_jaccard(file_paths, residues_only, remove_duplicate_residues)

# Save results_df as a TSV file
results_df.to_csv("pairwise_similarity.tsv", sep='\t', index=False)

# Save summary as a .txt file
with open("summary.txt", "w") as summary_file:
    summary_file.write(summary.to_string())
