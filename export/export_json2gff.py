#!/usr/bin/env python3

# export_json2gff.py
# Script to convert the CRISPRCasFinder output (result.json) to GFF3
# (C) 2021 EMBL - EBI

import json
import argparse

parser = argparse.ArgumentParser(description="Converts a CRISPRCasFinder JSON to GFF3")
parser.add_argument('-i', "--input", help="Input JSON", action='store', type=str, required=True)
parser.add_argument('-o', "--output", help="Output GFF3", action='store', type=str, required=True)

args = parser.parse_args()

input_json = args.input

with open(input_json, "r") as json_file:
    data = json.load(json_file)


