import requests
import pandas as pd
from io import StringIO
from typing import List, Union
from Bio import SeqIO
import os
import argparse
import json

def get_mint_data(output_folder, uniprot_ids):
    base_url = "http://www.ebi.ac.uk/Tools/webservices/psicquic/mint/webservices/current/search/query"
    mitab_columns = [
        "ID A", 
        "ID B",
        "Identifiers A",
        "Identifiers B", 
        "Alias A", 
        "Alias B",
        "Interaction Detection Method",
        "Publication 1st Author",
        "Publication Identifier",  
        "Tax ID A", 
        "Tax ID B",
        "Interaction Type", 
        "Source Database", 
        "Interaction Identifier",
        "Intact MI-Score"
    ]
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for uniprot_id in uniprot_ids:
        # Adding filters for Homo sapiens and 'Direct interaction' type
        query = f"{uniprot_id}?species=human&taxidA=9606&taxidB=9606type=direct interaction"
        query = query.replace(" ", "%20")
        request_url = f"{base_url}/{query}"
        print(request_url)
        response = requests.get(request_url)
        raw_data = response.text

        # Save data to a TSV file named after the UniProt ID
        with open(f"{output_folder}/{uniprot_id}.tsv", "w") as output_file:
            headers_line = '\t'.join(mitab_columns) + '\n'
            output_file.write(headers_line)
            output_file.write(raw_data)

def get_biogrid_data(output_folder, uniprot_ids, access_key):
    base_url = "https://webservice.thebiogrid.org/interactions/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for uniprot_id in uniprot_ids:
        params = {
            "additionalIdentifierTypes": "UNIPROT",
            "interSpeciesExcluded": "true",
            "geneList": uniprot_id,
            "includeInteractors": "true",
            "format": "tab2",
            "taxId": 9606,
            "includeEvidence": "true",
            "includeHeader": "true",
            "throughputTag": "high",
            "accessKey": access_key
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            with open(f"{output_folder}/{uniprot_id}.tsv", "w") as f:
                f.write(response.text)
        else:
            print(f"Error fetching data for {uniprot_id}: {response.status_code}")

def extract_interaction_partners_mint(uniprot_ids, output_folder):
    interaction_partners = {}

    for uniprot_id in uniprot_ids:
        mint_file = os.path.join(output_folder, f"{uniprot_id}.tsv")

        if os.path.exists(mint_file):
            mint_df = pd.read_csv(mint_file, sep="\t")
        else:
            mint_df = pd.DataFrame()

        # Extract interaction partner UniProt IDs from both A and B columns
        interaction_partners_a = mint_df.loc[mint_df['ID A'].str.startswith('uniprotkb:'), 'ID A'].str.replace('uniprotkb:', '')
        interaction_partners_b = mint_df.loc[mint_df['ID B'].str.startswith('uniprotkb:'), 'ID B'].str.replace('uniprotkb:', '')

        # Combine and remove duplicates
        all_interaction_partners = pd.concat([interaction_partners_a, interaction_partners_b], axis=0).drop_duplicates().tolist()

        # Remove the submitted UniProt ID from the list if present
        all_interaction_partners = [partner for partner in all_interaction_partners if partner != uniprot_id]

        # Add interaction partners to the dictionary
        interaction_partners[uniprot_id] = all_interaction_partners

    # Save the results as a JSON file
    with open(f"{output_folder}/interaction_partners.json", "w") as f:
        json.dump(interaction_partners, f, indent=4)

    return interaction_partners

# def extract_interaction_partners_biogrid(uniprot_ids, output_folder):
    # Placeholder for extracting interaction partners from BioGRID data

def create_mfa(interaction_partners: dict) -> Union[str, None]:
    base_url = "https://www.uniprot.org/uniprot/"
    
    if not os.path.exists("complexes"):
        os.makedirs("complexes")

    for key, values in interaction_partners.items():
        for idx, value in enumerate(values):
            uniprot_ids = [key, value]
            sequences = []

            for uniprot_id in uniprot_ids:
                url = base_url + uniprot_id + ".fasta"
                response = requests.get(url)

                if response.status_code == 200:
                    fasta_data = response.text
                    seq_record = SeqIO.read(StringIO(fasta_data), "fasta")
                    sequences.append(seq_record)
                else:
                    print(f"Error: Unable to retrieve sequence for {uniprot_id}")
                    return None

            mfa_data = StringIO()
            SeqIO.write(sequences, mfa_data, "fasta")
            mfa_data.seek(0)
            mfa_string = mfa_data.read()

            with open(f"complexes/{key}:{value}.fa", "w") as f:
                f.write(mfa_string)


def main():
    parser = argparse.ArgumentParser(description='Fetch interaction data from MINT or BioGRID.')
    parser.add_argument('uniprot_ids', nargs='+', help='List of UniProt IDs to fetch data for.')
    parser.add_argument('--source', choices=['mint', 'biogrid'], required=True, help='Choose the data source (mint or biogrid).')
    parser.add_argument('--output_folder', default='interactions', help='Output folder for interaction data (default: interactions).')
    parser.add_argument('--access_key', help='Access key for BioGRID API (required if source is biogrid).')

    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    if args.source == 'mint':
        get_mint_data(args.uniprot_ids, args.output_folder)
        interaction_partners = extract_interaction_partners_mint(args.uniprot_ids, args.output_folder)
        create_mfa(interaction_partners)
    elif args.source == 'biogrid':
        if not args.access_key:
            raise ValueError("Access key is required when the source is set to 'biogrid'.")
        get_biogrid_data(args.uniprot_ids, args.access_key, args.output_folder)
        # Uncomment the following line when the BioGRID function is implemented
        # interaction_partners = extract_interaction_partners_biogrid(args.uniprot_ids, args.output_folder)

    # Save the interaction partners dictionary as a JSON file
    with open(f"{args.output_folder}/interaction_partners.json", "w") as json_file:
        json.dump(interaction_partners, json_file, indent=2)

if __name__ == "__main__":
    main()