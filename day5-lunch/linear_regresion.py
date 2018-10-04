#!/usr/bin/env python3
"""
usage: ./linear_regression.py <ctab>.......<ctabn>

perform linear regression on five marks

"""
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os

all_means = {}

histone_1 = sys.argv[1].split(os.sep)[-1]
mean_1 = pd.read_csv(sys.argv[1], sep = "\t", index_col=0).iloc[:, 4]

histone_2 = sys.argv[2].split(os.sep)[-1]
mean_2 = pd.read_csv(sys.argv[2], sep = "\t", index_col=0).iloc[:, 4]

histone_3 = sys.argv[3].split(os.sep)[-1]
mean_3 = pd.read_csv(sys.argv[3], sep = "\t", index_col=0).iloc[:, 4]

histone_4 = sys.argv[4].split(os.sep)[-1]
mean_4 = pd.read_csv(sys.argv[4], sep = "\t", index_col=0).iloc[:, 4]

histone_5 = sys.argv[5].split(os.sep)[-1]
mean_5 = pd.read_csv(sys.argv[5], sep = "\t", index_col=0).iloc[:, 4]

fpkms_s = sys.argv[6].split(os.sep)[-1]

fpkm = pd.read_csv(sys.argv[6], sep = "\t", index_col="t_name").loc[:, "FPKM"]

all_means = {histone_1 : mean_1, histone_2 : mean_2, histone_3 : mean_3, histone_4 : mean_4, histone_5 : mean_5, 'fpkm' : fpkm}

all_means_df = pd.DataFrame(all_means)



all_means_df.columns = ["H3K27ac","H3K27me3","H3k4me1","H3K4me3","H3k9ac","fpkm_s"]
#y = all_means_df.loc[:, fpkms_s]
#x = all_means_df.loc[:, [histone_1,histone_2,histone_3,histone_4,histone_5]]
print(all_means_df.columns)
model = smf.ols(formula='fpkm_s ~ H3K27ac + H3K27me3 + H3k4me1 + H3K4me3 + H3k9ac', data=all_means_df)

results = model.fit()
print(results.summary())

