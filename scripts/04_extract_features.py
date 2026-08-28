import json
from pathlib import Path
from collections import Counter


IN_DIR = Path("data/splits/interface")
OUT_DIR = Path("features")

OUT_DIR.mkdir(exist_ok=True)


def seq_features(seq):

    seq = seq.upper()

    n=len(seq)

    c=Counter(seq)

    feat={
        "length":n,

        "A_frac":c["A"]/n,
        "U_frac":c["U"]/n,
        "G_frac":c["G"]/n,
        "C_frac":c["C"]/n,

        "GC_frac":(c["G"]+c["C"])/n,

    }


    # dinucleotide

    for a in "AUCG":
        for b in "AUCG":
            pair=a+b
            count=sum(
                seq[i:i+2]==pair
                for i in range(n-1)
            )
            feat["di_"+pair]=count/(n-1)


    return feat



def process(split):

    infile=IN_DIR/f"theta_{split}_input.jsonl"

    outfile=OUT_DIR/f"theta_{split}_features.jsonl"


    with open(infile) as f, open(outfile,"w") as out:

        for line in f:

            r=json.loads(line)


            feat=seq_features(
                r["sequence"]
            )


            feat.update({

                "id":r["id"],

                "family":r["family"],

                "theta_global":r["theta_global"],

                "split":r["split"]

            })


            out.write(
                json.dumps(feat)+"\n"
            )


    print(outfile)



for s in ["train","test"]:
    process(s)


print("DONE")
