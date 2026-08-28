import json
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error


def load(path):
    with open(path) as f:
        return [json.loads(x) for x in f]


train=load(
"features/theta_train_features.jsonl"
)

test=load(
"features/theta_test_features.jsonl"
)


targets_train=load(
"data/splits/interface/theta_train_target.jsonl"
)

targets_test=load(
"data/splits/interface/theta_test_target.jsonl"
)


def target_map(records):
    return {
        r["id"]:np.array(r["delta_theta"])
        for r in records
    }


yt=target_map(targets_train)
yv=target_map(targets_test)


def run(name, keys):

    X=[]
    Y=[]

    for r in train:
        X.append(
            [r[k] for k in keys]
        )
        Y.append(
            yt[r["id"]]
        )


    Xt=[]
    Yt=[]

    for r in test:
        Xt.append(
            [r[k] for k in keys]
        )
        Yt.append(
            yv[r["id"]]
        )


    scaler=StandardScaler()

    X=np.array(X)
    Xt=np.array(Xt)
    Y=np.array(Y)
    Yt=np.array(Yt)

    X=scaler.fit_transform(X)
    Xt=scaler.transform(Xt)

    model=Ridge(alpha=1.0)

    model.fit(
        X,
        Y
    )

    pred=model.predict(
        Xt
    )


    print(
        name,
        mean_absolute_error(
            np.array(Yt),
            pred
        )
    )


run(
"GC",
[
"GC_frac"
]
)


run(
"mono",
[
"A_frac",
"U_frac",
"G_frac",
"C_frac",
]
)


run(
"full",
[
k
for k in train[0]
if k.startswith("di_")
]+[
"A_frac",
"U_frac",
"G_frac",
"C_frac",
"length"
]
)

