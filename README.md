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
