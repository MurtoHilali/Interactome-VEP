#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: file '$1' not found"
    exit 1
fi

python damia/piscore/avgfeatures.py "$1"
