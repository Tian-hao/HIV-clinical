#!/usr/bin/env python
import os

#os.system('mkdir ../quasiRecomb/')
infile = '../bams/G1P1T1_aass1sorted.sam.bam'
os.system('cd ../quasiRecomb/')
os.system('java -XX:NewRatio=9 -jar ~/Documents/Tools/QuasiRecomb/QuasiRecomb.jar -i '+infile+' -noGaps -quality')

