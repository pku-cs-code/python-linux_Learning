#!/bin/bash
HttpCode=`curl -I -s http://192.168.31.60 |head -1|cut -d  " " -f2`
#curl -I -s http://192.168.31.60 |sed -n '1p'|grep 200
# curl -I -s http://192.168.31.60 |head -1|grep 200
if [ "$HttpCode" = "200" ];then
   echo "httpd is running"
   else
   echo "httpd is not running."
   /etc/init.d/httpd start
fi



����access.log�з����е��ֽ���

[root@test scripts]# awk '{print $10}' access.log |grep -v -|tr "\n" "+"|sed 's#52+#52#g'
11489+2547+2169+244+5252[root@test scripts]

����ķ�ʽ
1
exec<FILE
sum=0
while read line
do
cmd
done


2 cat ${FILE_PATH}|while read line
do 
cmd
done


3
while read line
do
cmd
done<${file_path}

�ܶ�whileѭ��������forѭ�����

