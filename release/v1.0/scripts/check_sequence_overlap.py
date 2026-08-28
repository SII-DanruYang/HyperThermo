
import json
import hashlib
from pathlib import Path
from collections import defaultdict


ROOT=Path("../HyperThermo_clean/data/splits")


seq_map=defaultdict(list)


if not ROOT.exists():

    print(
        "No split files found:",
        ROOT
    )

    exit()


for f in ROOT.rglob("*.jsonl"):

    with open(f) as fh:

        for line in fh:

            x=json.loads(line)


            seq=x.get(
                "sequence"
            )

            if seq:

                h=hashlib.md5(
                    seq.encode()
                ).hexdigest()


                seq_map[h].append(
                    {
                    "id":x.get("id"),
                    "file":str(f),
                    "split":x.get("split")
                    }
                )


print(
    "Sequences:",
    len(seq_map)
)


bad=0


for h,v in seq_map.items():

    if len(v)>1:

        bad+=1

        print(
            "\nLEAKAGE:",
            h
        )

        for x in v:
            print(x)


print(
    "\nDuplicate groups:",
    bad
)


