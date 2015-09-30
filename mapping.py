#!/usr/bin/env python
import os
import sys
import glob
import string

refseq  = '../ref/ref.fa'
fqfiles = ['../split/G1P1T1_R1.fq']
fqfiles = sorted(fqfiles)

for fqfile1 in fqfiles:
  fqfile2 = fqfile1.replace('_R1','_R2')
  fqfile  = fqfile1.rsplit('_')[0].rsplit('split/')[1]
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile1+" > ../tmp/"+fqfile1+".sai")
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile2+" > ../tmp/"+fqfile2+".sai")
  os.system("bwa sampe "+refseq+" ../tmp/"+fqfile1+".sai ../tmp/"+fqfile2+".sai "+fqfile1+" "+fqfile2+" > ../tmp/"+fqfile+".sam")
  os.system("samtools view -bS ../tmp/"+fqfile+".sam > ../tmp/"+fqfile+".bam")
  os.system("bamtools convert -format json -in ../tmp/"+fqfile+".bam -out ../json/"+fqfile+".json")

