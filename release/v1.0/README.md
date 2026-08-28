
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


