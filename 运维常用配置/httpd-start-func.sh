#!/bin/bash
. /etc/init.d/functions
httpd=" /usr/sbin/apachectl "
start(){
   $httpd start >/dev/null 2>&1
   [ $? -eq 0 ] &&action "httpd is started." /bin/true ||\
   action "httpd is started." /bin/false
}

stop(){
  $httpd stop >/dev/null 2>&1
   [ $? -eq 0 ] &&action "httpd is stopped." /bin/true ||\
   action "httpd is stopped." /bin/false
}

case "$1" in
start)
  start
;;
stop)
  stop
;;
restart)
 stop
 sleep 2
 start
;;
*)
  echo "Usage:$0 {start|stop|restart}"
exit
;;
esac
