#!/bin/bash
size=`awk '{print $10}' $1`
sum=0
for num in $size
do
[ -n "$num" -a "$num" = "${num//[^0-9]/}" ]||continue
((sum=$num+sum))
done
echo "Log.size: $sum  bytes=`echo  $(($sum/1024))`KB"
