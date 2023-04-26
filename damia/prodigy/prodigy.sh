#!/bin/bash

for file in *.pdb
do
  if [ -f "$file" ]; then
    mkdir "${file%.pdb}"
    output="${file%.pdb}.out"
    prodigy --contact_list --pymol_selection "$file" > "$output"
    mv "${file%.pdb}"* "${file%.pdb}"
  fi
done