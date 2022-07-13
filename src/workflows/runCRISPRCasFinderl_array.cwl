cwlVersion: v1.2
class: Workflow
label: runCRISPRCasFinder
doc: |
      Implementation of CRISPRCasFinder processing for multiple input fasta files.

requirements:
  SubworkflowFeatureRequirement: {}
  ResourceRequirement:
    coresMin: 1
    ramMin: 2000
  ScatterFeatureRequirement: {}

inputs:
  sequences:
    type: File[]
    format: edam:format_1929
    label: input Fasta file to analyze
  soFile:
    type: string?
    label: path to the sel392v2.so file, required by vmatch
    default: /opt/CRISPRCasFinder/sel392v2.so
  cas_definition:
    type: enum
    symbols:
        - G
        - T
        - S
    label: Cas-finder definition, such as G (general), T (Typing) or S (Subtyping)
    default: G

outputs:
  crisprcasfinder_fasta:
    type: File[]
    format: edam:format_1929
    outputSource: full_wf/crisprcasfinder_fasta
  crisprcasfinder_gff:
    type: File[]
    format: edam:format_1975
    outputSource: full_wf/crisprcasfinder_gff

steps:
    full_wf:
      label: run full CRIPRCasFinder workflow for multiple files
      run: runCRISPRCasFinderl.cwl
      scatter: sequences
      in:
        sequences: sequences
        soFile: soFile
        cas_definition: cas_definition
      out:
        - crisprcasfinder_fasta
        - crisprcasfinder_gff

$namespaces:
 edam: http://edamontology.org/
 s: http://schema.org/
$schemas:
 - http://edamontology.org/EDAM_1.16.owl
 - https://schema.org/version/latest/schemaorg-current-https.rdf

s:license: "https://www.apache.org/licenses/LICENSE-2.0"
s:copyrightHolder: "EMBL - European Bioinformatics Institute"
s:dateCreated: 2022-07-07
