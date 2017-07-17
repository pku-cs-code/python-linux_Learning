#!/bin/bash
#PORT=` netstat -lnt|grep 3306|awk -F '[ :]+' '{print $5}'`
#PORT=` netstat -lnt|grep 3306|wc -l`
mysqlStatus=`mysql -uroot -p'123456' -S /usr/local/mysql/tmp/mysql.sock -e "select version();" >/dev/null 2>&1`
if [ $? -eq 0 ];then
    echo "db is running"
   else
     /etc/init.d/mysqld start

fi

