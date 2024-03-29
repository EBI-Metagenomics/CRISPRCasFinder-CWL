cwlVersion: v1.2
class: CommandLineTool
label: CRIPRCasFinder2GFF
doc: |
      convert CRISPRCasFinder output to GFF.

requirements:
  ResourceRequirement:
    coresMin: 1
    ramMin: 2000
hints:
  DockerRequirement:
    dockerPull: microbiomeinformatics/pipeline-v5.crisprcasfinder:4.2.21

baseCommand: [ "crisprcf2gff.py" ]

inputs:
  seq_name:
    type: File
    label: sequence input file for renaming
  in_json:
    type: File
    label: input JSON file
    inputBinding:
      position: 1
      prefix: -j

arguments:
  - -o
  -  $(inputs.seq_name.nameroot)_CRISPRCasFinder.gff3

outputs:
  crisprcasfinder_gff:
    type: File
    format: edam:format_1975
    outputBinding:
      glob: '*_CRISPRCasFinder.gff3'
  
stdout: crisprcf2gff.log
stderr: crisprcf2gff.err

$namespaces:
 edam: http://edamontology.org/
 s: http://schema.org/
$schemas:
 - http://edamontology.org/EDAM_1.16.owl
 - https://schema.org/version/latest/schemaorg-current-https.rdf

s:license: "https://www.apache.org/licenses/LICENSE-2.0"
s:copyrightHolder: "EMBL - European Bioinformatics Institute"
s:dateCreated: 2021-04-14
