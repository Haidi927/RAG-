import requests
import os

url_base = "http://lavis.cs.hs-rm.de/storage/spert/public/datasets/conll04/"
files = ["train.json", "dev.json", "test.json"]

save_dir = r"C:\PHD\2025\08\spert\data\datasets\conll04"
os.makedirs(save_dir, exist_ok=True)

for fname in files:
    url = url_base + fname
    path = os.path.join(save_dir, fname)
    print(f"Downloading {url} -> {path}")
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)

print("下载完成 ✅")
