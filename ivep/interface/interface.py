import pandas as pd
import argparse

def read_tsv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, sep='\t')

def find_chain_residue(df: pd.DataFrame, chain: str, residue: int, distance_type: str) -> (bool, int, float):
    chain_residue_pair1 = (df['chain1'] == chain) & (df['res1_num'] == residue)
    chain_residue_pair2 = (df['chain2'] == chain) & (df['res2_num'] == residue)

    filtered_df = df[chain_residue_pair1 | chain_residue_pair2]
    count = filtered_df.shape[0]

    column = 'alpha_distance' if distance_type == 'alpha' else 'beta_distance'
    avg_distance = filtered_df[column].mean() if count > 0 else 0
    
    return (chain_residue_pair1 | chain_residue_pair2).any(), count, avg_distance

parser = argparse.ArgumentParser(description="Find occurrences of a chain-residue pair in multiple TSV files and calculate a consensus score.")
parser.add_argument('file_paths', metavar='file_paths', type=str, nargs='+', help='Paths to the TSV files')
parser.add_argument('chain', metavar='chain', type=str, help='Chain (A letter A-Z)')
parser.add_argument('residue', metavar='residue', type=int, help='Residue (An integer)')
parser.add_argument('-d', '--distance_type', type=str, choices=['alpha', 'beta'], default='beta', help='Distance type (alpha or beta)')
args = parser.parse_args()

file_paths = args.file_paths
chain = args.chain
residue = args.residue
distance_type = args.distance_type

results = [find_chain_residue(read_tsv(file_path), chain, residue, distance_type) for file_path in file_paths]

presence = [result[0] for result in results]
occurrences = [result[1] for result in results]
avg_distances = [result[2] for result in results]
consensus_score = sum(presence) / len(file_paths)

print(f"The consensus score for the chain-residue pair {chain}-{residue} is {consensus_score:.2f}.\nTotal occurrences: {sum(occurrences)}")

occurrences_df = pd.DataFrame({'TSV': file_paths, 'Occurrences': occurrences, 'Average Distance': avg_distances})
occurrences_df.to_csv('occurrences.tsv', sep='\t', index=False)

# Save the average distance to 'avg_distance.txt' file
with open('avg_distance.txt', 'w') as avg_distance_file:
    avg_distance_file.write("Average Distance: {:.2f}\n".format(sum(avg_distances) / len(avg_distances)))
