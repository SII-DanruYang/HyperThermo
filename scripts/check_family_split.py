
import json
from pathlib import Path
from collections import defaultdict


families=defaultdict(set)


for f in Path("results").rglob("*.jsonl"):

    with open(f) as fh:

        for line in fh:

            try:
                x=json.loads(line)
            except:
                continue


            if "family" in x and "split" in x:

                families[x["family"]].add(
                    x["split"]
                )


print("Family appearing in multiple splits:")


for fam,splits in families.items():

    if len(splits)>1:

        print(
            fam,
            splits
        )

