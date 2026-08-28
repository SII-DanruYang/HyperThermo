
import json
from pathlib import Path


files=list(Path(".").rglob("*.jsonl"))


records=[]


for f in files:

    try:

        with open(f) as fh:

            for line in fh:

                x=json.loads(line)

                if "id" in x:

                    records.append(
                        {
                            "id":x["id"],
                            "file":str(f),
                            "split":x.get("split","NA")
                        }
                    )

    except:
        pass


ids={}


for r in records:

    ids.setdefault(
        r["id"],
        []
    ).append(r)


print("Total IDs:",len(ids))


print("\nPotential overlap:")

for k,v in ids.items():

    splits=set(
        x["split"]
        for x in v
    )

    if len(splits)>1:

        print(
            k,
            splits
        )

