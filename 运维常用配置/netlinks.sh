#view netlinks stat
netstat -n | awk '/^tcp/ {++oldboy[$NF]} END {for(a in oldboy) print a, oldboy[a]}'
