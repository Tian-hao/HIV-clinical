#!/usr/bin/env python
#automatically run PredictHaplo

import os 
import sys
import glob
import string 

#generate config
listsample = open('listsample.txt','r')
for i in range(0,16):
  os.sys('cp config_sim0 config_sim'+str(i+1))
  samplename = listsample.xreadline().rsplit()
  os.sys('sed \'3s/.*/'+samplename+'/\' config_sim'+str(i+1)+' > config.tmp1')
  os.sys('sed \'5s/.*/ref.fa/\' config.tmp1 > config.tmp2')
  os.sys('sed \'9s:.*:data/'+samplename+'_R1aaaa.sam:\' config.tmp2 > config.tmp3')
  os.sys('sed \'11s/.*/0/\' config.tmp3 > config_sim'+str(i+1))
  os.sys('./PredictHaplo config_sim'+str(i+1))
