#!/bin/bash
#for num in 5 4 3 2 1 
#for num in 192.168.31.{5..1} 
#for num in  `seq -s " " 5 -1 -10`
#for num in  `ls -F|grep /` #print directory
for filename in `ls *.LOG`
do
 mv $filename `echo $filename|cut -d . -f1`.log
done

