#!/bin/bash
[ ! -e "/oldboy" ]&&mkdir -p /oldboy 
cd /oldboy

for n in {1..10}
do 
touch oldboy-${n}
done
