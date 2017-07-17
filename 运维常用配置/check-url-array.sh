#!/bin/bash

. /etc/init.d/functions
url_list=(
www.baidu.com
http://etiantian.org
http://oldboy.blog.51cto.com
http://192.168.31.60
)

function wait(){
echo -n "execute cmd after 3 secconds."
for((i=0;i<3;i++))
do
  echo -n ".";sleep 1
done
echo "\n"
}

function check_url(){
  wait
  echo "check ulr..."
  for((i=0;i<${#url_list[@]};i++))
  do
    judge=($(curl -I -s  --connect-timeout 5  ${url_list[$i]}|head -1))
  # echo ${judge[1]} ${judge[2]}
   if [[ "${judge[1]}" = "200" && "${judge[2]}"=="OK" ]];then
     action "${url_list[$i]} is successful." /bin/true
    else
     action "${url_list[$i]} is failed." /bin/false
    fi
#    for((j=0;j<${#judge[@]};j++))
#      do
#         echo "${judge[$j]}"
#      done
  done
}
check_url
