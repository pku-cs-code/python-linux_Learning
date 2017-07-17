#!/bin/bash
#created by zhangcai on 2017-05-25
#usually used after the web service start to check if the service successfully is started.
#can be placed with start script
. /etc/init.d/functions
 RETVAL=0
FAILCOUNT=0
SCRIPTS_PATH="/server/scripts"
MAIL_GROUP="414220021@qq.com test@qq.com"
LOG_FILE="/tmp/web-check.log"
function GetUrlStatus(){
  for((i=1;i<=3;i++))
   do
     wget -T 2 --tries=1 --spider http://${1} >/dev/null 2>&1
     [ $? -ne 0 ] &&let FAILCOUNT+=1;
   done
     if [ $FAILCOUNT -gt 1 ];then
          RETVAL=1
          NOWTIME=`date +"%m-%d %H:%M:%S"`
          SUBJECT_CONTENT="http://${HOSTNAME} service is error,${NOWTIME}."
          for MAIL_USER in $MAIL_GROUP
            do
          echo  "send to: $MAIL_USER,Title:$SUBJECT_CONTENT">$LOG_FILE
              mail -s  "$SUBJECT_CONTENT" $MAIL_USER <$LOG_FILE 
#mail mutt
            done
          else 
            RETVAL=0
    fi
    return $RETVAL

}

[ ! -d $SCRIPTS_PATH ]&&{
  mkdir -p $SCRIPTS_PATH
}

[ ! -f "$SCRIPTS_PATH/domain.list" ]&&{
cat >$SCRIPTS_PATH/domain.list<<EOF
oldboy.blog.51cto.com
bbs.etiantian.org
EOF
}

#service check
for URL in `cat $SCRIPTS_PATH/domain.list`
do
  echo -n "checking $URL "
 GetUrlStatus $URL &&action  "success" /bin/true||action  "failured" /bin/false
done
