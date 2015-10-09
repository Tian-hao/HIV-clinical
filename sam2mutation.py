#!/usr/bin/env python

import os
import sys
import glob
import string
from Bio import SeqIO

samfiles = sorted(glob.glob('../errorcorrection/*.sam'))
reffile  = open('../ref/ref.fa','r')
refhandle= SeqIO.parse(reffile,'fasta')
for record in refhandle:
  refseq = record.seq
for samfile in samfiles:
  samname = samfile.rsplit('/errorcorrection/')[1].rsplit('.sam')[0] 
  os.system('samtools view -bS '+samfile+' > ../errorcorrection/'+samname+'.bam')
  os.system("/usr/local/bin/bamtools convert -format json -in ../errorcorrection/"+samname+".bam -out ../json/"+samname+".json")
  infile  = open('../json/'+samname+'.json','r')
  outfile = open('../freq/'+samname+'.freq','w')
  count = {}
  for i in range(0,1520):
    for base in ['A','T','C','G']:
      count[base+str(i)] = 0
  for line in infile.xreadlines():
    line = line.rstrip()
    info = line.rsplit('"')
    startsite = info[14][1:-1]
    if '["113M"]' in line:
      JsonMut = info[int(info.index('MD'))+2]
      Seq = info[int(info.index('queryBases'))+2]
      inpos = 1000
      MutPos = JsonMut.replace('A','_')
      MutPos = MutPos.replace('C','_')
      MutPos = MutPos.replace('T','_')
      MutPos = MutPos.replace('G','_')
      wtbase = JsonMut.replace('1','')
      wtbase = wtbase.replace('2','')
      wtbase = wtbase.replace('3','')
      wtbase = wtbase.replace('4','')
      wtbase = wtbase.replace('5','')
      wtbase = wtbase.replace('6','')
      wtbase = wtbase.replace('7','')
      wtbase = wtbase.replace('8','')
      wtbase = wtbase.replace('9','')
      wtbase = wtbase.replace('0','')
      MutPos = MutPos.rsplit('_')
      MutPosarray = []
      MutIDarray = []
      RefPosarray = []
      FilterMut = []
      RefPos = int(startsite)-1
      Pos = 0
      for i in range(0,len(MutPos)-1):
        RefPos = RefPos + int(MutPos[i]) + 1
        Pos = Pos + int(MutPos[i]) + 1
        RefPosarray.append(RefPos)
        MutPosarray.append(Pos)
      for i in range(0,len(MutPosarray)):
        mutbase = Seq[MutPosarray[i]-1]
        RefPosOut = RefPosarray[i]
        if MutPosarray[i] >= inpos:
          RefPosOut = RefPosOut + 1
        Mut = ''.join([wtbase[i], str(RefPosOut), mutbase])
        MutIDarray.append(Mut)
      for i in MutIDarray:
        if not 'N' in i:
          FilterMut.append(i)
      if len(FilterMut) == 0:
        haplotag =  'WT'
      else:
        haplotag = '_'.join(FilterMut)
      for i in range(1,1520):
        count[refseq[i]+str(i)] += 1
      for mut in FilterMut:
        pos = filter(str.isdigit,mut)
        wtbase = mut.rsplit(pos)[0]
        mutbase = mut.rsplit(pos)[1]
        count[wtbase+str(pos)] -= 1 
        count[mutbase+str(pos)] += 1
  for i in range(1,1520):
      outfile.write(str(i)+'\t'+str(count['A'+str(i)])+'\t'+str(count['T'+str(i)])+'\t'+str(count['C'+str(i)])+'\t'+str(count['G'+str(i)])+'\n')

        
        


