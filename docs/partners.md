# Chain-Residue Pair Analysis Tool

This Python script analyzes occurrences of a chain-residue pair across multiple TSV files and calculates a consensus score based on their presence. The script also calculates the average distance (either alpha or beta) between the chain-residue pairs in the provided TSV files.

## Dependencies

- Python 3.6+
- pandas

## Usage

```bash
python chain_residue_pair_analysis.py <file_paths> <chain> <residue> [-d <distance_type>]
```

### Arguments

- `file_paths`: Paths to the TSV files (space-separated).
- `chain`: Chain (a letter A-Z).
- `residue`: Residue (an integer).
- `-d`, `--distance_type`: (Optional) Distance type, either "alpha" or "beta". Default is "beta".

### Example

Suppose we have two TSV files `file1.tsv` and `file2.tsv`. We want to analyze the occurrences of the chain-residue pair A-42 with alpha distance. The command would look like:

```bash
python chain_residue_pair_analysis.py file1.tsv file2.tsv A 42 -d alpha
```

## Output

The script prints the consensus score and total occurrences of the chain-residue pair to the console. Additionally, it generates two output files:

1. `occurrences.tsv`: A TSV file containing the occurrences and average distances for each input TSV file.
2. `avg_distance.txt`: A plain text file containing the overall average distance.

## Functions

### read_tsv(file_path: str) -> pd.DataFrame

Reads a TSV file and returns a pandas DataFrame.

### find_chain_residue(df: pd.DataFrame, chain: str, residue: int, distance_type: str) -> (bool, int, float)

Finds the occurrences of a chain-residue pair in the given DataFrame and calculates the average distance based on the specified distance type. Returns a tuple containing a boolean indicating presence, the number of occurrences, and the average distance.

## Example Input TSV File

The input TSV files should have the following format:

```
index   chain1  res1    res1_num chain2  res2    res2_num alpha_distance  beta_distance
1       A       ALA     15       B       GLY     32       12.34           10.56
2       A       VAL     42       B       MET     29       7.92            6.34
3       B       ALA     15       A       GLY     32       11.87           9.42
```

## Example Output TSV File

The output TSV file `occurrences.tsv` will have the following format:

```
TSV     Occurrences  Average Distance
file1.tsv       2           6.45
file2.tsv       1           7.92
```

## Example Output TXT File

The output plain text file `avg_distance.txt` will have the following content:

```
Average Distance: 6.94
```