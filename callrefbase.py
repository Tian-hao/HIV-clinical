#!/usr/bin/env python
import os
import sys
from Bio import SeqIO

def callrefbase(number): 
  ref = SeqIO.parse('../ref/ref.fa','fasta')
  for refhandle in ref:
    refseq = str(refhandle.seq)
  return refseq[number]

print callrefbase(int(sys.argv[1]))
