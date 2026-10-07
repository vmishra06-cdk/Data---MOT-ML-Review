#!/usr/bin/env python3
"""
download_full_qm9.py
Automated utility to fetch the complete 133k-molecule QM9 dataset 
from the official Figshare / Materials Cloud archive.

Reference:
Ramakrishnan et al., Scientific Data 1, 140022 (2014).
DOI: 10.6084/m9.figshare.c.978904.v5
"""

import os
import sys
import urllib.request
import tarfile

QM9_FIGSHARE_URL = "https://ndownloader.figshare.com/files/3195389"
TARGET_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "qm9_raw")

def download_qm9(dest_dir=TARGET_DIR):
    os.makedirs(dest_dir, exist_ok=True)
    tar_path = os.path.join(dest_dir, "dsgdb9nsd.xyz.tar.bz2")
    
    print(f"[*] Downloading QM9 dataset from Figshare (DOI: 10.6084/m9.figshare.c.978904.v5)...")
    print(f"[*] Target file: {tar_path}")
    
    try:
        def progress(count, block_size, total_size):
            pct = int(count * block_size * 100 / total_size)
            sys.stdout.write(f"\r--> Progress: {pct}% [{count * block_size / 1e6:.1f} MB / {total_size / 1e6:.1f} MB]")
            sys.stdout.flush()

        urllib.request.urlretrieve(QM9_FIGSHARE_URL, tar_path, reporthook=progress)
        print("\n[+] Download complete. Extracting XYZ files...")
        
        with tarfile.open(tar_path, "r:bz2") as tar:
            tar.extractall(path=dest_dir)
        print(f"[+] Successfully extracted 133,885 molecular geometries to: {dest_dir}")
    except Exception as e:
        print(f"[-] Download error: {e}")
        print("[-] Manual download link: https://doi.org/10.6084/m9.figshare.c.978904.v5")

if __name__ == "__main__":
    download_qm9()
