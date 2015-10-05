#!/usr/bin/env python

import os
import sys
import glob
from Bio import SeqIO

bamfiles = sorted(glob.glob('../bams/*sorted.bam'))
cnsfile  = "../cns/cns.fa"
for bamfile in bamfiles:
  fqfile = bamfile.replace('sorted.bam','cns.fq')
  os.system('samtools mpileup -uf ../ref/ref.fa '+bamfile+' | bcftools call -c | vcfutils.pl vcf2fq > '+fqfile)
outfile = open(cnsfile,'w')
fqfiles = sorted(glob.glob('../bams/*cns.fq'))
for cnsreadf in fqfiles:
  infile = open(cnsreadf,'r')
  for record in SeqIO.parse(infile,"fastq"):
    record.id = cnsreadf
    SeqIO.write(record, outfile, "fasta")
  infile.close()
outfile.close()
