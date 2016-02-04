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

ctllist = []
with open('background/OptiCTL.csv','rU') as ctlfile:
  ctlreader = csv.reader(ctlfile)
  for ctl in ctlreader:
    ctllist.append(ctl)
ctlregion = parsectl(ctllist)
#print ctlregion
ctlfitness = []
otherfitness = []
with open('background/RFvisual_gag.txt','r') as fitnessfile:
  fitnessfile.readline()
  for line in fitnessfile:
    line = line.rstrip().rsplit('\t')
    if int(line[4][1:-1]) in ctlregion: ctlfitness.append(float(line[14]))
    else: otherfitness.append(float(line[14]))
#print ctlfitness
#print otherfitness
with open('freq/ctl/ctlfitness','w') as outfile:
  for fit in ctlfitness:
    outfile.write(str(fit)+'\n')
with open('freq/ctl/ctlfitnessno','w') as outfile:
  for fit in otherfitness:
    outfile.write(str(fit)+'\n')

