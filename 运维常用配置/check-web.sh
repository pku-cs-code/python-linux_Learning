#!/bin/bash
HttpPortNum=`nmap 192.168.31.60 -p 80|grep open|wc -l`
if [ $HttpPortNum -eq 1 ];then
   echo "httpd is running"
   else
   echo "httpd is not running."
   /etc/init.d/httpd start
fi
