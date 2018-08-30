#!/usr/bin/env python3

"""
usage: ./03-numpy.py <ctab_file>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm1 = df1.loc[:, "FPKM"]
fpkm2 = df2.loc[:, "FPKM"]

fpkm1_log = np.log(fpkm1 + 1)
fpkm2_log = np.log(fpkm2 + 1)

bestfit = np.polyfit(fpkm1_log, fpkm2_log, 1)
#print(bestfit)



fig, ax = plt.subplots()
ax.scatter(fpkm1_log, fpkm2_log, alpha=0.05)
ax.set_xlabel("fpkm1")
ax.set_ylabel("fpkm2")
ax.set_title("fpkm1 vs fpkm2")

x = np.linspace(0,8)
y = np.poly1d(bestfit)
plt.plot(x, y(x), 'k')

fig.savefig("scatterplot1.png")
plt.close(fig)