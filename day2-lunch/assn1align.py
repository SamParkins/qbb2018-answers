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
        count = count + 1
print(count)

