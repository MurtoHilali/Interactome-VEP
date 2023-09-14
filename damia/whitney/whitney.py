import argparse
import pandas as pd
from scipy.stats import mannwhitneyu

def read_and_extract_column(filepaths, column_name):
    data = []
    for filepath in filepaths:
        df = pd.read_csv(filepath, sep='\t')
        extracted_column = df[column_name].dropna()
        data.extend(extracted_column[~(extracted_column == 'N/A')])
    return data

def main(sample_a_files, sample_b_files, column_name):
    sample_a = read_and_extract_column(sample_a_files, column_name)
    sample_b = read_and_extract_column(sample_b_files, column_name)

    sample_a = pd.Series(sample_a).apply(pd.to_numeric, errors='coerce').dropna().tolist()
    sample_b = pd.Series(sample_b).apply(pd.to_numeric, errors='coerce').dropna().tolist()

    u_statistic, p_value = mannwhitneyu(sample_a, sample_b, alternative='two-sided')
    
    output = f"Mann-Whitney U-test results:\nU statistic: {u_statistic}\nP-value: {p_value}"
    print(output)

    with open("whitney.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform Mann-Whitney U-test on specified columns from multiple TSV files.')
    parser.add_argument('-a', '--sample_a', nargs='+', help='List of TSV files for sample A.', required=True)
    parser.add_argument('-b', '--sample_b', nargs='+', help='List of TSV files for sample B.', required=True)
    parser.add_argument('-c', '--column_name', help='Column name to extract data from.', required=True)
    
    args = parser.parse_args()
    
    main(args.sample_a, args.sample_b, args.column_name)
