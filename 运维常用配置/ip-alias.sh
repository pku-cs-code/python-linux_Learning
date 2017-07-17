#!/bin/bash
for((i=1;i<=14;i++))
do
  if [ $i -eq 10 ];then
    continue
  fi
    ifconfig eth0:$i 192.168.32.$i netmask 255.255.240.0 up
done
