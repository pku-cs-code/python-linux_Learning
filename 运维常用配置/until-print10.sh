#!/bin/bash
i=10
until [[ $i -le 0 ]]
do
  echo $i
  ((i--))
done
