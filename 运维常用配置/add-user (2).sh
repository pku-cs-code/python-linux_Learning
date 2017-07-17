#!/bin/bash
. /etc/init.d/functions
>/mnt/user.txt
for n in `seq -w 10`
do
#passwd must be defined first
 passwd=` echo $(date +%t%N)$RANDOM|md5sum|cut -c 2-9`
 useradd oldboy-$n >/dev/null 2>&1 &&user_status=$? 
 echo "$passwd"|passwd --stdin oldboy-$n >/dev/null  &&pass_status=$?

if [ $user_status -eq 0 -a $pass_status -eq 0 ];then
 action "adduser oldboy-$n" /bin/true
 echo -e "user:\toldboy-$n pass:\t ${passwd}">>/mnt/user.txt
else
 action "adduser oldboy-$n" /bin/false
 echo -e "user:\toldboy-$n pass:\t ${passwd}">>/mnt/failuser.txt
fi
done
