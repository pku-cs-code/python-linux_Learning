#!/bin/bash
#PORT=` netstat -lnt|grep 3306|awk -F '[ :]+' '{print $5}'`
MYSQL=/etc/init.d/mysqld
LogPath=/tmp/mysql.log
mysql -uroot -p'123456' -S /usr/local/mysql/tmp/mysql.sock -e "select version();" >/dev/null 2>&1
#if [ $PORT -eq 1 -a $mysqlProcessNum -eq 2 ];then
if [ $? -eq 0 ];then
    echo "db is running"
   else
    $MYSQL  start > $LogPath
     sleep 10
     mysql -uroot -p'123456' -S /usr/local/mysql/tmp/mysql.sock -e "select version();" >/dev/null 2>&1
     if [ $? -ne 0 ];then
     while true
      do
        killall -9  mysqld >/dev/null 2>&1
        [ $? -ne 0 ] && break
        sleep 1
     done     
     $MYSQL start >>$LogPath && status="mysql is succesfully started."||status="failure"
    # echo "mysql is while true started."
    mail -s "mysql started startup status is $status" 414220021@qq.com <$LogPath
    fi
fi

