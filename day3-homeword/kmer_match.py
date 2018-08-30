#!/usr/bin/env python3

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])

reader = fasta.FASTAReader( target )

kmers = {}
k = int(sys.argv[3])

for t_ident, t_sequence in reader:
    for i in range( 0, len(t_sequence) - k):
        t_kmer = t_sequence[i:i+k]
        if t_kmer not in kmers:
            kmers[t_kmer] = [[t_ident,i]]
        else:
            kmers[t_kmer].append([t_ident,i])
            
reader_q = fasta.FASTAReader(query)

for q_ident, q_sequence in reader_q:
    for i in range( 0, len(q_sequence) - k):
        kmer = q_sequence[i:i+k]
        if kmer in kmers:
            hits_list = kmers[kmer]
            for t_list in hits_list:
                print(t_list[0], t_list[1],i, kmer)


