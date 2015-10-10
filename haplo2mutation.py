#!/usr/bin/env python

import os
import sys
import glob
import string
from Bio import SeqIO

samplefiles = glob.glob('../paired/*.pair')
samplefiles = sorted(samplefiles)
reffile     = open('../ref/ref.fa','r')
for ref in SeqIO.parse(reffile,'fasta'):
  refseq  = str(ref.seq)
for sample in samplefiles: 
  mutA = {}
  mutC = {}
  mutG = {}
  mutT = {}
  outfile = sample.replace('/paired/','/freq/')
  outfile = outfile.replace('.pair','.freq')
  handle = open(sample,'r')
  output = open(outfile,'w')
  for line in handle.xreadlines():
    line = line.rsplit('\t')[1]
    mutations = line.rsplit('_')
    for sub in mutations:
      pos = filter(str.isdigit,sub)
      if sub[-1] == 'A':
        if pos in mutA.keys(): mutA[pos] += 1
	else: mutA[pos] = 1
      if sub[-1] == 'C':
        if pos in mutC.keys(): mutC[pos] += 1
	else: mutC[pos] = 1
      if sub[-1] == 'G':
        if pos in mutG.keys(): mutG[pos] += 1
	else: mutG[pos] = 1
      if sub[-1] == 'T':
        if pos in mutT.keys(): mutT[pos] += 1
	else: mutT[pos] = 1
  output.write('index\tA\tC\tG\tT\n')
  for index in range(1,1520):
    wtbase = refseq[index-1]
    index  = str(index)
    if index in mutA.keys(): numA = mutA[index] 
    else: numA = 0
    if index in mutC.keys(): numC = mutC[index] 
    else: numC = 0
    if index in mutG.keys(): numG = mutG[index] 
    else: numG = 0
    if index in mutT.keys(): numT = mutT[index] 
    else: numT = 0
    numA = str(numA); numT = str(numT); numG = str(numG); numC = str(numC)
    if wtbase == 'A': output.write(index+'\t'+'NA'+'\t'+numC+'\t'+numG+'\t'+numT+'\n')
    if wtbase == 'C': output.write(index+'\t'+numA+'\t'+'NA'+'\t'+numG+'\t'+numT+'\n')
    if wtbase == 'G': output.write(index+'\t'+numA+'\t'+numC+'\t'+'NA'+'\t'+numT+'\n')
    if wtbase == 'T': output.write(index+'\t'+numA+'\t'+numC+'\t'+numG+'\t'+'NA'+'\n')
     
