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

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "louvain", save = ("tsne_plot"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "louvain", save = ("umap_plot"))