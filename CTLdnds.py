#!/usr/bin/env python
#caluclate fitness of ctlescape mutations
#output format:
#patient/HLA/epitope_sequence/epitope_position/escape_mutation/freq/fitness/translated?/
#011516: adapt to extract dNdS input.
#coupled with sampling.py
import os
import sys
import string
from Bio import SeqIO

def readepitope(infile):
  epidict = {}
  inhandle = open(infile,'r')
  for line in inhandle:
    line = line.rstrip().rsplit('\t')
    epidict[line[2]] = line[0]+'_'+line[1]
  inhandle.close()
  return epidict

def readfitness(infile):
  fitdict = {}
  inhandle = open(infile,'rU')
  for line in inhandle:
    line = line.rstrip().rsplit(',')
    fitdict[line[0]] = line[1]
  inhandle.close()
  return fitdict

def readhaplos(infile,infas,pt,HLA,epitope):
  epilist = []
  pos = int(epitope.rsplit('_')[1])
  oldseq = epitope.rsplit('_')[0]
  length = len(oldseq)
  inhandle = open(infile,'r')
  fashandle = SeqIO.parse(open(infas,'r'),'fasta')
  for haplo in SeqIO.parse(inhandle,'fasta'):
    nucrec = fashandle.next()
    sample = haplo.id.rsplit('_')[0]
    if (pt not in sample): continue
    freq = haplo.id.rsplit('_')[2]
    seq = str(haplo.seq)
    nucseq = str(nucrec.seq)
    nucseq = nucseq[(pos-1)*3:(pos-1+length)*3]
    newseq = seq[pos-1:pos+length-1]
    newseq = newseq.replace('_','%')
    if '_' in seq[0:pos]: translated = 'no'
    else: translated = 'yes'
    epi = oldseq+'_'+newseq+'_'+str(pos)+'_'+freq+'_'+translated+'_'+HLA+'_'+sample+'_'+nucseq
    epilist.append(epi)
  inhandle.close()
  return epilist

def reformfitdict(fitdict):
  newfitdict = {}
  for mut in fitdict.keys():
    pos = mut[1:-1]
    old = mut[0]
    new = mut[-1]
    if pos not in newfitdict.keys(): newfitdict[pos] = {}
    newfitdict[pos][old] = 1
    newfitdict[pos][new] = fitdict[mut]
  return newfitdict

def writefile(outfile,haplo,fitdict):
  haplo = haplo.rsplit('_')
  oldseq = haplo[0]
  newseq = haplo[1]
  pos = haplo[2]
  freq = haplo[3]
  translated = haplo[4]
  HLA = haplo[5]
  sample = haplo[6]
  nucseq = haplo[7]
  newfitdict = reformfitdict(fitdict)
  #for i in range(0,len(newseq)):
   # if oldseq[i] != newseq[i]:
      #print haplo
#  index = str(int(pos)+i)
#  escape = oldseq[i]+str(index)+newseq[i]
  #if index in newfitdict.keys():
   #     if oldseq[i] in newfitdict[index].keys() and newseq[i] in newfitdict[index].keys():
    #      fitness = float(newfitdict[index][newseq[i]]) / float(newfitdict[index][oldseq[i]])
#	else: fitness = 'unknown'
 #     else: fitness = 'unknown'
   #   fitness = str(fitness)
  fitness = 'NA'
  temp = sample+'\t'+HLA+'\t'+oldseq+'\t'+freq+'\t'+nucseq
  outfile.write(temp+'\n')

def meanfitness(infile):
  ptfit = {}
  ptcount = {}
  for line in infile:
    if 'patient' in line: continue
    line = line.rstrip().rsplit('\t')
    pt = line[0]
    freq = float(line[5])
    fitness = line[6]
    if fitness == 'unknown': continue
    fitness = float(fitness)
    if pt not in ptfit.keys():
      ptfit[pt] = fitness**freq
    else:
      ptfit[pt] *= (fitness**freq)
    if pt not in ptcount.keys():
      ptcount[pt] = freq
    else: 
      ptcount[pt] += freq
  for pt in ptfit.keys():
    ptfit[pt] = ptfit[pt]**(1/float(ptcount[pt]))
  print ptfit


path2work = '../freq/ctl/'
epitopedict = readepitope(path2work+'ctl.txt')
#dict: epitopeseq_pos:patient_HLA
fitnessdict = readfitness(path2work+'gagfitness.csv')
#dict: mutation:fitness
outfile = open(path2work+'epitopeextraction','w')
outfile.write('patient\tHLA\tepitope_sequence\tfreq\tnucseq\n')
for epitope in epitopedict.keys():
  patient = epitopedict[epitope].rsplit('_')[0]
  HLA = epitopedict[epitope].rsplit('_')[1]
  epitopehaplos = readhaplos(path2work+'all.pep',path2work+'all.fas',patient,HLA,epitope)
  #list: epitopeseqold_epitopeseqnew_pos_freq_tranlated_HLA_sample
  for haplo in epitopehaplos:
    writefile(outfile,haplo,fitnessdict)
outfile.close()
#infile = open(path2work+'epitopefitness.txt','r')
#meanfitness(infile)
