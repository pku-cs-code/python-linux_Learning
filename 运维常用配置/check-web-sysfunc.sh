#!/bin/bash
[ -f /etc/init.d/functions ]&& . /etc/init.d/functions ||exit 1
HttpCode=`curl -I -s http://192.168.31.60 |head -1|cut -d  " " -f2`
#curl -I -s http://192.168.31.60 |sed -n '1p'|grep 200
# curl -I -s http://192.168.31.60 |head -1|grep 200
if [ "$HttpCode" = "200" ];then
   action "httpd is running" /bin/true
   else
   action "httpd is not running." /bin/false
    sleep 1
   /etc/init.d/httpd start
fi
