#!/bin/bash
sum=0
while read line
do
   size=`echo $line| awk '{print $10}'`
   [ "$size" == "-" ]  &&continue
   ((sum=sum+$size))
done<access.log
[ -n "$sum" ]&& echo "$sum"
