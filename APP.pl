@'
import urllib.request
from pathlib import Path

lines = Path("assembly_summary_refseq.txt").read_text(errors="ignore").splitlines()
hdr = next(l for l in lines if l.startswith("#assembly_accession")).lstrip("#").split("\t")
idx = {n:i for i,n in enumerate(hdr)}

acc_i = idx["assembly_accession"]
org_i = idx["organism_name"]
ftp_i = idx["ftp_path"]

rows = [r.split("\t") for r in lines if r and not r.startswith("#")]

def pick(substr, n):
    out = []
    for cols in rows:
        if len(cols) <= max(acc_i, org_i, ftp_i):
            continue
        org = cols[org_i]
        base = cols[ftp_i].strip()
        if not base or base.lower() == "na":
            continue
        # base is already https in your file, but keep it robust anyway
        base = base.replace("ftp://ftp.ncbi.nlm.nih.gov", "https://ftp.ncbi.nlm.nih.gov")

        if substr.lower() in org.lower():
            asm_dir = base.rstrip("/").split("/")[-1]  # e.g. GCF_000006645.1_ASM664v1
            out.append((org, asm_dir, base))
        if len(out) >= n:
            break
    return out

pestis   = pick("Yersinia pestis", 5)
yersinia = pick("Yersinia", 10)

def download(group, items):
    Path(group).mkdir(exist_ok=True)
    for org, asm_dir, base in items:
        url = f"{base}/{asm_dir}_protein.faa.gz"
        out = Path(group) / f"{asm_dir}.faa.gz"
        if out.exists():
            continue
        print("Downloading", asm_dir, "-", org)
        urllib.request.urlretrieve(url, out)

print("Selected pestis:", len(pestis), "Selected yersinia:", len(yersinia))
download("pestis", pestis)
download("yersinia", yersinia)
print("DONE.")
'@ | Set-Content -Encoding UTF8 .\download_relatives.py
