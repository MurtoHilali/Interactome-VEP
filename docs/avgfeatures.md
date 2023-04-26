# Average Features Calculator: PI-Score Features Analysis Tool

This Python script reads a CSV file containing PI-Score features and calculates the averages, standard deviations, and standard errors for each numeric feature. The results are saved in a TSV file.

## Dependencies

- Python 3.6+
- pandas
- numpy

## Usage

```bash
python avgfeatures.py <csv_path> [-o output_file]
```

### Arguments

- `csv_path`: Path to the input CSV file.
- `output_file`: (Optional) Output file name. Default is "averages.tsv".

### Example

Suppose we have a CSV file `input.csv`. We want to calculate the averages, standard deviations, and standard errors for the numeric features and save the results in a file called "results.tsv". The command would look like:

```bash
python avgfeatures.py input.csv -o results.tsv
```

## Output

The script generates an output TSV file containing the averages, standard deviations, and standard errors for each numeric feature in the input CSV file.

## Functions

### process_csv_file(filename: str, output_filename: str)

Reads a CSV file, calculates the averages, standard deviations, and standard errors for each numeric feature, and saves the results in a TSV file.

## Example Input CSV File

The input CSV files should have the following format:

```
pdb,interface,Num_intf_residues,Polar,Hydrophobhic,Charged,conserved_interface, contact_pairs, sc, hb, sb, int_solv_en, int_area, pvalue
ranked_0,B_A,54,0.278,0.259,0.37,NA,55,0.629,21,6,-8.41,1770.08,0.63
```

## Example Output TSV File

The output TSV file will have the following format:

```
Feature	        Average    Std. Deviation	Std. Error
Num_intf_residues 54.000000	0.000000	    0.000000
Polar	          0.278000	0.000000	    0.000000
Hydrophobhic      0.259000	0.000000	    0.000000
Charged           0.370000	0.000000	    0.000000
```

Note that the example output file contains only a single row of data, as there is only one input row in the example input file. In practice, the input CSV file will have multiple rows, and the output file will show the calculated values based on all input rows.