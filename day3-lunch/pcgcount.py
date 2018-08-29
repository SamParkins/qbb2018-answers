#!/usr/bin/env python3

#count the number of protien coding genes

import sys
f = open( sys.argv[1] )
count = 0

for i, line in enumerate( f ):
    if "gene" in line and "protein_coding" in line:
        fields = line.rstrip("\r\n").split()
        #print(fields)
        if "gene" in fields[2]:
            count = count + 1
print(count)
            
        