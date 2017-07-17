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



计算access.log中访问行的字节数

[root@test scripts]# awk '{print $10}' access.log |grep -v -|tr "\n" "+"|sed 's#52+#52#g'
11489+2547+2169+244+5252[root@test scripts]

读入的方式
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

很多while循环都能用for循环替代

