#!/bin/sh
. /etc/init.d/functions
file="$1"
remote_dir="$2"

if [ $# -ne 2 ];then
   echo "usage:$0 argv1 argv2"
   echo " must have two args"
   exit
fi

for ip in `cat /server/scripts/iplist`
do  
  scp -P 22 -r -p $file oldboy@$ip:~ #>/dev/null 2>&1 
  ssh -t -p 22  oldboy@$ip sudo rsync -avzP ~\/$file $remote_dir # >/dev/null 2>&1
#  if [ $? -eq 0 ];then
#    action "$ip is successful." /bin/true
#  else 
#    action "$ip is failure."  /bin/false
#  fi   
done
