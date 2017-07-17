#!/bin/bash
#PORT=` netstat -lnt|grep 3306|awk -F '[ :]+' '{print $5}'`
MYSQL_STARTUP=/etc/init.d/mysqld
MYUSER=root
MYPASS="123456"
MYSOCK="/usr/local/mysql/tmp/mysql.sock"
LogPath=/tmp
Log_FILE=${LogPath}/mysqllogs_`date +%F`.log
MYSQL_PATH=/usr/local/mysql/bin
MYSQL_CMD="$MYSQL_PATH/mysql -u$MYUSER -p$MYPASS -S $MYSOCK"
#if msyql host not in the same machine, then add -h 192.168.31.x after MYSQL_CMD
#like $MYSQL_CMD -h 192.168.31.58 -e "select version();" >/dev/null 2>&1
#make true your machine has the privilege to the msyql database.
$MYSQL_CMD -e "select version();" >/dev/null 2>&1
#if [ $PORT -eq 1 -a $mysqlProcessNum -eq 2 ];then
if [ $? -eq 0 ];then
    echo "db is running"
    exit 0
   else
    $MYSQL_STARTUP  start > $Log_FILE
     sleep 5
     $MYSQL_CMD -e "select version();" >/dev/null 2>&1
#while true can be used, too.
     if [ $? -ne 0 ];then
     for ((i=1;i<1001;i++))
      do
        killall mysqld 
        [ $? -ne 0 ] && break
        sleep 1
     done     
     [ -x $MYSQL_STARTUP ]&&$MYSQL_START start >>$LOG_FILE
     fi
     $MYSQL_CMD -e "select version();" >/dev/null 2>&1 && Status="restarted"||Status="unknown"
    # echo "mysql is while true started."
     echo "Mysql status is $Status.">>$Log_FILE
    mail -s "Mysql status is $Status" 414220021@qq.com <$Log_FILE
    
fi

#[root@test tmp]#  killall   mysqld >/dev/null 2>&1
#[root@test tmp]#  killall   mysqld                
#mysqld: no process killed
