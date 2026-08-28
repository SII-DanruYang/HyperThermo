import os
import json
import hashlib
from pathlib import Path


ROOT=Path(".")


files=[]

for p in ROOT.rglob("*"):
    if p.is_file():
        if any(x in str(p) for x in [
            "results",
            "figures/data"
        ]):
            h=hashlib.md5(
                open(p,"rb").read()
            ).hexdigest()

            files.append({
                "path":str(p),
                "size":p.stat().st_size,
                "md5":h
            })


with open(
"docs/audit/result_manifest.json",
"w"
) as f:
    json.dump(
        files,
        f,
        indent=2
    )

print("files:",len(files))
