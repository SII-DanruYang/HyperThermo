
from pathlib import Path
import json
import hashlib


ROOT = Path(".")


def md5(path):

    h = hashlib.md5()

    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)

    return h.hexdigest()


files=[]


for p in ROOT.rglob("*"):

    if p.is_file():

        if (
            p.suffix in [
                ".jsonl",
                ".csv",
                ".json"
            ]
        ):

            files.append(
                {
                    "file":str(p),
                    "size":p.stat().st_size,
                    "md5":md5(p)
                }
            )


print(json.dumps(
    files,
    indent=2
))


with open(
    "docs/data_lineage_raw.json",
    "w"
) as f:

    json.dump(
        files,
        f,
        indent=2
    )


print(
    "saved docs/data_lineage_raw.json"
)

