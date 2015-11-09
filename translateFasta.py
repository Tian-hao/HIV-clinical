#!/usr/bin/env python
import os
import sys
import string
import glob
from Bio import SeqIO
from Bio.Seq import Seq

def translation(seq):
  dnamap = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"_", "TAG":"_",
    "TGT":"C", "TGC":"C", "TGA":"_", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G", "XXX":"X"}
  pep = []
  i = 0
  seq = str(seq).translate(None,"-")
  while i < len(seq):
    codon = seq[i:i+3]
    if 'N' in codon:
      aa = 'X'
    elif len(codon) != 3:
      aa = 'X'
    else:
      aa = dnamap[codon]
    if aa == '_':
      break
    pep.append(aa)
    i = i + 3
  pep = ''.join(pep)
  return pep

infiles = sorted(glob.glob('../haploPredict/pilot2/*.fas'))
for infile in infiles:
  outfile = infile.rsplit('.fas')[0]+'.pep'
  outlist = []
  inhandle = open(infile,'r')
  outhandle = open(outfile,'w')
  for record in SeqIO.parse(inhandle,"fasta"):
    record.seq = Seq(translation(record.seq))
    outlist.append(record)
  SeqIO.write(outlist,outhandle,'fasta')
