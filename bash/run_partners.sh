#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 <directory> <residue_id> <chain_id>"
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

# Call partners.py with the found file paths and command-line arguments
python damia/partners/partners.py "$file_paths" "$2" "$3"
