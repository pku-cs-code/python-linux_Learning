for f in `ls ./*log*`
do
#mv $f `echo ${f/%log/LOG}`
 mv $f 	`echo $f|sed 's/log/LOG/g'`
done
