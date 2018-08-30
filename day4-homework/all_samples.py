#!/usr/bin/env python3

"""
usage: ./all_samples.py <gene_name> <samples.csv> <ctab_dir>
Create a single file all.csv that contains the FPKMs from all 16 samples
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt



fpkm_dict = {}
df = pd.read_csv(sys.argv[1])

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab", )
    ctab_df = pd.read_table(filename, index_col="t_name").loc[:,"FPKM"]
    fpkm_dict[str(sex)+str(stage)] = ctab_df

fpkms_all = pd.DataFrame(fpkm_dict)
fpkms_all.to_csv(sys.stdout)
   