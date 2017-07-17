#!/bin/bash
for user in `seq -w 10`
do
 useradd oldboy-$user
 echo "$user"|passwd --stdin oldboy-$user
done
