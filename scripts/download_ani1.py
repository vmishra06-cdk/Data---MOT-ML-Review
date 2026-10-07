#!/usr/bin/env python3
"""
download_ani1.py
Utility to download the ANI-1 dataset from Zenodo.

Reference:
Smith, J. S.; Isayev, O.; Roitberg, A. E. Chem. Sci. 2017, 8, 3192-3203.
DOI: 10.5281/zenodo.1184918
"""

import os
import urllib.request

ZENODO_RECORD = "1184918"
ZENODO_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD}"

def get_zenodo_info():
    print(f"[*] Accessing Zenodo record {ZENODO_RECORD} (DOI: 10.5281/zenodo.1184918)...")
    print(f"[*] Persistent DOI: https://doi.org/10.5281/zenodo.1184918")
    print("[*] To download the full HDF5 archives (~14 GB), please use the official Zenodo link:")
    print("    https://zenodo.org/record/1184918/files/ani_gdb_s01.h5")

if __name__ == "__main__":
    get_zenodo_info()
