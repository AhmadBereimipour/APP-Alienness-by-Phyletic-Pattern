from pathlib import Path
import re
import pandas as pd

proteome = Path("../example/NC_004088.faa")
targets = set(Path("recent_like_genes.txt").read_text().split())

records = []
current = None

for line in proteome.open():
    if line.startswith(">"):
        header = line.strip()

        gene_id = header.split()[0][1:]

        if gene_id in targets:
            loc = re.search(r'\[(?:location|loc)=([^\]]+)\]', header)
            if loc:
                coords = loc.group(1)
                nums = re.findall(r'\d+', coords)
                if len(nums) >= 2:
                    start, end = int(nums[0]), int(nums[1])
                    records.append((gene_id, start, end))

df = pd.DataFrame(records, columns=["gene","start","end"])
df = df.sort_values("start")

df.to_csv("gene_positions.csv", index=False)

print(df)
