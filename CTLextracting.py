#!/usr/bin/env python
import os
import sys
import glob
import string
from math import log

def readpatient(ptfile):
  pthla = {}
  pthandle = open(ptfile,'r')
  for line in pthandle:
    line = line.rstrip().rsplit('\t')
    pthla[line[0]] = line[1]
  pthandle.close()
  return pthla

def readtarget(ctlfile):
  ctldict = {}
  ctlhandle = open(ctlfile,'rU')
  for line in ctlhandle:
    line = line.rstrip().rsplit(',')
    if line[2] in ctldict.keys():
      ctldict[line[2]] += ('/'+line[0]+'_'+line[1])
    else:
      ctldict[line[2]] = line[0]+'_'+line[1]
  ctlhandle.close()
  return ctldict

def diversity(numlist):
  div = 0
  total = sum(numlist)
  for num in numlist:
    if num == 0: 
      numlist.remove(num)
      continue
    num = float(num)
    div += num/total * log(num/total)
  div = div/log(len(numlist))
  return div

def readfrequency(ctl,ptfile):
  div = 0
  ctl = ctl.rsplit('_')
  ctlpos = int(ctl[1])
  ctlseq = ctl[0]
  ctlend = ctlpos+len(ctlseq)
  pthandle = open(ptfile,'r')
  head = pthandle.readline().rstrip().rsplit('\t')
  aalist = head[1::]
  escape = ''
  for i,line in enumerate(pthandle):
    if i+1 < ctlpos or i+1 >= ctlend: continue
    line = line.rstrip().rsplit('\t')[1::]
    line = map(int,line)
    div += diversity(line)
    cns = line.index(max(line))
    cns = aalist[cns]
    wtpos = i-ctlpos+1
    if cns != ctlseq[wtpos]: escape += (ctlseq[wtpos]+str(i+1)+cns+'_')
  div = div/len(ctlseq)
  #return str(-div)+'_'+escape
  return escape

def writediversity(time,div,outhandle):
  div = div[:-1]
  if time == 'T1':
    outhandle.write(time+':'+div+'\t')
  if time == 'T2':
    outhandle.write(time+':'+div+'\n')

PatientHLA = readpatient('../background/patientctl.txt')
CTLtarget = readtarget('../background/OptiCTL.csv')
outfile = open('../freq/ctl/ctl.txt','w')
for Patient in sorted(PatientHLA.keys()):
  #outfile.write(Patient+'\n')
  HLAlist = list(set(PatientHLA[Patient].rsplit('/')))
  for HLA in HLAlist:
    #outfile.write(HLA+'\n')
    if HLA in CTLtarget.keys():
      Targetlist = CTLtarget[HLA].rsplit('/')
    else:
      Targetlist = []
    for Target in Targetlist:
      outfile.write(Patient+'\t'+HLA+'\t'+Target+'\n')
      Patientfile = '../freq/pepfreq/'+Patient+'T1.freq'
      Diversity = readfrequency(Target,Patientfile)
      #writediversity('T1',Diversity,outfile)
      Patientfile = Patientfile.replace('T1','T2')
      Diversity = readfrequency(Target,Patientfile)
      #writediversity('T2',Diversity,outfile)
  #outfile.write('\n')
outfile.close()
