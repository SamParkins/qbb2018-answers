#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATE=../genomes/BDGP6.Ensembl.81.gtf

for FASTQ in SRR072893  SRR072903 SRR072905  SRR072915
do
	mkdir ${FASTQ}
	fastqc ~/data/rawdata/${FASTQ}.fastq
	hisat2 -x ${GENOME} -U ~/data/rawdata/${FASTQ}.fastq -S ${FASTQ}.sam
	samtools view -b ${FASTQ}/${FASTQ}.sam > ${FASTQ}/${FASTQ}.bam
	samtools sort ${FASTQ}/${FASTQ}.bam > ${FASTQ}/${FASTQ}.sort.bam
	samtools index ${FASTQ}/${FASTQ}.sort.bam
	stringtie ${FASTQ}/${FASTQ}.sort.bam -G ${ANNOTATE} -p 8 -o ${FASTQ}/${FASTQ}.abound.gtf -e -B
done