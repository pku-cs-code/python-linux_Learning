#!/bin/bash
#para
host01=192.168.1.60
src=/data0/www/www/
dst=www
user=rsync_backup
rsync_passfile=/etc/rsyncd.passwd
inotify_home=/usr/local/inotify/

#judge
if [ ! -e "$src" ]\
|| [ ! -e "${rsync_passfile}" ]\
|| [ ! -e "${inotify_home}/bin/inotifywait" ]\
|| [ ! -e "/usr/bin/rsync" ];
then
   echo "Check File and Folder"
   exit 9
fi

${inotify_home}/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f' -e close_write,delete,create,attrib $src \
| while read file
    do
        #rsync -avzP --delete --timeout=100 --passwd-file=${rsync_passfile} $src $user@$host01::$dst >/dev/null 2>&1
          cd $src && rsync -aruz -R --delete ./ --timeout=100 $user@$host01::$dst --password-file=${rsync_passfile} >/dev/null 2>&1
    done
exit 0
