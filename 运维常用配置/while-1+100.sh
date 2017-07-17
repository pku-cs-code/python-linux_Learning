#!/bin/bash
i=1
sum=0
while((i<=1000000))
do
  ((sum=sum+i))
   ((i++))
done
#echo "sum=$sum"
[ -n "$sum" ]&&printf "total sum is:$sum\n"
