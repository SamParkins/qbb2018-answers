#!/usr/bin/env python3

"""
usage: ./fpkm_merge.py <threshold> <ctab_file1> <ctab_file2>....<ctab_filen>

create csv file with fpkms from 2 or more samples

"""

import sys
import os
import pandas as pd
import numpy as np

list_of_files = sys.argv[2:len(sys.argv)]
fpkm_dict = {}
threshold = float(sys.argv[1])

#gives me my list of fkpkms from all the files as a dataframe
for file in list_of_files:
    name = file.split( os.sep )[-2] 
    fpkm = pd.read_csv(file, sep="\t", index_col="t_name").loc[:,"FPKM"]
    fpkm_dict[name] = fpkm
fpkms_all = pd.DataFrame(fpkm_dict)
#print(fpkms_all)

#sum across the rows
sum_c = fpkms_all.sum(axis=1)
fpkms_sum = fpkms_all.assign(sum=sum_c)
sum_over_threshold = fpkms_sum.loc[:,"sum"] > threshold

print(fpkms_sum.loc[sum_over_threshold,:])

#print(fpkms_sum)

