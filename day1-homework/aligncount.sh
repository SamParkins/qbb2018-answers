#!/bin/bash


grep -v 2110000 | cut -f 3 | head -n 100000 | sort | uniq -c


