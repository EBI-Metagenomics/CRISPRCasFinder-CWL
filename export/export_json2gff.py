#!/usr/bin/env python3

# export_json2gff.py
# Script to convert the CRISPRCasFinder output (result.json) to GFF3
# (C) 2021 EMBL - EBI

import json
import argparse

def getCrisprAttributes(crispr):
    attr = []
    return attr

parser = argparse.ArgumentParser(description="Converts a CRISPRCasFinder JSON to GFF3")
parser.add_argument('-i', "--input", help="Input JSON", action='store', type=str, required=True)
parser.add_argument('-o', "--output", help="Output GFF3", action='store', type=str, required=True)

args = parser.parse_args()

input_json = args.input
out_file   = args.output

with open(input_json, "r") as json_file:
    data = json.load(json_file)

oh = open(out_file, "w")
oh.write("##gff-version 3\n")

if "Sequences" in data:
    for seq in data["Sequences"]:
        seq_id = seq["Id"]
        if "Cas" in seq:
            for cas in seq["Cas"]:
                cas_id = "{}_{}_{}_{}".format(seq_id, cas["Type"], str(cas["Start"]), str(cas["End"]))
                cas_label = "Id={};Type={}".format(cas_id, cas["Type"])
                oh.write("\t".join([
                                    seq_id,
                                    ".",
                                    "region",
                                    str(cas["Start"]),
                                    str(cas["End"]),
                                    ".",
                                    ".",
                                    ".",
                                    cas_label
                                ]))
                oh.write("\n")

                if "Genes" in cas:
                    for gen in cas["Genes"]:
                        gen_id = "{}_{}_{}_{}".format(seq_id, gen["Sub_type"], str(gen["Start"]), str(gen["End"]))
                        gen_label="Id={};Parent={}".format(gen_id, cas_id)
                        oh.write("\t".join([
                                            seq_id,
                                            ".",
                                            "gene",
                                            str(gen["Start"]),
                                            str(gen["End"]),
                                            ".",
                                            gen["Orientation"],
                                            ".",
                                            gen_label
                                        ]))
                        oh.write("\n")
        else:
            print("no Cas found")

        if "Crispr" in seq:
            for crs in seq["Crisprs"]:
                crs_id = crs["Name"]
                crs_attr = getCrisprAttributes(crs)
                crs_label = ";".join["Id={}".format(crs_id), crs_attr)]
                oh.write("\t".join([
                                    seq_id,
                                    ".",
                                    "region",
                                    str(crs["Start"]),
                                    str(crs["End"]),
                                    ".",
                                    crs["Potential_Orientation"],
                                    ".",
                                    crs_label
                                ]))
                        oh.write("\n")
        else:
            print("no CRISPR found")

else:
    print("no sequences found")


oh.close()