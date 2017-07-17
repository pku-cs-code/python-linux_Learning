#!/bin/bash
#PORT=` netstat -lnt|grep 3306|awk -F '[ :]+' '{print $5}'`
mysqlProcessNum=` ps -ef|grep mysqld |grep -v grep|wc -l`
PORT=` netstat -lnt|grep 3306|wc -l`
#if [ $PORT -eq 1 -a $mysqlProcessNum -eq 2 ];then
if [ $PORT -eq 1 ]&&[ $mysqlProcessNum -eq 2 ];then
    echo "db is running"
   else
     /etc/init.d/mysqld start

fi

