# APP — Alienness by Phyletic Pattern

A prototype/teaching pipeline for detecting **alienness (HGT candidates)** using **phyletic pattern analysis** across taxonomic levels (species/genus/family), starting from RefSeq protein FASTA datasets.

> **Scope note (important):** This repository is a correct and reproducible pipeline for **small–medium genome sets** (tens to hundreds).  
> Scaling to **tens of thousands (e.g., 40–50k genomes)** requires replacing BLAST-style steps with **DIAMOND/MMseqs2**, adding a workflow manager (Snakemake/Nextflow), and running on HPC.

---

## What this repository contains

- `download_relatives.py` — download and organize “relative” proteomes from NCBI/RefSeq metadata  
- `genomic_map.py` — generate genome/protein mapping utilities  
- `scripts/` — helper scripts (unzip, preprocessing, etc.)
- `database/` — supporting metadata/resources used by the pipeline  
- `APP_methodology.png` — high-level workflow diagram

---

## Quick start

### 1) Create an environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

python download_relatives.py
python genomic_map.py
# then run downstream analysis scripts as needed

Inputs and outputs (high-level)

Inputs

RefSeq/NCBI metadata (e.g., assembly summaries / FTP links)

Protein FASTA files (*.faa or *.faa.gz) for target and relatives

Typical outputs

Organized relatives database by taxonomic level

Phyletic pattern tables (presence/absence profiles)

Candidate lists highlighting “recent-like” phyletic signatures

Optional clustering/plots

Recommended repository practice

This repo should remain lightweight:

✅ keep code + docs + small examples

❌ avoid committing large downloaded datasets (*.faa.gz) and large generated outputs (*.tsv)

Use .gitignore to prevent accidental uploads.

Citation

If you use or build on this repository in academic work, please cite the repository and acknowledge the contributing lab/team.

