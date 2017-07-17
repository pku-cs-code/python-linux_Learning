#bak site
ip=`grep IPADDR /etc/sysconfig/network-scripts/ifcfg-eth0 | cut -d  = -f2`
cd /backup/$ip || mkdir /backup/$ip


cd /var/html/ && tar zcf /backup/$ip/www_$(date +%F).tar.gz ./www
cd /app/ && tar zcf /backup/$ip/logs_$(date +%F).tar.gz ./logs

#bak sysconf
cd / && tar zcf /backup/$ip/etc_$(date +%F).tar.gz ./etc
cd /server && tar zcf /backup/$ip/scripts_$(date +%F).tar.gz ./scripts
/bin/cp /var/spool/cron/root /backup/$ip/

#rsync data to backserver
cd /backup/ && rsync -avzP ./ rsync_backup@192.168.1.60::backup --password-file=/etc/rsyncd.passwd >/dev/null 2>&1

#del file 7 days ago
find /backup/$ip/ -type f -name "*.tar.gz" -mtime +7 | xargs rm -f

