#!/bin/bash
i=1
#while ((i<11))
while [[ i -lt 11 ]]
do
  echo $i
  ((i++))
done
