#!/usr/bin/env python3
"""
usage: ./contig_counter.py <fasta_file> 

Computing number of contigs, minimum/maximum/average contig length, and N50

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

contig_compute = fasta.FASTAReader(open(sys.argv[1]))


contig_list = []


for contig_id, contig in contig_compute:
    length = len(contig)
    contig_list.append(length)
genome_length = sum(contig_list)
contig_count = len(contig_list)


print("Max = " + str(max(contig_list)))
print("Min = " + str(min(contig_list)))
print("Mean = " + str(np.mean(contig_list)))
print("Count = " + str(contig_count))


n50_list = sorted(contig_list)

mid_sum = 0
for contig in n50_list:
    mid_sum += contig
    if mid_sum > (genome_length/2):
        print("N50 = " + str(contig))
        break
 


