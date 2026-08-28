import json
import hashlib
from pathlib import Path
from collections import Counter


INPUT = Path("data/processed/theta_correction_dataset.jsonl")
OUT = Path("data/splits")

OUT.mkdir(exist_ok=True)


TEST_FAMILIES = {
    "telomerase",
    "RNaseP"
}


def seq_hash(seq):
    return hashlib.sha256(
        seq.encode()
    ).hexdigest()


records=[]

with open(INPUT) as f:
    for line in f:
        r=json.loads(line)

        r["sequence_hash"]=seq_hash(
            r["sequence"]
        )

        records.append(r)


train=[]
test=[]


for r in records:

    if r["family"] in TEST_FAMILIES:
        r["split"]="test"
        test.append(r)

    else:
        r["split"]="train"
        train.append(r)


def save(name,data):

    with open(
        OUT/name,
        "w"
    ) as f:

        for r in data:
            f.write(
                json.dumps(r)
                +"\n"
            )


save(
    "theta_train.jsonl",
    train
)

save(
    "theta_test.jsonl",
    test
)


stats={

    "total":
        len(records),

    "train":
        len(train),

    "test":
        len(test),

    "train_families":
        sorted(
            set(
                r["family"]
                for r in train
            )
        ),

    "test_families":
        sorted(
            set(
                r["family"]
                for r in test
            )
        ),

    "sequence_overlap":
        len(
            set(
                r["sequence_hash"]
                for r in train
            )
            &
            set(
                r["sequence_hash"]
                for r in test
            )
        )
}


with open(
    OUT/"split_statistics.json",
    "w"
) as f:

    json.dump(
        stats,
        f,
        indent=2
    )


print(json.dumps(
    stats,
    indent=2
))
