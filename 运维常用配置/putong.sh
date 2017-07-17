for ip in `cat iplist`
do
  scp -P22 -r -p ~/$1 test001@$ip:~/
  ssh -t -p 22  test001@$ip sudo rsync -avzP $1 /root/
done
