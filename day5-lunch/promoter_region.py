#!/usr/bin/env python3
"""
usage: ./promoter_region.py <ctab>

estimate promoter region for transcripts in a file

"""



ctab = open(sys.argv[1])

for line in ctab:
    if line.startswith("t"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "+":
        start = int(fields[3]) - 500
        if start < 0:
            start = 0
        end = fields[3]
        print(fields[1] + "\t" + str(start) + "\t" + str(end) + "\t" + fields[5])
    else:
        start =int(fields[4]) + 500
        end = fields[4]
    
        print(fields[1] + "\t" + str(end) + "\t" + str(start) + "\t" + fields[5])
    


    


