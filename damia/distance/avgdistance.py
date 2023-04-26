import argparse
import pandas as pd
import numpy as np
import os

def calculate_stats(distances):
    mean = np.mean(distances)
    std_dev = np.std(distances)
    std_err = std_dev / np.sqrt(len(distances))
    return mean, std_dev, std_err

def main():
    parser = argparse.ArgumentParser(description="Calculate average distances from TSV files")
    parser.add_argument("tsvs", metavar="TSV", nargs="+", help="One or more TSV files")
    parser.add_argument("-f", "--flag", choices=["alpha", "beta", "both"], default="both", help="Flag: alpha, beta, or both (default)")
    parser.add_argument("-o", "--output", default="distances.txt", help="Output file name (default: distances.txt)")
    args = parser.parse_args()

    alpha_distances = []
    beta_distances = []

    for tsv_file in args.tsvs:
        if not os.path.isfile(tsv_file):
            print(f"File {tsv_file} not found. Skipping.")
            continue
        df = pd.read_csv(tsv_file, sep="\t")
        df.replace("N/A", np.nan, inplace=True)  # Replace "N/A" with NaN
        
        if args.flag in ["alpha", "both"]:
            alpha_valid = df["alpha_distance"].notna()
            alpha_distances.extend(df.loc[alpha_valid, "alpha_distance"].tolist())
        if args.flag in ["beta", "both"]:
            beta_valid = df["beta_distance"].notna()
            beta_distances.extend(df.loc[beta_valid, "beta_distance"].tolist())

    alpha_distances = np.array(alpha_distances, dtype=float)
    beta_distances = np.array(beta_distances, dtype=float)

    with open(args.output, "w") as output_file:
        if args.flag in ["beta", "both"]:
            mean, std_dev, std_err = calculate_stats(beta_distances)
            output_file.write(f"Beta Carbon Distance: {mean:.2f}, {std_dev:.2f}, {std_err:.2f}\n")
        if args.flag in ["alpha", "both"]:
            mean, std_dev, std_err = calculate_stats(alpha_distances)
            output_file.write(f"Alpha Carbon Distance: {mean:.2f}, {std_dev:.2f}, {std_err:.2f}\n")

if __name__ == "__main__":
    main()
