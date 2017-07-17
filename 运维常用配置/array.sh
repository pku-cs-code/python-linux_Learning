#!/bin/bash
#array practice
array=(

one
two
three
four

five

)
for ((i=0;i<${#array[*]};i++))
do
echo "array[$i] is ${array[$i]}"

done
echo "-----------------"
echo "The length of array is:${#array[*]}"
