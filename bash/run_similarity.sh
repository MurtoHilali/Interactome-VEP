#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: directory '$1' not found"
    exit 1
fi

# Find all TSV files in the current directory and its subdirectories
file_paths=$(find "$1" -type f -name "ranked_[0-9].tsv")

if [ -z "$file_paths" ]; then
    echo "Error: no TSV files found in directory '$1' and its subdirectories"
    exit 1
fi

# Call similarity.py with the found file paths
python damia/similarity/similarity.py --residues_only --remove_duplicate_residues "$file_paths"
