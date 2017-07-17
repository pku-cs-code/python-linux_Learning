#!/bin/bash
for ip in `cat /server/scripts/iplist`
  do 
     echo "$ip----------"
     ssh $ip $1
done
