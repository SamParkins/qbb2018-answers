#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
from scipy.spatial.distance import pdist
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq

data = []


for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split()
    poly = fields[2]
    cfu = fields[1]
    data.append([cfu, poly])
#print(data)
centroids,_ = kmeans(data,7)
idx,_ = vq(data,centroids)

plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()

# fig= plt.figure(figsize=(25, 10))
# dn = dendrogram(z)
# plt.tight_layout()
# fig.savefig("dendrogram.png")
# plt.close(fig)