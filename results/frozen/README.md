# Frozen Theta Correction Experiment

## Dataset
RNA sequences:
- total: 277
- train: 210
- test: 67

Family split:

Train:
- SRP
- tmRNA
- group_I_intron

Test:
- RNaseP
- telomerase

No sequence overlap.

## Input

Sequence-only features:

- length
- nucleotide composition
- dinucleotide frequencies

No structural information used.

## Target

Predict RNA-specific thermodynamic correction:

delta_theta = theta_RNA - theta_global

## Model

Ridge regression.

Files:

models/ridge_theta.pkl
models/theta_scaler.pkl

## Evaluation

Metrics:

- Pearson correlation
- cosine similarity
- MAE
- RMSE

## Ablation

GC only:
0.003108

Mononucleotide:
0.002208

Full sequence features:
0.0000238
