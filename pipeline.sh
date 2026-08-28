
#!/bin/bash


set -e


echo "Step 1 data preparation"
python scripts/01_prepare_data.py


echo "Step 2 split"
python scripts/02_make_split.py


echo "Step 3 feature extraction"
python scripts/03_extract_features.py


echo "Step 4 train"
python scripts/04_train_thermostate.py


echo "Step 5 predict"
python scripts/05_predict_theta.py


echo "Step 6 structural transfer"
python scripts/06_structural_transfer.py


echo "Step 7 figures"
python scripts/07_generate_figures.py


