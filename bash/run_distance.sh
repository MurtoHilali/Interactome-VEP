#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: directory '$1' not found"
    exit 1
fi

cd "$1" || { echo "Error: could not change directory to '$1'"; exit 1; }

for ranked_dir in ranked_*; do
    if [ ! -d "$ranked_dir" ]; then
        echo "Error: '$ranked_dir' is not a directory"
        continue
    fi
    # Go inside each ranked_* directory
    cd "${ranked_dir}" || { echo "Error: could not change directory to '$ranked_dir'"; continue; }
    echo "Now in ${ranked_dir}"
    # Run the command using the ranked_* basename
    python damia/distance/distance.py "${ranked_dir}".ic "${ranked_dir}".pdb -o "${ranked_dir}".tsv

    # Go back to the analysis directory
    cd ..
done
