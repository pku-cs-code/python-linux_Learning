#!/bin/bash
for ip in `cat /server/scripts/iplist`
  do 
     echo "$ip----------"
     scp -r -p $1 $ip:$2
done
