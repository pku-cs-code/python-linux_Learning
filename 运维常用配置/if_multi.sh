#!/bin/bash
#This script  is created by zhangcai on 2017-05-21
#function: compare two nums.
#author:zhangcai
#version:0.1
read -t 10 -p "please input two nums:" a b
#if [ $a -gt $b ];then
if (($a > $b));then
   echo "yes, $a > $b"
elif [ $a -eq $b ];then
   echo "yes, $a=$b"
else
   echo "yes, $a < $b"
fi
