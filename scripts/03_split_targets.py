import json
from pathlib import Path


SRC = Path("data/splits")

OUT = Path("data/splits/interface")

OUT.mkdir(exist_ok=True)


def process(name):

    records=[]

    with open(SRC/name) as f:
        for line in f:
            records.append(json.loads(line))


    inputs=[]
    targets=[]


    for r in records:

        inputs.append({
            "id":r["id"],
            "family":r["family"],
            "length":r["length"],
            "sequence":r["sequence"],
            "theta_global":r["theta_global"],
            "sequence_hash":r["sequence_hash"],
            "split":r["split"]
        })


        targets.append({
            "id":r["id"],
            "delta_theta":r["delta_theta"]
        })


    stem=name.replace(".jsonl","")


    with open(
        OUT/(stem+"_input.jsonl"),
        "w"
    ) as f:
        for r in inputs:
            f.write(json.dumps(r)+"\n")


    with open(
        OUT/(stem+"_target.jsonl"),
        "w"
    ) as f:
        for r in targets:
            f.write(json.dumps(r)+"\n")


for x in [
    "theta_train.jsonl",
    "theta_test.jsonl"
]:
    process(x)


print("DONE")
