#!/usr/bin/env python
import os
import sys
import csv
from math import log

def parsectl(ctllist):
  rglist = []
  for ctl in ctllist:
    poslist = range(int(ctl[1]),int(ctl[1])+len(ctl[0]))
    for pos in poslist:
      if pos not in rglist: rglist.append(pos)
  return rglist

def findepitope(ctllist,mut):
  epilist = []
  mutpos = int(mut[1:-1])
  for ctl in ctllist:
    ctlrange = range(int(ctl[1]),int(ctl[1])+len(ctl[0]))
    if mutpos in ctlrange:
      spos = mutpos - int(ctl[1])
      newepi = ctl[0][:spos]+mut[-1]+ctl[0][spos+1:]
      epilist.append([ctl[2],newepi])
  return epilist

def calcbinding(epi):
  with open('freq/ctl/tmp.fa','w') as tmpfile:
    tmpfile.write('>tmpppp\n'+epi[1])
  os.system('grep \''+epi[0]+'\' /Users/Tian-hao/Documents/Tools/netMHC-4.0/Darwin_x86_64/data/allelelist > freq/ctl/tmp')
  with open('freq/ctl/tmp','r') as tmpfile:
    hla = tmpfile.readline().rstrip().rsplit('\t')[0]
  os.system('netMHC -a '+hla+' -f freq/ctl/tmp.fa > freq/ctl/netout')
  with open('freq/ctl/netout','r') as netoutfile:
    for line in netoutfile:
      if 'tmpppp' in line:
        record = line.rstrip().rsplit()
	affinity = record[13]
	return affinity

ctllist = []
with open('background/OptiCTL.csv','rU') as ctlfile:
  ctlreader = csv.reader(ctlfile)
  for ctl in ctlreader:
    ctllist.append(ctl)
ctlregion = parsectl(ctllist)
datalist = []
with open('background/RFvisual_gag.txt','r') as fitnessfile:
  fitnessfile.readline()
  for line in fitnessfile:
    line = line.rstrip().rsplit('\t')
    if int(line[4][1:-1]) in ctlregion:
      epitopelist = findepitope(ctllist,line[4])
      for epi in epitopelist:
        affinity = calcbinding(epi)
        if affinity is not None: datalist.append([line[0],line[14],affinity])
#print datalist
with open('freq/ctl/bindingcor','w') as outfile:
  for point in datalist:
    outfile.write('\t'.join(point)+'\n')
