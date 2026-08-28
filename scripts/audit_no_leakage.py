
import json
from pathlib import Path


ROOT=Path(".")


print("="*60)
print("HyperThermo leakage audit")
print("="*60)


checks=[]


# check forbidden files

forbidden=[
    "oracle",
    "true_pairs",
    "target_structure",
    "validation_target"
]


for p in ROOT.rglob("*"):

    if p.is_file():

        name=str(p).lower()

        for f in forbidden:

            if f in name:

                checks.append(
                    ("WARNING",str(p))
                )


if checks:

    print("\nPotential leakage files:")
    for x in checks:
        print(x)

else:

    print("No suspicious filenames detected")


print("\nAudit finished")

