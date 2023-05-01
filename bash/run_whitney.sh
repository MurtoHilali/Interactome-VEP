#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 <directory_a> <directory_b> <column_name>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: directory '$1' not found"
    exit 1
fi

if [ ! -d "$2" ]; then
    echo "Error: directory '$2' not found"
    exit 1
fi

# Find all TSV files in the specified directories
file_paths_a=$(find "$1" -type f -name "ranked_[0-9].tsv")
file_paths_b=$(find "$2" -type f -name "ranked_[0-9].tsv")

if [ -z "$file_paths_a" ]; then
    echo "Error: no TSV files found in directory '$1' and its subdirectories"
    exit 1
fi

if [ -z "$file_paths_b" ]; then
    echo "Error: no TSV files found in directory '$2' and its subdirectories"
    exit 1
fi

# Call whitney.py with the found file paths, output directory, and column name
python damia/whitney/whitney.py -a "$file_paths_a" -b "$file_paths_b" -c "$3"
