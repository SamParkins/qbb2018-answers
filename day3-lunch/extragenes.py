#!/usr/bin/env python3

#other types of genes present and their number

import sys
f = open( sys.argv[1] )
count = 0
gene_type_unique = {}


for i, line in enumerate( f ):
    if "gene" in line:
        if line.startswith("#!"):
            continue
        fields = line.rstrip("\r\n").split()
        if "gene" in fields[2]:
            for i,val  in enumerate( fields ):
                if val == "gene_biotype":
                    gene_type = (fields[i + 1])
                    if gene_type in gene_type_unique:
                        gene_type_unique[gene_type] += 1
                    else:
                        gene_type_unique[gene_type] = 1
                        
for name, value in gene_type_unique.items():
    print(name, value)
                
            