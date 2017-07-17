#!/bin/bash
#function: check if the system optimization is done
#author:zhangcai
#date:2017-05-26
#version:0.1
export PATH=$PATH:/bin:/sbin/:/usr/bin
export LANG="zh_CN.GB18030"

#require root to run this script
if [[ "$(whoami)" != "root" ]];then
echo "Please rum this script as root." >&2
exit 1
fi

#Source function libarary
. /etc/init.d/functions

if [ `grep 18030 /etc/sysconfig/i18n|wc -l` -eq 1 ];then
  action "/etc/sysconfig/i18n"  /bin/true
 else 
  action "/etc/sysconfig/i18n" /bin/false

fi
  
export LANG=en
if [ `chkconfig --list|grep 3:on|egrep "crond|network|syslog|sshd"|wc -l` -eq 4 ]
  then
    action "sys service init"  /bin/true
  else
    action "sys service init" /bin/false
fi

if [ `grep 65535 /etc/security/limits.conf|wc -l` -eq 1 ]
  then
   action "/etc/security/limits.conf" /bin/true
  else
   action "/etc/security/limits.conf" /bin/false
fi
