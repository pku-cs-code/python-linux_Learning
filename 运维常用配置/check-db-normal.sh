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
$MYSQL_CMD -e "select version();" >/dev/null 2>&1
#if [ $PORT -eq 1 -a $mysqlProcessNum -eq 2 ];then
if [ $? -eq 0 ];then
    echo "db is running"
   else
    $MYSQL_STARTUP  start > $Log_FILE
     sleep 10
     $MYSQL_CMD -e "select version();" >/dev/null 2>&1
     if [ $? -ne 0 ];then
     while true
      do
        killall mysqld 
        [ $? -ne 0 ] && break
        sleep 1
     done     
     $MYSQL_STARTUP start >>$Log_FILE && status="mysql is succesfully started."||status="failure"
    # echo "mysql is while true started."
    mail -s "mysql started startup status is $status" 414220021@qq.com <$LogPath
    fi
fi

#[root@test tmp]#  killall   mysqld >/dev/null 2>&1
#[root@test tmp]#  killall   mysqld                
#mysqld: no process killed
