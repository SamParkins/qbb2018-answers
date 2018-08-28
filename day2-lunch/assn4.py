#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
count = 0

for i, line in enumerate( f ):
    if line.startswith("@"):
        pass
    else:
        #print(line)
        print(line.rstrip("\r\n").split("\t")[2])       
   # elif line.rstrip("\r\n").split("\t")
        #column16
        #if "NH:i:1" in line:
        count = count + 1
        if count > 10:
            break
                 
    
print(count)