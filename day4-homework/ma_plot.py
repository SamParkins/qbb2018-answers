#!/usr/bin/env python3

"""
usage: ./ma_plot.py <ctab_file>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm1 = df1.loc[:, "FPKM"]
fpkm2 = df2.loc[:, "FPKM"]

m = np.log2(fpkm1 + 1) - np.log2(fpkm2 + 1)
a = 0.5*(np.log2(fpkm1 + 1) + np.log2(fpkm2 + 1))

# bestfit = np.polyfit(fpkm1_log, fpkm2_log, 1)
# #print(bestfit)
#
#
#
fig, ax = plt.subplots()
ax.scatter(a, m, alpha=0.05)
ax.set_xlabel("Average of Ratio of SRR072893 vs SRR072915")
ax.set_ylabel("Ratio of SRR072893 vs SRR072915 ")
ax.set_title("MAplot")
#
# x = np.linspace(0,8)
# y = np.poly1d(bestfit)
# plt.plot(x, y(x), 'k')
#
fig.savefig("maplot1.png")
plt.close(fig)