#!/bin/bash
new_chars(){
RED_COLOR='\E[1;31m'
GREEN_COLOR='\E[1;32m'
YELLOW_COLOR='\E[1;33m'
BLUE_COLOR='\E[1;34m'
RES='\E[0m'
if [ $# != 2 ];then
  echo "Usage:$0 content {red|green|yellow}"
  exit 1
fi
case "$2" in
red|RED|Red)
  echo -e "${RED_COLOR}"$1"${RES}"
;;
yellow|YELLOW|Yellow)
  echo -e "${YELLOW_COLOR}"$1"${RES}"
;;
green|GREEN|Green)
  echo -e "${GREEN_COLOR}"$1"${RES}"
;;
*)
  echo -e "${BLUE_COLOR}"$1"${RES}"
  exit;
;;
esac
}
#new_chars yubing red
#new_chars xiaoge green
#new_chars "welcome." yellow
new_chars "$1" "$2"
