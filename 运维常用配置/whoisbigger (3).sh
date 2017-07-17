#!/bin/bash
a=$1
b=$2
if [ $# -ne 2 ]
  then 
    echo "Usage: num1 num2"
     exit 1

fi
[ -n "`echo $a|sed 's/[0-9]//g'`" ]&&echo "first arg must be num"&&exit 1
[ -n "`echo $b|sed 's/[0-9]//g'`" ]&&echo "second arg must be num"&&exit 1
#read -p "please input two integers:" a b
if [ $a -gt $b ]
   then 
      echo "$a is bigger than $b."
   elif [ $a -eq $b ]
      then
        echo "$a is equal to $b."
   else
      echo "$a is less than $b."

fi
