# Mann-Whitney U-test: Interaction Data Significance Analysis Tool

This Python script performs a Mann-Whitney U-test on specified columns from multiple TSV files to determine if the difference between interaction data of two sets of models is significant.

## Dependencies

- Python 3.6+
- pandas
- scipy

## Usage

```bash
python whitney.py -a <sample_a_files> -b <sample_b_files> -c <column_name>
```

### Arguments

- `-a`, `--sample_a`: List of TSV files for sample A (space-separated).
- `-b`, `--sample_b`: List of TSV files for sample B (space-separated).
- `-c`, `--column_name`: Column name to extract data from.

### Example

Suppose we have four TSV files, `sample_a1.tsv`, `sample_a2.tsv`, `sample_b1.tsv`, and `sample_b2.tsv`. We want to perform a Mann-Whitney U-test on the "interaction_strength" column. The command would look like:

```bash
python whitney.py -a sample_a1.tsv sample_a2.tsv -b sample_b1.tsv sample_b2.tsv -c interaction_strength
```

## Output

The script prints the Mann-Whitney U-test results, including the U statistic and P-value, to the console. Additionally, it generates an output text file called "whitney.txt" containing the same information.

## Functions

### read_and_extract_column(filepaths: List[str], column_name: str) -> List[float]

Reads the specified column from each TSV file in the list of file paths, ignoring rows with "N/A" in the specified column, and returns the combined data as a list of floats.

### main(sample_a_files: List[str], sample_b_files: List[str], column_name: str)

Performs a Mann-Whitney U-test on the specified columns from the given TSV files for samples A and B, prints the results, and writes the results to an output file.

## Input TSV File Format

The input TSV files should have the following format:

```
pdb_id  interaction_strength
model1  0.65
model2  0.72
model3  0.61
```

## Example Output TXT File

The output text file `whitney.txt` will have the following content:

```
Mann-Whitney U-test results:
U statistic: 15.0
P-value: 0.0389249472108
```