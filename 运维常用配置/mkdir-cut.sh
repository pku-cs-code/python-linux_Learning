#!/bin/bash
[ ! -e "/oldboy" ]&&mkdir -p /oldboy 
cd /oldboy

for n in `ls oldboy*`
do 
mv $n  linux-`echo $n |cut -d "-" -f2`
done
