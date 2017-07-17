#!/bin/bash

function trapper(){
trap ':' INT EXIT TSTP TERM HUP
}

while :
do
   trapper
      clear
      cat <<menu
       1)web a
       2)web b
       3)exit
menu
	     read -p "please select:" num
             case $num in
             1)
              ssh 192.168.31.63
              ;;
             2)
              ssh 192.168.31.58
              ;;
             3|*)
              exit
              ;;
             esac 
done
