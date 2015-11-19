#!/usr/bin/env python
import os
import sys
import string

hamfile = open('nuc.ham','r')
distable = open('nucheat.tab','w')
quasi = []
for line in hamfile.xreadlines():
  seqA = line.rsplit('\t')[0]
  if seqA not in quasi:
    quasi.append(seqA)
distable.write('name\t')
for quasiname in quasi:
  distable.write(quasiname+'\t')
distable.write('\n')
linecount = 0
hamfile.seek(0)
for line in hamfile.xreadlines():
  line = line.rsplit('\t')
  seqA = line[0]
  seqB = line[1]
  dist = line[2].rstrip()
  linecount += 1
  if linecount % 28 == 1:
    distable.write(seqA+'\t'+dist+'\t')
  elif linecount % 28 == 0:
    distable.write(dist+'\n')
  else:
    distable.write(dist+'\t')
