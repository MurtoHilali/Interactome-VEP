# Distance: A Residue Distance Calculator

This script calculates the distances between the alpha- and beta-carbons of residue pairs in a PDB file, using PyMOL. The input is an `.ic` file containing the list of residue pairs, and the output is a TSV file containing the calculated distances.

## Usage

To run the script from the command line, use the following format:

```bash
python distance.py <ic_file> <pdb_file> [-o <output_tsv>]
```

Where:

- `<ic_file>`: Path to the `.ic` file containing the residue pairs.
- `<pdb_file>`: Path to the PDB file containing the protein structure.
- `<output_tsv>`: (Optional) Path to the output TSV file where the distances will be saved. Defaults to `output.tsv` in the current directory.

### Example:

```bash
python distance.py input.ic protein.pdb -o distances.tsv
```

## Input

The input `.ic` file should contain a list of residue pairs, one pair per line. Each line should contain the following columns, separated by whitespace:

1. Residue type of the first residue (e.g., "GLY").
2. Residue number of the first residue (e.g., "42").
3. Chain identifier of the first residue (e.g., "A").
4. Residue type of the second residue (e.g., "LEU").
5. Residue number of the second residue (e.g., "87").
6. Chain identifier of the second residue (e.g., "B").

For example:

```
GLY 42 A LEU 87 B
```

## Output

The output TSV file will contain the following columns:

1. Index: The index of the residue pairn from the `.ic` file.
2. Chain1: Chain identifier of the first residue.
3. Res1: Residue type of the first residue.
4. Res1_num: Residue number of the first residue.
5. Chain2: Chain identifier of the second residue.
6. Res2: Residue type of the second residue.
7. Res2_num: Residue number of the second residue.
8. Alpha_distance: Distance between the alpha-carbons of the two residues.
9. Beta_distance: Distance between the beta-carbons of the two residues, or "N/A" if one of the residues is glycine.

Example output:

```
index   chain1  res1    res1_num chain2  res2    res2_num alpha_distance    beta_distance
1       A       GLY     42       B       LEU     87       12.34             N/A
```

## Code Overview

The script is divided into the following functions:

- `calculate_distance`: Calculates the distance between the alpha- and beta-carbons of two residues in a PDB file.
- `main`: Reads the input `.ic` file, calculates distances for all residue pairs, and writes the results to the output TSV file.

The script uses the `argparse` library to parse command-line arguments, and the `pymol` library to load PDB files and calculate distances.

For more information on the `pymol` library, visit the [PyMOL Wiki](https://pymolwiki.org/index.php/Main_Page).