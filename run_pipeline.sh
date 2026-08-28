#!/bin/bash

set -e

echo "=============================="
echo " HyperThermo Clean Pipeline"
echo "=============================="

python scripts/00_build_clean_dataset.py

python scripts/02_make_split.py

python scripts/03_split_targets.py

python scripts/04_extract_features.py

python scripts/05_train_theta_model.py

echo "=============================="
echo " DONE"
echo "=============================="
