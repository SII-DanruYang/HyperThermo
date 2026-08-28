import json
from pathlib import Path
from hashlib import md5
from collections import defaultdict


ROOT=Path("data/processed")


files=list(ROOT.glob("*.jsonl"))


seq_hash=defaultdict(list)


print("=== FIELD AUDIT ===")


for f in files:

    rows=[]

    with open(f) as fh:
        for line in fh:
            rows.append(json.loads(line))


    print("\n",f.name)

    fields=set()

    for r in rows:
        fields.update(r.keys())


    print("fields:")
    print(sorted(fields))


    forbidden=[
        "true_pairs",
        "structure",
        "pairs",
        "pairmap"
    ]


    bad=fields.intersection(forbidden)

    if bad:
        print("WARNING forbidden:",bad)
    else:
        print("OK no structure leakage")


    for r in rows:

        if "sequence" in r:

            h=md5(
                r["sequence"].encode()
            ).hexdigest()

            seq_hash[h].append(
                (f.name,r["id"])
            )


print("\n=== SEQUENCE DUPLICATE AUDIT ===")

dup=0

for h,v in seq_hash.items():

    if len(v)>1:

        dup+=1

        print("\nHASH",h)

        for x in v:
            print(x)


print("\nduplicate sequence groups:",dup)
