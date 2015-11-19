#!/usr/bin/env python
import os
import sys
import string

fitfile = open('RFvisual_gag.txt','r')
outfile = open('fitness.txt','w')
fitdict = {}
mutlist = []
for line in fitfile.xreadlines():
  line = line.rstrip().rsplit('\t')
  if line[0] == 'ref': continue
  name = line[4]
  freq = line[16]
  if name in fitdict.keys():
    fitdict[name].append(freq)
  else:
    fitdict[name] = [freq]
    mutlist.append(name)
for name in mutlist:
  mean = 0
  for freq in fitdict[name]:
    mean += float(freq)
  mean /= len(fitdict[name])
  outfile.write(name+'\t'+str(mean)+'\n')
fitfile.close()
outfile.close()

