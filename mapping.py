#!/usr/bin/env python
import os
import sys
import glob
import string

def FormatMut(JsonMut, Seq, startsite, Qual):
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
    if int(Qual[MutPosarray[i]-1]) < 30:
      continue
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
    return 'WT'
  else:
    return '_'.join(FilterMut)  

def IdentifyMut(jsonfile, output):
  infile  = open(jsonfile,'r')
  outfile = open(output,'w')
  for line in infile.xreadlines():
    line = line.rstrip()
    info = line.rsplit('"')
    position = info[14][1:-1]
    if '["121M"]' in line:
      ID = info[3]
      REF = info[11]
      BARCODE = info[int(info.index('BC'))+2]
      MREF = info[int(info.index('mate'))+4]
      MUT = info[int(info.index('MD'))+2]
      SEQ = info[int(info.index('queryBases'))+2]
      QUAL = info[int(info.index('qualities'))+1].replace(':[','').replace('],', '').rsplit(',')
      if REF == MREF:
        MUT = FormatMut(MUT, SEQ, position, QUAL)
	outfile.write(ID+"\t"+REF+"\t"+BARCODE+"\t"+MUT+"\n")
  infile.close()
  outfile.close() 

refseq  = '../ref/ref.fa'
fqfiles = ['../split/G1P1T1_R1.fq']
fqfiles = sorted(fqfiles)
for fqfile1 in fqfiles:
  fqfile2  = fqfile1.replace('_R1','_R2')
  fqfile   = fqfile1.rsplit('_')[0].rsplit('split/')[1]
  jsonfile = ''.join(["../json/", fqfile, ".json"])
  outfile  = ''.join(["../mut/", fqfile, ".mut"])
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile1+" > ../tmp/"+fqfile1+".sai")
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile2+" > ../tmp/"+fqfile2+".sai")
  os.system("bwa sampe "+refseq+" ../tmp/"+fqfile1+".sai ../tmp/"+fqfile2+".sai "+fqfile1+" "+fqfile2+" > ../tmp/"+fqfile+".sam")
  os.system("samtools view -bS ../tmp/"+fqfile+".sam > ../tmp/"+fqfile+".bam")
  os.system("bamtools convert -format json -in ../tmp/"+fqfile+".bam -out ../json/"+fqfile+".json")
  IdentifyMut(jsonfile,outfile)
