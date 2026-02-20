# APP — Alienness by Phyletic Pattern

A reproducible bioinformatics pipeline for detecting horizontal gene transfer (HGT) candidate genes using multi-level phyletic pattern analysis across taxonomic groups (species, genus, and family) based on RefSeq proteomes.

---

## Overview

APP (Alienness by Phyletic Pattern) is a prototype pipeline designed to:

- Download and organize related proteomes from RefSeq
- Construct multi-level phyletic presence/absence profiles
- Identify genes with atypical taxonomic distribution
- Highlight potential HGT (alienness) candidates
- Generate genome-level summaries and clustering outputs

This repository represents a validated and structured implementation suitable for research prototyping and educational use.

---

## Scope and Scaling

This repository is designed for:

- Small to medium genome collections (tens to hundreds of genomes)

Scaling to very large datasets (e.g., 40,000–50,000 genomes) requires:

- Replacing BLAST-style steps with DIAMOND or MMseqs2
- Parallelized workflow managers (Snakemake or Nextflow)
- HPC infrastructure
- Optimized storage and I/O handling

This repository provides the architectural foundation for such scaling.

---

## Repository Structure

```
database/               Supporting metadata resources
scripts/                Helper and preprocessing scripts
download_relatives.py   Proteome retrieval module
genomic_map.py          Genome mapping utilities
APP.pl                  Original APP implementation
APP_methodology.png     Workflow diagram
LICENSE                 MIT license
README.md               Project documentation
```

---

## Installation

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate:

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Typical Workflow

1. Retrieve lineage metadata from RefSeq
2. Download related proteomes
3. Organize FASTA structure
4. Construct phyletic presence/absence matrices
5. Identify genes with atypical distribution
6. Generate summary outputs and visualizations

---

## Inputs

- RefSeq assembly metadata
- Protein FASTA files (`*.faa` or `*.faa.gz`)
- Taxonomic lineage information

---

## Outputs

- Organized proteome structure
- Phyletic pattern tables
- Candidate alienness gene lists
- Optional clustering summaries and plots

---

## Best Practices

This repository intentionally excludes:

- Large `.faa.gz` proteome files
- Large generated `.tsv` outputs
- Log files

Use `.gitignore` to prevent committing generated data.

---

## License

This project is released under the MIT License.  
See the LICENSE file for details.

---

## Citation

If you use this repository in academic work, please cite the repository and acknowledge the contributing laboratory.
