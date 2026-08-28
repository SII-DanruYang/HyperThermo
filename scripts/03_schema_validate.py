import json
from pathlib import Path


checks = {

"theta_correction_dataset.jsonl":
{
"id",
"family",
"length",
"sequence",
"theta_global",
"delta_theta"
},

"theta_oracle_dataset.jsonl":
{
"id",
"true_pairs"
},

"thermostate_prediction_dataset.jsonl":
{
"id",
"length",
"representation",
"delta_thermostate"
},

"structural_transfer_dataset.jsonl":
{
"id",
"length",
"global_f1",
"oracle_f1",
"delta_f1"
}

}


root=Path("data/processed")


for file,required in checks.items():

    path=root/file

    print("\n====",file)

    with open(path) as f:
        r=json.loads(next(f))

    keys=set(r.keys())

    print(keys)

    missing=required-keys

    if missing:
        print("ERROR missing:",missing)
    else:
        print("SCHEMA OK")

    if "true_pairs" in keys and file!="theta_oracle_dataset.jsonl":
        print("ERROR STRUCTURE LEAKAGE")


print("\nDONE")
