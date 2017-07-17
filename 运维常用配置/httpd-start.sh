#!/bin/bash
. /etc/init.d/functions
httpd=" /usr/sbin/apachectl "
case "$1" in
start)
   $httpd start >/dev/null 2>&1
   [ $? -eq 0 ] &&action "httpd is started." /bin/true ||\
   action "httpd is started." /bin/false
;;
stop)
  $httpd stop >/dev/null 2>&1
   [ $? -eq 0 ] &&action "httpd is stopped." /bin/true ||\
   action "httpd is stopped." /bin/false
;;
restart)
     $httpd restart >/dev/null 2>&1
   [ $? -eq 0 ] &&action "httpd is restartedd." /bin/true ||\
   action "httpd is restarted." /bin/false
;;
*)
  echo "Usage:$0 {start|stop|restart}"
exit
;;
esac
