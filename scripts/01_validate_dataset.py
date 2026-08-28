import json
from pathlib import Path
from collections import Counter


ROOT=Path("data/processed")


rules={

"theta_correction_dataset.jsonl":
[
"id",
"family",
"length",
"theta_global",
"delta_theta"
],

"thermostate_prediction_dataset.jsonl":
[
"id",
"representation",
"delta_thermostate"
],

"structural_transfer_dataset.jsonl":
[
"id",
"global_f1",
"oracle_f1",
"delta_f1"
],

"oracle_alignment_dataset.jsonl":
[
"id",
"pred_delta_theta",
"true_delta_theta",
"cos_similarity"
]

}


for file,required in rules.items():

    path=ROOT/file

    if not path.exists():
        print("MISSING",file)
        continue


    rows=[]

    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))


    print("\n====",file)

    print("N =",len(rows))


    missing=[]

    for r in rows:
        for k in required:
            if k not in r:
                missing.append(k)


    if missing:
        print(
            "missing fields:",
            Counter(missing)
        )
    else:
        print("schema OK")


    ids=[r["id"] for r in rows]

    dup=len(ids)-len(set(ids))

    print(
        "duplicate IDs:",
        dup
    )


print("\nAUDIT DONE")
