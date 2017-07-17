#!/bin/bash
if [ $# -ne 1 ];then
echo "Usage:sh $0 {up|down}"
exit
fi

case "$1" in 
"up")
for((i=1;i<=14;i++))
do
  if [ $i -eq 10 ];then
    continue;
  fi
    ifconfig eth0:$i 192.168.32.$i netmask 255.255.240.0 up
done
;;
"down")
for((i=1;i<=14;i++))
do
  if [ $i -eq 10 ];then
    continue;
  fi
    ifconfig eth0:$i 192.168.32.$i netmask 255.255.240.0 down
done
;;
*)
 echo "Usage:sh $0 {up|down}"
  exit;
;;
esac
#exit $RET
exit
