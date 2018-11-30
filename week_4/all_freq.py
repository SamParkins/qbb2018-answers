#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

# Usage: week3plot.py identifying variants and generating a multi panel plot
# ./week3plot.py file.vcf snpEff_genes.txt


data_file = open(sys.argv[1])
allele_freq = []


for i in data_file:
    if i.startswith("#"):
        continue
    else:
        fields = i.rstrip("\r\n").split("\t")
        info = fields[7]
        allele = info.split("=")[1]
        allele_n = allele.split(",")[0]
        allele_freq.append(float(allele_n))
        


fig, ax = plt.subplots()
plt.hist(allele_freq, bins=2000)
ax.set(title="variant allele frequency", xlabel="frequency", ylabel="variants")
plt.tight_layout()
fig.savefig("allele_freq.png")
plt.close(fig)