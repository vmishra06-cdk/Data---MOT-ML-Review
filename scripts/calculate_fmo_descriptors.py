#!/usr/bin/env python3
"""
calculate_fmo_descriptors.py
Calculates frontier molecular orbital (FMO) reactivity indices from HOMO and LUMO eigenvalues:
- HOMO-LUMO Gap: Delta_E = LUMO - HOMO
- Chemical Hardness: eta = (LUMO - HOMO) / 2
- Electronic Chemical Potential: mu = (HOMO + LUMO) / 2
- Electronegativity: chi = -mu
- Global Electrophilicity Index: omega = mu^2 / (2 * eta)

Based on Conceptual Density Functional Theory (Parr, Pearson, Fukui).
"""

import csv
import os

def compute_fmo_metrics(input_path, output_path):
    with open(input_path, "r", newline="") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        fieldnames = reader.fieldnames + [
            "chemical_hardness_eta_eV",
            "chemical_potential_mu_eV",
            "electronegativity_chi_eV",
            "electrophilicity_omega_eV"
        ]

    for r in rows:
        homo = float(r["homo_eV"])
        lumo = float(r["lumo_eV"])
        gap = lumo - homo
        eta = gap / 2.0
        mu = (homo + lumo) / 2.0
        chi = -mu
        omega = (mu ** 2) / (2.0 * eta) if eta != 0 else 0.0

        r["chemical_hardness_eta_eV"] = f"{eta:.3f}"
        r["chemical_potential_mu_eV"] = f"{mu:.3f}"
        r["electronegativity_chi_eV"] = f"{chi:.3f}"
        r["electrophilicity_omega_eV"] = f"{omega:.3f}"

    with open(output_path, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Computed Conceptual DFT parameters saved to: {output_path}")

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    qm9_csv = os.path.join(data_dir, "qm9_fmo_benchmark.csv")
    out_csv = os.path.join(data_dir, "qm9_fmo_calculated.csv")
    if os.path.exists(qm9_csv):
        compute_fmo_metrics(qm9_csv, out_csv)
    else:
        print(f"[-] Input file not found: {qm9_csv}")

if __name__ == "__main__":
    main()
