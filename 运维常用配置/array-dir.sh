#!/bin/bash

array=($(ls))
for ((i=0;i<${#array[*]};i++))
do
 echo "array[$i] is ${array[$i]}"
done
