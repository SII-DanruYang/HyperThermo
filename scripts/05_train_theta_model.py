import json
import numpy as np

from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import joblib


FEATURE_DIR=Path("features")
DATA_DIR=Path("data/splits/interface")

MODEL_DIR=Path("models")
RESULT_DIR=Path("results")

MODEL_DIR.mkdir(exist_ok=True)
RESULT_DIR.mkdir(exist_ok=True)


def load_jsonl(path):

    with open(path) as f:
        return [
            json.loads(x)
            for x in f
        ]


def vectorize(r):

    keys=[
        "length",
        "A_frac",
        "U_frac",
        "G_frac",
        "C_frac",
        "GC_frac"
    ]

    keys += [
        "di_"+a+b
        for a in "AUCG"
        for b in "AUCG"
    ]


    x=[
        r[k]
        for k in keys
    ]


    x += r["theta_global"]

    return np.array(x,dtype=float)



# -----------------
# train
# -----------------

train_feat=load_jsonl(
    FEATURE_DIR/"theta_train_features.jsonl"
)


train_target=load_jsonl(
    DATA_DIR/"theta_train_target.jsonl"
)


target_map={
    x["id"]:x["delta_theta"]
    for x in train_target
}


X=[]
Y=[]


for r in train_feat:

    X.append(
        vectorize(r)
    )

    Y.append(
        target_map[r["id"]]
    )


X=np.array(X)
Y=np.array(Y)



scaler=StandardScaler()

X=scaler.fit_transform(X)


model=Ridge(
    alpha=1.0
)

model.fit(
    X,
    Y
)



joblib.dump(
    scaler,
    MODEL_DIR/"theta_scaler.pkl"
)


joblib.dump(
    model,
    MODEL_DIR/"ridge_theta.pkl"
)



# -----------------
# test
# -----------------

test_feat=load_jsonl(
    FEATURE_DIR/"theta_test_features.jsonl"
)


Xt=np.array(
    [
        vectorize(x)
        for x in test_feat
    ]
)


Xt=scaler.transform(Xt)


pred=model.predict(Xt)


out=[]


for r,p in zip(test_feat,pred):

    out.append({

        "id":r["id"],

        "family":r["family"],

        "pred_delta_theta":
            p.tolist()

    })


with open(
    RESULT_DIR/"theta_test_prediction.jsonl",
    "w"
) as f:

    for r in out:
        f.write(
            json.dumps(r)+"\n"
        )


print("train samples:",len(X))
print("test samples:",len(Xt))
print("DONE")

