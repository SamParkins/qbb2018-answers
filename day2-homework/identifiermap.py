#!/usr/bin/env python3

#append AC numbers
#fly_2c is my input file with two columns
#transdata corresponds to my c_tab file
#FBgn_dict is my dictionary allowing me to map the imput file to c_tab

import sys
fly_2c = open( sys.argv[1] )
transdata = open( sys.argv[2])

FBgn_dict = {}
for line in fly_2c:
    fields = line.rstrip("\r\n").split()
    FBgn_dict[fields[0]] = fields[1]
print(fly_2c)

for line_1 in transdata:
    count = 0
    if "FBgn" in line_1:
        fields_1 = line_1.rstrip("\r\n").split()
        #print(fields_1)
        if fields_1[8] in FBgn_dict.keys():
            if count < 100:
                print(FBgn_dict[fields_1[8]], "/t", line_1.rstrip("\r\n"))
                count = count + 1
        else:
            if sys.argv[3] == 'print':
                print('no match', "\t", line_1)
    

