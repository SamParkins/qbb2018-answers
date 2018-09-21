#!/usr/bin/env python3
"""
usage: ./dotplot.py <lastz_file> 

Making a dotplot of contigs against a reference file

"""


import fasta
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import sys
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os
from statsmodels.stats import weightstats as stest
import math

site = 0 
fig, ax = plt.subplots()
for i in open(sys.argv[1]):
    field = i.split("\t")
    target_start = field[0]
    contig_length = field[1]
    target_end = field[2]
    plt.plot([int(target_start), int(target_end)], [site, site+int(contig_length)])
    site += int(contig_length)
    
ax.set_ylabel("Contigs")
ax.set_xlabel("Reference")
ax.set_title("Position of contigs in relation to reference sequence")
plt.tight_layout()
plt.xlim(0, 100000)
plt.ylim(0, 120000)
fig.savefig("better_vh_dotplot")
plt.close(fig)
    