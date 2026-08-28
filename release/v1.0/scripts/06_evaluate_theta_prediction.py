import json
import numpy as np

from pathlib import Path
from scipy.stats import pearsonr
from sklearn.metrics import mean_absolute_error, mean_squared_error


RESULT=Path("results")
DATA=Path("data/splits/interface")


def load(path):

    with open(path) as f:
        return [
            json.loads(x)
            for x in f
        ]


pred=load(
    RESULT/"theta_test_prediction.jsonl"
)

target=load(
    DATA/"theta_test_target.jsonl"
)


target_map={
    x["id"]:x["delta_theta"]
    for x in target
}


ys=[]
yp=[]

family={}


for r in pred:

    y=np.array(
        target_map[r["id"]]
    )

    p=np.array(
        r["pred_delta_theta"]
    )


    ys.extend(y)
    yp.extend(p)


    fam=r["family"]

    if fam not in family:
        family[fam]={
            "y":[],
            "p":[]
        }

    family[fam]["y"].extend(y)
    family[fam]["p"].extend(p)



ys=np.array(ys)
yp=np.array(yp)


summary={

"N_RNA":len(pred),

"N_components":len(ys),

"pearson":
    float(pearsonr(ys,yp)[0]),

"cosine":
    float(
        np.dot(ys,yp)
        /
        (
        np.linalg.norm(ys)
        *
        np.linalg.norm(yp)
        )
    ),

"MAE":
    float(mean_absolute_error(ys,yp)),

"RMSE":
    float(
        mean_squared_error(
            ys,
            yp
        )**0.5
    )
}


print(json.dumps(
    summary,
    indent=2
))


for fam,v in family.items():

    y=np.array(v["y"])
    p=np.array(v["p"])

    print(
        fam,
        "N=",
        len(y),
        "MAE=",
        float(
            np.mean(abs(y-p))
        )
    )


with open(
    RESULT/"theta_prediction_summary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=2
    )

