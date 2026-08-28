
# HyperThermo

Thermodynamic prior mismatch diagnosis and correction for RNA folding.

## Pipeline

raw RNA data

↓

sequence preprocessing

↓

RNA-specific thermodynamic state representation

↓

theta correction prediction

↓

structure folding transfer

↓

evaluation


## Reproducibility

Run:

bash pipeline.sh


## Leakage control

All correction predictors are trained without access to:

- test structures
- oracle folding
- target base pairs




# Quick Start

## Environment

Create the environment:

```bash
conda env create -f environment.yml
conda activate hyperthermo
Reproduce HyperThermo pipeline

The complete analysis pipeline can be reproduced with:

bash run_pipeline.sh

The pipeline performs:

Clean dataset construction
Family-level train/test split generation
Thermodynamic correction target extraction
Sequence feature extraction
RNA-specific thermodynamic correction prediction

Outputs are generated under:

results/
features/
models/
Input Data Format

HyperThermo expects three input datasets under:

data/raw/
1. Thermodynamic correction dataset

File:

predicted_theta_277_FULL.jsonl

Each RNA record contains:

{
"id": "RNA_ID",
"family": "RNA_family",
"sequence": "AUGC...",
"theta_global": [],
"delta_theta": []
}
2. Thermostate validation dataset

File:

thermostate900_dev69_states.jsonl

Contains thermodynamic state information used for physical validation.

3. Structural transfer dataset

File:

b2p7c_structural_transfer_records.jsonl

Required fields:

{
"id": "...",
"split": "...",
"regime": "...",
"length": 0,
"global_f1": 0.0,
"oracle_f1": 0.0,
"delta_f1": 0.0
}
Reproducibility Notes

The released pipeline uses:

family-level train/test splitting
zero sequence overlap validation
no random RNA-level split
no PCA fitted on full data
no oracle information used during prediction
explicit data lineage tracking

All generated files are recorded in:

docs/release_manifest.json
Repository Structure
HyperThermo/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
├── features/
├── models/
├── results/
└── docs/

