# Similarity: Determine Overlap Between Complex Interactions

This script calculates the Jaccard Index similarity between multiple TSV files. Users can provide options to keep only the residue numbers, remove duplicate residues, or both. The script saves the pairwise similarity scores in a TSV file and writes a summary of the results to a text file.

## Command-Line Arguments

* `file_paths` (str): Paths to the TSV files to be compared.
* `--residues_only` (bool, optional): If provided, keep only the residue number columns in the input DataFrames.
* `--remove_duplicate_residues` (bool, optional): If provided, remove duplicate residues from the input DataFrames.

## Example Usage

Here is an example of how to run the script from the command line:

```bash
python multi_table_jaccard.py file1.tsv file2.tsv file3.tsv --residues_only --remove_duplicate_residues
```

In this example, the script will:

1. Read the contents of `file1.tsv`, `file2.tsv`, and `file3.tsv`.
2. Preprocess each DataFrame by keeping only the residue number columns (`res1_num` and `res2_num`) and removing duplicate residues if the `--residues_only` and `--remove_duplicate_residues` flags are provided.
3. Calculate the pairwise Jaccard Index similarity between each pair of tables.
4. Save the pairwise similarity scores in a TSV file named `pairwise_similarity.tsv`.
5. Calculate the average, median, minimum, and maximum similarity scores and save the summary in a text file named `summary.txt`.

The output files `pairwise_similarity.tsv` and `summary.txt` will be generated in the same directory as the script.

## Functions

1. `read_tsv(file_path: str) -> pd.DataFrame`:

   Reads a TSV file and returns a pandas DataFrame.
   
   * `file_path` (str): The file path of the TSV file.

2. `preprocess_table(df: pd.DataFrame, residues_only: bool, remove_duplicate_residues: bool) -> pd.DataFrame`:

   Preprocesses a DataFrame by keeping only the residue number columns or removing unnecessary columns and duplicate rows.
   
   * `df` (pd.DataFrame): The input DataFrame.
   * `residues_only` (bool): If True, keep only the residue number columns.
   * `remove_duplicate_residues` (bool): If True, remove duplicate residues.

3. `jaccard_index(df1: pd.DataFrame, df2: pd.DataFrame) -> float`:

   Calculates the Jaccard Index similarity between two DataFrames.
   
   * `df1` (pd.DataFrame): The first DataFrame.
   * `df2` (pd.DataFrame): The second DataFrame.

4. `multi_table_jaccard(file_paths: List[str], residues_only: bool, remove_duplicate_residues: bool) -> Tuple[pd.DataFrame, pd.Series]`:

   Calculates pairwise Jaccard Index similarity between multiple TSV files and returns a DataFrame with the results and a summary Series.
   
   * `file_paths` (List[str]): A list of file paths to the TSV files.
   * `residues_only` (bool): If True, keep only the residue number columns in the input DataFrames.
   * `remove_duplicate_residues` (bool): If True, remove duplicate residues from the input DataFrames.

## Output Files

1. `pairwise_similarity.tsv`: A TSV file containing the pairwise similarity scores.
2. `summary.txt`: A text file containing the average, median, minimum, and maximum similarity scores.

Example Input:

Let's consider three example TSV files, `file1.tsv`, `file2.tsv`, and `file3.tsv`.

`file1.tsv`:

```
index   chain1  res1    res1_num chain2  res2    res2_num alpha_distance  beta_distance
1       A       ALA     15       B       GLY     32       12.34           10.56
2       A       VAL     42       B       MET     29       7.92            6.34
3       B       ALA     15       A       GLY     32       11.87           9.42
```

`file2.tsv`:

```
index   chain1  res1    res1_num chain2  res2    res2_num alpha_distance  beta_distance
1       A       ALA     15       B       GLY     32       13.45           11.32
2       B       VAL     42       A       MET     29       8.01            6.47
4       A       ARG     8        B       LEU     21       10.29           8.61
```

`file3.tsv`:

```
index   chain1  res1    res1_num chain2  res2    res2_num alpha_distance  beta_distance
1       A       ALA     15       B       GLY     32       12.78           10.89
2       A       VAL     42       B       MET     29       7.95            6.38
3       B       ALA     15       A       GLY     32       11.89           9.44
5       A       ARG     8        B       LEU     21       10.31           8.63
```

Command:

```bash
python multi_table_jaccard.py file1.tsv file2.tsv file3.tsv --residues_only --remove_duplicate_residues
```

Example Output:

`pairwise_similarity.tsv`:

```
Pairwise Matchup      Similarity Score
Table 1 - Table 2     0.6
Table 1 - Table 3     0.75
Table 2 - Table 3     0.6
```

`summary.txt`:

```
Average Score: 0.65
Median Score: 0.6
Minimum Score: 0.6
Maximum Score: 0.75
```

In this example, the pairwise similarity scores between the tables are 0.6 and 0.75, indicating that the residue pairs in the tables are not identical after preprocessing.