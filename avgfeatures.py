import argparse
import csv
import numpy as np

def process_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        numeric_columns = [i for i, h in enumerate(headers) if h not in ('pdb', 'interface')]
        data = [[] for _ in headers]
        for row in reader:
            for i, col in enumerate(row):
                if i in numeric_columns and row[col] != 'NA':
                    data[i].append(float(row[col]))
        with open('averages.txt', 'w') as fout:
            for i, h in enumerate(headers):
                if i in numeric_columns:
                    col_data = np.array(data[i])
                    avg = np.mean(col_data)
                    std = np.std(col_data)
                    fout.write(f'{h}: {avg:.3f} {std:.3f}\n')

parser = argparse.ArgumentParser(description="Find averages and standard deviations for PI-Score features.")
parser.add_argument('csv_path', metavar='csv_path', type=str, help='Path to the CSV file')
args = parser.parse_args()
csv_path = args.csv_path

process_csv_file(csv_path)