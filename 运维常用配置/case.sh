#!/bin/bash
read -p "please input a num:" ans
case "$ans" in
1)
  echo "the num you input is 1."
;;
2)
  echo "the num you input is 2."
;;
[3-9])
  echo "the num you input is $ans"
;;
*)
  echo "the num you input must be less than 9."
  exit;
;;
esac

