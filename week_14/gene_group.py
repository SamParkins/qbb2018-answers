#!/usr/bin/env python3
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import scanpy.api as sc
import matplotlib
matplotlib.use("Agg")

sc.settings.autoshow = False

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
#to filter the data

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.pp.neighbors(adata, n_neighbors=15)
sc.tl.louvain(adata, resolution=None)

sc.tl.rank_genes_groups(adata, groupby = "louvain", use_raw=True, groups="all", reference="rest", n_genes=100, rankby_abs=False, key_added=None, copy=False, method="logreg", corr_method="benjamini-hochberg")
sc.pl.rank_genes_groups(adata, color = "louvain", save = ("gene_groups_logreg"))