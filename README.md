# Data and Benchmark Repository: Integrating Molecular Orbital Theory with Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Journal: Digital Discovery (RSC)](https://img.shields.io/badge/Journal-Digital%20Discovery%20(RSC)-teal.svg)](https://pubs.rsc.org/en/journals/journalissues/dd)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)

This repository hosts the official curated benchmarks, electronic structure datasets, and metadata catalogs accompanying the review paper:

> **"Integrating Molecular Orbital Theory with Machine Learning: Practical Frameworks, Operator Approximations, and Physical Symmetries"**  
> **Authors:** [Vedant Mishra](mailto:vedantmishra0605@gmail.com) and [Anisha Garg](mailto:anishagarg2806@gmail.com)  
> **Affiliation:** Department of Chemistry, School of Advanced Sciences and Languages (SASL), Vellore Institute of Technology (VIT), Bhopal, Madhya Pradesh 466114, India  
> **Target Journal:** *Digital Discovery* (Royal Society of Chemistry)

---

## 🔬 Repository Overview

Modern machine learning surrogates for quantum chemistry accelerate electronic structure calculations by up to five orders of magnitude while preserving essential physical symmetries ($\mathrm{SO}(3)$ / $\mathrm{E}(3)$ equivariance). This repository consolidates the public benchmark datasets, Conceptual DFT indices, and operator-learning representations surveyed throughout the review.

```
Data---MOT-ML-Review/
├── README.md                           # Comprehensive documentation & metadata
├── LICENSE                             # MIT Open-Source License
├── CITATION.cff                        # Citation metadata (CFF format)
├── data/
│   ├── dataset_catalog.json            # Machine-readable catalog with DOIs and accession codes
│   ├── qm9_fmo_benchmark.csv           # QM9 B3LYP/6-31G(2df,p) frontier molecular orbitals
│   ├── qm9_fmo_calculated.csv          # Conceptual DFT reactivity indices (eta, mu, omega)
│   ├── pubchemqc_benchmark.csv         # PubChemQC electronic properties & UV-Vis absorption
│   ├── transition_metal_spin_states.csv # Fe/Co/Ni/Mn spin multiplicities & orbital splittings
│   ├── kinase_warheads_lumo.csv        # Targeted covalent inhibitor warheads & LUMO energies
│   ├── eas_regioselectivity_benchmark.csv # EAS directing effects & HOMO electron densities
│   ├── organic_photovoltaics_cep.csv   # Harvard Clean Energy Project OPV donor-acceptors
│   ├── ani1_conformational_pes.csv     # ANI-1 potential energy surface conformational scans
│   └── deeph_hamiltonian_blocks.json   # Equivariant atomic orbital Hamiltonian matrix blocks
└── scripts/
    ├── download_full_qm9.py            # Automated downloader for the 133k-molecule QM9 dataset
    ├── download_ani1.py                # Reference fetcher for the ANI-1 Zenodo archive
    └── calculate_fmo_descriptors.py    # Python utility to compute Conceptual DFT metrics
```

---

## 📊 Summary of Included Datasets

| Dataset | Primary Scope | Quantum Chemical Level | Key Properties |
| :--- | :--- | :--- | :--- |
| **`qm9_fmo_benchmark.csv`** | Small organic molecules ($\le 9$ heavy atoms) | B3LYP/6-31G(2df,p) | $\varepsilon_{\text{HOMO}}$, $\varepsilon_{\text{LUMO}}$, Gap, $\mu$, ZPVE |
| **`qm9_fmo_calculated.csv`** | Conceptual DFT descriptors | Parr--Pearson formalism | Hardness ($\eta$), Chem Potential ($\mu$), Electrophilicity ($\omega$) |
| **`pubchemqc_benchmark.csv`** | Drug-like & heteroaromatic molecules | B3LYP/6-31G* | Total Energy, Dipole, $\lambda_{\max}$ UV-Vis excitation |
| **`transition_metal_spin_states.csv`** | Fe(II), Fe(III), Co, Ni, Mn complexes | DFT / CASSCF references | Spin multiplicity, High/Low spin, $\Delta_{\text{oct}}$ splitting |
| **`kinase_warheads_lumo.csv`** | Targeted covalent inhibitor warheads | B3LYP / GNN predictions | Warhead LUMO, Global electrophilicity ($\omega$), Target residue |
| **`eas_regioselectivity_benchmark.csv`** | Functionalized arenes & heterocycles | Frontier Molecular Orbital (FMO) | $C_{r,\text{HOMO}}^2$, Wheland intermediate stability, Regioisomers |
| **`organic_photovoltaics_cep.csv`** | Conjugated OPV donor-acceptor polymers | BP86 / B3LYP screening | Optical bandgap ($E_g$), $V_{\text{oc}}$, PCE % surrogate |
| **`ani1_conformational_pes.csv`** | Off-equilibrium conformational scans | $\omega\text{B97X}$/6-31G* | Torsion profiles, relative energies, atomic forces |
| **`deeph_hamiltonian_blocks.json`** | Equivariant operator learning | STO-3G / def2-SVP | Diagonal/off-diagonal Fock matrix blocks $\mathbf{H}_{ij}, \mathbf{S}_{ij}$ |

---

## 🌐 External Benchmark Repositories & Accession Codes

All datasets referenced across this review originate from peer-reviewed public archives:

| Benchmark Resource | Public Repository | Persistent DOI / URL | Accession Identifier |
| :--- | :--- | :--- | :--- |
| **QM9 Benchmark** | Figshare / Materials Cloud | [10.6084/m9.figshare.c.978904.v5](https://doi.org/10.6084/m9.figshare.c.978904.v5) | `978904` / `2020.0026` |
| **PubChemQC Project** | RIKEN PubChemQC | [http://pubchemqc.riken.jp/](http://pubchemqc.riken.jp/) | `PubChemQC-PM6` |
| **ANI-1 Dataset** | Zenodo | [10.5281/zenodo.1184918](https://doi.org/10.5281/zenodo.1184918) | `1184918` |
| **Harvard Clean Energy Project** | Harvard Dataverse | [10.7910/DVN/944NX4](https://doi.org/10.7910/DVN/944NX4) | `DVN/944NX4` |
| **ChEMBL Database** | EMBL-EBI | [https://www.ebi.ac.uk/chembl/](https://www.ebi.ac.uk/chembl/) | `CHEMBL28` |

---

## 🚀 Quick Start & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/vmishra06-cdk/Data---MOT-ML-Review.git
cd Data---MOT-ML-Review
```

### 2. Compute Conceptual DFT Descriptors
To recalculate chemical hardness ($\eta$), chemical potential ($\mu$), and global electrophilicity index ($\omega$):
```bash
python3 scripts/calculate_fmo_descriptors.py
```

### 3. Download the Full QM9 Dataset (133k Molecules)
```bash
python3 scripts/download_full_qm9.py
```

---

## 📖 Citation

If you use these benchmark datasets or reference this work in your research, please cite:

```bibtex
@article{mishra2026integrating,
  author    = {Mishra, Vedant and Garg, Anisha},
  title     = {Integrating Molecular Orbital Theory with Machine Learning: Practical Frameworks, Operator Approximations, and Physical Symmetries},
  journal   = {Digital Discovery},
  year      = {2026},
  publisher = {Royal Society of Chemistry},
  note      = {Data repository available at: https://github.com/vmishra06-cdk/Data---MOT-ML-Review}
}
```

---

## 📜 License
This repository is licensed under the [MIT License](LICENSE).