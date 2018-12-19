#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
from scipy.spatial.distance import pdist
import pandas as pd
import seaborn as sns


d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

ax = sns.clustermap(df)
plt.show()
ax.savefig("heatmap_dendrogram.png")
plt.close()


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
new_kmeans = kmeans.predict(df)

plt.figure()
plt.title("K_means_cluster")
plt.scatter(df["CFU"], df['poly'], c=new_kmeans, s=5, cmap='viridis')
plt.ylabel("poly")
plt.xlabel("CFU")
plt.savefig("k_means.png")
plt.close()