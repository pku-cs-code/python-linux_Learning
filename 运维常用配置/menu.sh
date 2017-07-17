#!/bin/bash
#zhangcai
cat <<END
1.[install lamp]
2.[install lnmp]
3.[install nfs]
4.[install rsync]
END
read a
[ $a -eq 1 ]&&{
cat<<END
[1.install apache]
[2.isntall mysql]
END
read b
echo want to install $b.apache
}
