import json
from collections import defaultdict
from pathlib import Path
from hashlib import md5


path=Path(
"data/processed/theta_correction_dataset.jsonl"
)


groups=defaultdict(list)


with open(path) as f:

    for line in f:

        r=json.loads(line)

        seq=r.get("sequence")

        if seq:

            h=md5(
                seq.encode()
            ).hexdigest()

            groups[h].append(r)


for h,v in groups.items():

    if len(v)>1:

        print("\nHASH:",h)

        for r in v:

            print(
                r["id"],
                r.get("family")
            )

