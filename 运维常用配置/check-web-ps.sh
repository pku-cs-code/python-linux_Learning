#!/bin/bash
HttpProcessNum=`ps -ef|grep http|grep -v grep|wc -l`
if [ $HttpProcessNum -gt 4 ];then
   echo "httpd is running"
   else
   echo "httpd is not running."
   /etc/init.d/httpd start
fi
