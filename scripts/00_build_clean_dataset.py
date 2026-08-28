import json
import os
from pathlib import Path
from collections import Counter


SRC = Path("data/raw")

OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)


def read_jsonl(path):
    data=[]
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data



# =====================================================
# Figure1 dataset
# theta correction learning
# =====================================================

src1 = SRC / "predicted_theta_277_FULL.jsonl"

records = read_jsonl(src1)


theta_dataset=[]


for r in records:

    theta_dataset.append({

        "id": r["id"],

        "family": r.get("family","unknown"),

        "length": r["length"],

        "sequence": r.get("sequence",None),

        # fixed thermodynamic prior
        "theta_global": r["theta_global"],

        # learned correction target
        "delta_theta": r["delta_theta_pred"],


        # only for evaluation,
        # NOT used during training
        "true_pairs": r.get("true_pairs",None),


        "source":
            "predicted_theta_277_FULL.jsonl"

    })


with open(
    OUT/"theta_correction_dataset.jsonl",
    "w"
) as f:

    for x in theta_dataset:
        f.write(
            json.dumps(x)+"\n"
        )

print(
    "theta dataset:",
    len(theta_dataset)
)



# =====================================================
# Figure2 dataset
# Thermostate prediction
# =====================================================


src2 = SRC / "thermostate900_dev69_states.jsonl"


records = read_jsonl(src2)


thermo=[]


for r in records:

    thermo.append({

        "id": r["id"],

        "split": r.get("split"),

        "length": r["length"],


        "representation":
            r["representation"],


        # target
        "delta_thermostate":
            r["delta_thermostate"],


        # prediction
        "prediction_delta_centered":
            r["prediction_delta_centered"],


        "source":
            "thermostate900_dev69_states.jsonl"

    })



with open(
    OUT/"thermostate_prediction_dataset.jsonl",
    "w"
) as f:

    for x in thermo:
        f.write(json.dumps(x)+"\n")


print(
    "thermostate dataset:",
    len(thermo)
)



# =====================================================
# Figure3 structural transfer
# =====================================================


src3 = Path("data/raw/b2p7c_structural_transfer_records.jsonl")

if src3.exists():


    records = read_jsonl(src3)

    transfer=[]

    for r in records:

        transfer.append({

            "id":r.get("id", r.get("name", "unknown")),

            "split":r.get("split"),

            "regime":r.get("regime"),

            "length":r.get("length"),


            "global_f1":
                r["global_f1"],

            "oracle_f1":
                r["oracle_f1"],

            "delta_f1":
                r["delta_f1"],


            "source":
            "b2p7c_structural_transfer_records.jsonl"

        })


    with open(
        OUT/"structural_transfer_dataset.jsonl",
        "w"
    ) as f:

        for x in transfer:
            f.write(json.dumps(x)+"\n")


    print(
        "transfer dataset:",
        len(transfer)
    )



# =====================================================
# Figure4 mechanism alignment
# =====================================================


src4 = SRC.parent/"mechanism"/"oracle_alignment.jsonl"


if src4.exists():

    records=read_jsonl(src4)

    alignment=[]


    for r in records:

        alignment.append({

            "id":r.get("id", r.get("name", "unknown")),

            "pred_delta_theta":
                r["pred_delta_theta"],

            "true_delta_theta":
                r["true_delta_theta"],

            "cos_similarity":
                r["cos_similarity"],


            "source":
            "oracle_alignment.jsonl"

        })


    with open(
        OUT/"oracle_alignment_dataset.jsonl",
        "w"
    ) as f:

        for x in alignment:
            f.write(json.dumps(x)+"\n")


    print(
        "alignment dataset:",
        len(alignment)
    )


print("\nDONE")
