#!/bin/bash
if [ $# != 2 ];then
    echo "Usage:$0 ip port"
    exit 1
fi
HttpPortNum=`nmap $1 -p $2|grep open|grep -v grep|wc -l`
if [ $HttpPortNum -eq 1 ];then
   echo "$1 $2 is open"
   else
   echo "$1 $2 is closed."
fi
