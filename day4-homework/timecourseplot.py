#!/usr/bin/env python3

"""
usage: ./03-timecourse.py <t_name> <samples.csv> <ctab_dir>
create a timecourse for a given transcript FBtr0331261 for females and males
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt



def genderfilter_s(gender):
    df = pd.read_csv(sys.argv[2])
    #we do soi to subset
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]
    stages = []
    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab", )
        ctab_df = pd.read_table(filename, index_col="t_name")

        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages.append(stage)
    return fpkms, stages
    

def genderfilter_r(gender):
    df = pd.read_csv(sys.argv[4])
    #we do soi to subset
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]
    stages2 = []
    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab", )
        ctab_df = pd.read_table(filename, index_col="t_name")

        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages2.append(stage)
    return fpkms, stages2    

fpkms_f,stages = genderfilter_s("female")
fpkms_m,stages = genderfilter_s("male")

fpkms_r_f,stages2 = genderfilter_r("female")
fpkms_r_m,stages2 = genderfilter_r("male")



fig, ax = plt.subplots()
ax.plot(fpkms_f, label="female", c="red")
ax.plot(fpkms_m, label="male", c="blue")
ax.plot([4,5,6,7], fpkms_r_f, label="female_r", c="green")
ax.plot([4,5,6,7], fpkms_r_m, label="male_r", c="orange")
ax.set_title("Sxl")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abudance (RPKM)")
ax.set_xticklabels(stages, rotation=90)
plt.legend(bbox_to_anchor=(1.07, 0.5), loc=2, borderaxespad=0)
plt.tight_layout()
fig.savefig("timecourseplot.png", bbox_inches='tight')
plt.close(fig)

#./03-timecourse.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/