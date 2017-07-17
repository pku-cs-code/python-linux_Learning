#!/bin/bash
#function
#author
#version

#port=3306
mysql_user="root"
mysql_pwd="123456"
Cmd_Path="/usr/local/mysql/bin"
mysql_sock="/usr/local/mysql/tmp/mysql.sock"
#startup function
function_start_mysql()
{
 if [ ! -e $mysql_sock ];then
# if [ ! -f $mysql_sock ];then  can't use -f
  printf  "Starting MySQL...\n"
  /bin/sh ${Cmd_Path}/mysqld_safe --defaults-file=/etc/my.cnf 2>&1 >/dev/null &
  exit
  else
  printf "already started.\n"
  exit
 fi
}

#stop function
function_stop_mysql()

{

 if [ ! -e $mysql_sock ];then
  printf  "already stopped.\n"
  exit
  else
  printf "Stopping MySQL...\n"
   ${Cmd_Path}/mysqladmin -u ${mysql_user} -p${mysql_pwd} -S $mysql_sock shutdown
 fi

}

#restart function
function_restart_mysql(){
  printf "Restarting mysql...\n"
  function_stop_msyql
  sleep 2
  function_start_mysql
}
 
case $1 in  
start) 
 function_start_mysql
;;
stop)
 function_stop_mysql
;;
restart)
  function_stop_mysql
;;
*)
  printf "Usage: /data/${port}/mysql {start|stop|restart}\n"
;;
esac




