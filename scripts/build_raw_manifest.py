
from pathlib import Path
import hashlib
import json


root=Path("../")

ext=[
".fa",
".fasta",
".ct",
".bpseq",
".dbn",
".sto"
]


records=[]


for p in root.rglob("*"):

    if p.is_file() and p.suffix in ext:

        md5=hashlib.md5(
            p.read_bytes()
        ).hexdigest()

        records.append(
            {
            "path":str(p),
            "size":p.stat().st_size,
            "md5":md5
            }
        )


Path("docs").mkdir(exist_ok=True)

json.dump(
    records,
    open("docs/raw_manifest.json","w"),
    indent=2
)


print("Files:",len(records))

