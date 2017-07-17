#!/bin/bash
a="$1"
b="$2"
Usage(){
  echo "USAGE:sh $0 num1 num2"
   exit 1
}
if [ $# -ne 2 ];
   then
    Usage
fi
expr $a + 0 >&/dev/null #2>&1
[ $? -ne 0 ] &&Usage  #if not 0,continue to read line
expr $b + 0 >&/dev/null #2>&1
[ $? -ne 0 ] &&Usage #if not 0,continue to read line.if 0 break to jump out
echo "a-b=$(($a-$b))"
echo "a+b=$(($a+$b))"
echo "a*b=$(($a*$b))"
echo "a/b=$(($a/$b))"
echo "a**b=$(($a**$b))"
echo "a%b=$(($a%$b))"
