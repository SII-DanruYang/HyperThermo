import os
import hashlib
import json

root="."

files=[]

for base,dirs,fs in os.walk("data"):
    for f in fs:
        path=os.path.join(base,f)
        files.append(path)

for base,dirs,fs in os.walk("results/frozen"):
    for f in fs:
        path=os.path.join(base,f)
        files.append(path)


out=[]

for f in sorted(files):
    h=hashlib.md5(open(f,'rb').read()).hexdigest()
    out.append({
        "file":f,
        "size":os.path.getsize(f),
        "md5":h
    })


os.makedirs("docs",exist_ok=True)

json.dump(
    out,
    open("docs/release_manifest.json","w"),
    indent=2
)

print("FILES:",len(out))
print("saved docs/release_manifest.json")
