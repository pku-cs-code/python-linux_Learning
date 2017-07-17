#!/bin/bash
filepath="/server/scripts"
if [ -e "$filepath/if3.sh" ]
   then
   echo "$filepath/if3.sh exists."
fi

if [ ! -e "$filepath/if3.sh" ]
   then
    [ ! -d $filepath ] &&mkdir -p $filepath 
    [ -d $filepath ]&&{
          cd $filepath
          touch if3.sh
          echo "if3.sh is created."
}
fi
#[ ! -d /server/backup ]&&mkdir -p /server/backup/
#mysqldump -uroot -p233 -A -B > /server/backup/a.sql
#[ ! -f /server/backip/a.sql ]&&mail -s "bak failed."  afdj@qq.com
