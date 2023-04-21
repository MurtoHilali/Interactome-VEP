# Interactome-VEP (iVEP)

Interactome-VEP is a collection of tools for predicting the impact of missense mutations on direct Protein-Protein Interactions (PPIs). It is designed to work with PDB entries or AlphaFold output. The current version of Interactome-VEP includes four main functionalities: distance calculation, interface determination, interaction partners, and Jaccard index similarity.

## Features

- **Distance Calculation**: Computes the distances between alpha and beta carbons in protein structures.
- **Interface Determination**: Identifies whether a given chain-residue pair appears in interfaces based on interaction data (TSVs) and determines the frequency of their occurrence.
- **Interaction Partners**: Provides information on interaction partners for a chain-residue pair.
- **Jaccard Index Similarity**: Calculates Jaccard index similarity between interaction data TSV files.

## Input Formats

The tools in Interactome-VEP primarily accept TSV files with specific headers. As a user, you will typically only need to input a PDB file. Most of the data processed by this project is self-generated.

## Installation

### Dependencies

To use Interactome-VEP, you will need to install the following dependencies:

1. [PI score](https://gitlab.com/topf-lab/pi_score)
2. [Prodigy](https://gitlab.com/topf-lab/pi_score)
3. [PyMOL](https://pymol.org/)

Please follow the installation steps provided in the respective links above.

### Interactome-VEP

To install Interactome-VEP, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/interactome-vep.git
cd interactome-vep
```

## Usage Examples

For specific usage examples and explanations of each tool, please refer to the documentation in the `/docs` directory, or an overview at the [Documentation Index](docs/index.md):

- [distance.md](docs/distance.md): Distance calculation between alpha and beta carbons
- [interface.md](docs/interface.md): Interface determination for chain-residue pairs
- [partners.md](docs/partners.md): Interaction partners of chain-residue pairs
- [similarity.md](docs/similarity.md): Jaccard index similarity calculation

## Contributing

We welcome contributions to the project! If you have any suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).