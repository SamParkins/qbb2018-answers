#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math


comp_1 = []
comp_2 = []

for i in open(sys.argv[1]):
    fields = i.rstrip("\r\n").split(" ")
    comp_1x = fields[2]
    comp_2y = fields[3]
    comp_1.append(float(comp_1x))
    comp_2.append(float(comp_2y))

fig, ax = plt.subplots()
plt.scatter(comp_1,comp_2)
plt.ylabel("Genetic Relatedness")
plt.xlabel("Components")
ax.set_title("PCA plot")
plt.tight_layout()
fig.savefig("Week4_PCA.png")
plt.close(fig)
    