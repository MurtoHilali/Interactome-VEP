#!/bin/bash

if [[ "$#" -ne 1 ]]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

if [[ ! -d "$1" ]]; then
  echo "Error: '$1' is not a directory"
  exit 1
fi

# Find all TSV files in the current directory and its subdirectories
file_paths=$(find "$1" -type f -name "ranked_[0-9].tsv")

if [[ -z "$file_paths" ]]; then
  echo "Error: No TSV files found in directory '$1' and its subdirectories"
  exit 1
fi

# Call similarity.py with the found file paths
python damia/distance/avgdistance.py "$file_paths"
