import argparse
from damia.distance import distance, avgdistance
from damia.interface import interface
from damia.partners import partners
from damia.similarity import similarity
from damia.whitney import whitney
from damia.piscore import avgfeatures

def main():
    parser = argparse.ArgumentParser(description="Protein Interaction Analysis Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Distance subcommand
    distance_parser = subparsers.add_parser("distance", help="Calculate average distance and occurrences of a chain-residue pair in multiple TSV files.")
    distance.add_arguments(distance_parser)
    distance_parser.set_defaults(func=distance.main)

    # Average Distance subcommand
    avgdistance_parser = subparsers.add_parser("avgdistance", help="Calculate average distance between carbon-alphas and -betas across all TSV files.")
    distance.add_arguments(avgdistance_parser)
    avgdistance_parser.set_defaults(func=avgdistance.main)

    # PI-Score subcommands
    piscore_parser = subparsers.add_parser("avgfeatures", help="Calculate average, standard deviation, and standard error of all available PI-score metrics.")
    avgfeatures.add_argument(piscore_parser)
    piscore_parser.set_defaults(func=avgfeatures.main)

    # Interface subcommand
    interface_parser = subparsers.add_parser("interface", help="Filter and extract interface data from TSV files.")
    interface.add_arguments(interface_parser)
    interface_parser.set_defaults(func=interface.main)

    # Partners subcommand
    partners_parser = subparsers.add_parser("partners", help="Calculate the percentage of interaction partners shared between two chains in multiple TSV files.")
    partners.add_arguments(partners_parser)
    partners_parser.set_defaults(func=partners.main)

    # Similarity subcommand
    similarity_parser = subparsers.add_parser("similarity", help="Compute Jaccard Index similarity between TSV files using either all columns or just the residue numbers.")
    similarity.add_arguments(similarity_parser)
    similarity_parser.set_defaults(func=similarity.main)

    # Mann-Whitney subcommand
    whitney_parser = subparsers.add_parser("distance", help="Determine statistical signifance of difference between WT and missense interactions (using distances) via MW-U test.")
    whitney.add_arguments(distance_parser)
    whitney_parser.set_defaults(func=whitney.main)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
    else:
        args.func(args)

if __name__ == "__main__":
    main()
