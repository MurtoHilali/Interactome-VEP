import argparse
import csv
import numpy as np

def process_csv_file(filename, output_filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        numeric_columns = [i for i, h in enumerate(headers) if h not in ('pdb', 'interface')]
        data = [[] for _ in headers]
        for row in reader:
            for i, col in enumerate(row):
                if i in numeric_columns and row[col] != 'NA':
                    data[i].append(float(row[col]))

    with open(output_filename, 'w', newline='') as fout:
        tsv_writer = csv.writer(fout, delimiter='\t')
        tsv_writer.writerow(headers + ['Average', 'Std. Deviation', 'Std. Error'])
        for i, h in enumerate(headers):
            if i in numeric_columns:
                col_data = np.array(data[i])
                avg = np.mean(col_data)
                std = np.std(col_data)
                std_error = std / np.sqrt(len(col_data))
                tsv_writer.writerow([h, avg, std, std_error])

def main():
    parser = argparse.ArgumentParser(description="Find averages, standard deviations, and standard errors for PI-Score features.")
    parser.add_argument('csv_path', metavar='csv_path', type=str, help='Path to the CSV file')
    parser.add_argument('-o', '--output', metavar='output_file', default='averages.tsv', type=str, help='Output file name (default: averages.tsv)')
    args = parser.parse_args()
    csv_path = args.csv_path
    output_file = args.output

    process_csv_file(csv_path, output_file)

if __name__ == "__main__":
    main()
