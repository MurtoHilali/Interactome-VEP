import argparse
import os
import re
from itertools import product
from pymol import cmd

def calculate_distance(pdb_file, chain1, res_num1, res_type1, chain2, res_num2, res_type2):
    """Calculates the distance between the alpha- and beta-carbons of two residues in a PDB file"""
    cmd.load(pdb_file, "protein")
    atom1_alpha = f'/protein//{chain1}/{res_num1}/CA'
    atom1_beta = f'/protein//{chain1}/{res_num1}/CB' if res_type1 != 'GLY' else None
    atom2_alpha = f'/protein//{chain2}/{res_num2}/CA'
    atom2_beta = f'/protein//{chain2}/{res_num2}/CB' if res_type2 != 'GLY' else None
    
    alpha_distance = cmd.get_distance(atom1_alpha, atom2_alpha)
    beta_distance = cmd.get_distance(atom1_beta, atom2_beta) if atom1_beta and atom2_beta else None
    
    cmd.delete('all')
    return alpha_distance, beta_distance

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Calculate distances between residues in an .ic file using PyMol')
    parser.add_argument('ic_file', type=str, help='path to the .ic file')
    parser.add_argument('pdb_file', type=str, help='path to the PDB file')
    parser.add_argument('-o', '--output', type=str, help='path to the output TSV file', default='output.tsv')
    args = parser.parse_args()
    
    # Read the .ic file and extract residue pairs
    with open(args.ic_file, 'r') as f:
        residue_pairs = [re.split('\s+', line.strip()) for line in f]
    
    # Calculate distances for each residue pair and store results in a list of tuples
    results = []
    for i, pair in enumerate(residue_pairs, start=1):
        res_type1, res_num1, chain1, res_type2, res_num2, chain2 = pair
        alpha_distance, beta_distance = calculate_distance(args.pdb_file, chain1, res_num1, res_type1, chain2, res_num2, res_type2)
        results.append((i, chain1, res_type1, res_num1, chain2, res_type2, res_num2, alpha_distance, beta_distance))
    
    # Sort the results by the value in column 3 (res_num1)
    sorted_results = sorted(results, key=lambda x: int(x[3]))
    
    # Open the output TSV file for writing
    with open(args.output, 'w') as f:
        # Write header row
        f.write('index\tchain1\tres1\tres1_num\tchain2\tres2\tres2_num\talpha_distance\tbeta_distance\n')
        
        # Loop over sorted results and write them to the output file
        for result in sorted_results:
            f.write(f'{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}\t{result[5]}\t{result[6]}\t{result[7]:.2f}\t')
            if result[8] is not None:
                f.write(f'{result[8]:.2f}\n')
            else:
                f.write('N/A\n')
    
    print(f'Distances written to {os.path.abspath(args.output)}')

if __name__ == '__main__':
    main()

