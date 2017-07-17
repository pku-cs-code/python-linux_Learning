#!/bin/sh
. /etc/init.d/functions
for ip in `cat iplist`
do
 expect oldboy-2.exp /etc/hosts $ip /etc/hosts >/dev/null 2>&1
 if [ $? -eq 0 ];then
      action "$ip" /bin/true
 else
      action "$ip" /bin/false
 fi
done
