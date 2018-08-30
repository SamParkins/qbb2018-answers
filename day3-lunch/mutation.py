#!/usr/bin/env python3

#distance from mutation

import sys
f = open( sys.argv[1] )

current_best_distance = 100000000000000000
current_best_gene = 'gene name'

find_chr = '3R'
find_pos = 21378950
for i, line in enumerate( f ):
    if "gene" in line and "protein_coding" in line:
        fields = line.rstrip("\r\n").split()
        #print(fields)
        if "gene" in fields[2] and "3R" in fields[0]:
            gene_start = int(fields[3])
            gene_end = int(fields[4])
            my_dist = 0
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end

            if my_dist < current_best_distance:
                current_best_distance = my_dist
                current_best_gene = fields[13]
print(current_best_gene, current_best_distance)

f.seek(0)
#count = 0
current_best_distance = 100000000000000000 
        
for i, line in enumerate( f ):
    if "gene" in line:
        if line.startswith("#!"):
            continue
        fields = line.rstrip("\r\n").split()
        if "gene" in fields[2]:
            for i,val  in enumerate( fields ):
                if val == "gene_biotype":
                    gene_type = (fields[i + 1])
            gene_start = int(fields[3])
            gene_end = int(fields[4])
            my_dist = 10000000000000000
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
                #print(my_dist)
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                #print(my_dist)

            if my_dist < current_best_distance:
                current_best_distance = my_dist
                current_best_gene = fields[13]
print(current_best_gene, current_best_distance)





