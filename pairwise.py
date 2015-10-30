#!/usr/bin/env python 
import os
import sys
import glob
import string
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

reffile = sys.argv[1]
canfile = sys.argv[2]
refhandle = open(reffile,'r')
canhandle = open(canfile,'r')
for record in SeqIO.parse(refhandle,'fasta'):
  refseq = str(record.seq)
for record in SeqIO.parse(canhandle,'fasta'):
  canseq = str(record.seq)
align = pairwise2.align.localms(refseq,canseq,2,-1,-5,-.001)
print format_alignment(*align[0])
