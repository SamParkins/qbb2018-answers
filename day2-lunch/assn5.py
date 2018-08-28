#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
count = 0
mapq = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        pass
    else:
        #print(line)
        #print(line.rstrip("\r\n").split("\t")[4])       
   # elif line.rstrip("\r\n").split("\t")
        #if "NH:i:1" in line:
        count = count + 1
        mapq = mapq + int(line.rstrip("\r\n").split("\t")[4])
        average = mapq / count
        
        #if count > 10:
        #    break
                 
    
print("MAPQaverage " +str(average))