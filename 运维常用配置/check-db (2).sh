#!/bin/bash
#PORT=` netstat -lnt|grep 3306|awk -F '[ :]+' '{print $5}'`
MYSQL=/etc/init.d/mysqld
LogPath=/tmp/mysql.log
mysqlProcessNum=` ps -ef|grep mysqld |grep -v grep|wc -l`
PORT=` netstat -lnt|grep 3306|wc -l`
#if [ $PORT -eq 1 -a $mysqlProcessNum -eq 2 ];then
if [ $PORT -eq 1 ]&&[ $mysqlProcessNum -eq 2 ];then
    echo "db is running"
   else
    $MYSQL  start > $LogPath
     sleep 10
     mysqlProcessNum=` ps -ef|grep mysqld |grep -v grep|wc -l`
     PORT=` netstat -lnt|grep 3306|wc -l`
     if [ $PORT -ne 1 ]&&[ $mysqlProcessNum -ne 2 ];then
     while true
      do
        killall -9  mysqld >/dev/null 2>&1
        [ $? -ne 0 ] && break
        sleep 1
     done     
     $MYSQL start >>$LogPath && status="mysql is succesfully started."||status="failure"
    mail -s "mysql started startup status is $status" 414220021@qq.com <$LogPath
    fi
fi

