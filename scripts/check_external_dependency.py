
from pathlib import Path
import re

root=Path(".")

bad=[]

for p in root.rglob("*.py"):

    txt=p.read_text(errors="ignore")

    for line in txt.splitlines():

        if "HyperThermo_paper_complete" in line:
            bad.append(
                (str(p),line.strip())
            )

        if "../" in line:
            bad.append(
                (str(p),line.strip())
            )


print("\nExternal references:\n")

for x in bad:
    print(x[0])
    print("   ",x[1])

print("\nCount:",len(bad))

