#!/bin/bash
i=$1
#while ((i>0))
while [[ $i -gt 0 ]]
do
   printf "$i\n"
   ((i--))
done
