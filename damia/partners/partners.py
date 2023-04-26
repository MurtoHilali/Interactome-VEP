import csv
import argparse
from collections import defaultdict
import matplotlib.pyplot as plt

def analyze_residue_interactions(input_files, target_chain, target_residue, output_file):
    residue_counts = defaultdict(int)

    for input_file in input_files:
        with open(input_file, 'r') as infile:
            tsv_reader = csv.reader(infile, delimiter='\t')
            next(tsv_reader)  # Skip header

            for row in tsv_reader:
                chain_a, residue_num_a, chain_b, residue_num_b = row[1], row[2], row[4], row[5]

                if (chain_a == target_chain and residue_num_a == target_residue) or (chain_b == target_chain and residue_num_b == target_residue):
                    interacting_residue = row[3] if chain_a == target_chain else row[0]
                    residue_counts[interacting_residue] += 1

    # Write the output data to the TSV file
    with open(output_file, 'w', newline='') as outfile:
        tsv_writer = csv.writer(outfile, delimiter='\t')
        tsv_writer.writerow(['Residue', 'Count'])

        for residue, count in residue_counts.items():
            tsv_writer.writerow([residue, count])

    return residue_counts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze residue interactions from multiple TSV files.')
    parser.add_argument('input_files', nargs='+', help='Paths to the input TSV files.')
    parser.add_argument('target_chain', choices=['A', 'B'], help='Target chain (A or B).')
    parser.add_argument('target_residue', help='Target residue number.')

    args = parser.parse_args()

    output_file = "{}-{}-partners.tsv".format(args.target_chain, args.target_residue)
    counts = analyze_residue_interactions(args.input_files, args.target_chain, args.target_residue, output_file)

    # Print the results
    print("Residue interaction counts for chain {} and residue {}:".format(args.target_chain, args.target_residue))
    for residue, count in counts.items():
        print("{}: {}".format(residue, count))
