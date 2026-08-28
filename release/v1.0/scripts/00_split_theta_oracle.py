import json
from pathlib import Path


src = Path("data/raw/predicted_theta_277_FULL.jsonl")

out_theta = Path("data/processed/theta_correction_dataset.jsonl")
out_oracle = Path("data/processed/theta_oracle_dataset.jsonl")

out_theta.parent.mkdir(parents=True, exist_ok=True)


theta_records=[]
oracle_records=[]


with open(src) as f:
    for line in f:
        r=json.loads(line)

        theta_records.append({
            "id": r["id"],
            "family": r["family"],
            "length": r["length"],
            "sequence": r["sequence"],
            "theta_global": r["theta_global"],
            "delta_theta": r["delta_theta_pred"]
        })

        oracle_records.append({
            "id": r["id"],
            "true_pairs": r["true_pairs"]
        })


with open(out_theta,"w") as f:
    for r in theta_records:
        f.write(json.dumps(r)+"\n")


with open(out_oracle,"w") as f:
    for r in oracle_records:
        f.write(json.dumps(r)+"\n")


print("theta:",len(theta_records))
print("oracle:",len(oracle_records))
print("DONE")
