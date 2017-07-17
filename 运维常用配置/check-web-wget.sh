#!/bin/bash
wget -T 10 -q  --spider http://192.168.31.60 >/dev/null 2>&1
#curl -s http://192.168.31.60 >/dev/null 2>&1
if [ $? -eq 0 ];then
   echo "httpd is running"
   else
   echo "httpd is not running."
   /etc/init.d/httpd start
fi
