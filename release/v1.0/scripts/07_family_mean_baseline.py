import json
import numpy as np
from sklearn.metrics import mean_absolute_error


def load(path):
    with open(path) as f:
        return [json.loads(x) for x in f]


train=load(
"data/splits/theta_train.jsonl"
)

test=load(
"data/splits/interface/theta_test_target.jsonl"
)


# global training mean
ys=[]

for r in train:
    ys.append(r["delta_theta"])

mean=np.mean(
    np.array(ys),
    axis=0
)


pred=[]
true=[]


for r in test:

    pred.extend(
        mean
    )

    true.extend(
        r["delta_theta"]
    )


print(
"family mean baseline MAE:",
np.mean(
    np.abs(
        np.array(pred)
        -
        np.array(true)
    )
))

