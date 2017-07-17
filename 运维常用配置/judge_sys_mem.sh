#!/bin/bash
cur_free=` free -m|awk  '/buffers\//  {print $NF}'`
chars="current memory is ${cur_free}M"
if [ $cur_free -lt 99999999900 ]
   then
    echo $chars
    echo $chars |mail -s "$chars" 414220021@qq.com
fi
