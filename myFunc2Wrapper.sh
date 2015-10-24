#!/bin/bash
# myFunc2FastWrapper.sh
echo $SGE_TASK_ID
./splitbam.py `sed -n ${SGE_TASK_ID}p ~/HIVnc/listtmp.txt`
