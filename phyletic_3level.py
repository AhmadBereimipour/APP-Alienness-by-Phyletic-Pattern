@'
from pathlib import Path

K = 8
THRESH = 0.20

def read_faa(path: Path):
    sid = None
    seq = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if sid is not None:
                    yield sid, "".join(seq)
                sid = line[1:].split()[0]
                seq = []
            else:
                seq.append(line)
        if sid is not None:
            yield sid, "".join(seq)

def kmers(s: str, k: int):
    if len(s) < k:
        return set()
    return {s[i:i+k] for i in range(len(s)-k+1)}

def build_db(paths):
    db = {}
    for p in paths:
        allk = set()
        n = 0
        for _, seq in read_faa(p):
            n += 1
            allk |= kmers(seq, K)
        db[p.name] = allk
    return db

def frac_present(qk, db, paths):
    if not qk:
        return 0.0
    hits = 0
    for p in paths:
        sk = db[p.name]
        score = len(qk & sk)/len(qk)
        if score >= THRESH:
            hits += 1
    return hits/len(paths) if paths else 0.0

def main():
    pestis = sorted(Path("pestis").glob("*.faa"))
    yers   = sorted(Path("yersinia").glob("*.faa"))
    fam    = sorted(Path("family").glob("*.faa"))

    if not pestis: raise SystemExit("Missing pestis/*.faa")
    if not yers:   raise SystemExit("Missing yersinia/*.faa")
    if not fam:    raise SystemExit("Missing family/*.faa")

    query = Path(r"..\example\NC_004088.faa")
    if not query.exists():
        raise SystemExit("Query missing: ..\\example\\NC_004088.faa")

    print("Indexing species (pestis)...")
    db_sp = build_db(pestis)
    print("Indexing genus (yersinia)...")
    db_ge = build_db(yers)
    print("Indexing family (enterobacteriaceae)...")
    db_fa = build_db(fam)

    out = Path("phyletic_3level.tsv")
    out.write_text(
        "gene\tspecies_frac\tgenus_frac\tfamily_frac\trecent_like\tancient_like\n",
        encoding="utf-8"
    )

    recent_n = 0
    ancient_n = 0

    with open(out, "a", encoding="utf-8") as w:
        for gid, seq in read_faa(query):
            qk = kmers(seq, K)

            sp = frac_present(qk, db_sp, pestis)
            ge = frac_present(qk, db_ge, yers)
            fa = frac_present(qk, db_fa, fam)

            # working theory thresholds
            recent_like  = 1 if (sp <= 0.30 and ge <= 0.30 and fa >= 0.70) else 0
            ancient_like = 1 if (sp <= 0.30 and ge >= 0.70 and fa >= 0.70) else 0

            recent_n += recent_like
            ancient_n += ancient_like

            w.write(f"{gid}\t{sp:.2f}\t{ge:.2f}\t{fa:.2f}\t{recent_like}\t{ancient_like}\n")

    print("Wrote:", out)
    print("Recent-like candidates:", recent_n)
    print("Ancient-like candidates:", ancient_n)

if __name__ == "__main__":
    main()
'@ | Set-Content -Encoding UTF8 .\phyletic_3level.py
