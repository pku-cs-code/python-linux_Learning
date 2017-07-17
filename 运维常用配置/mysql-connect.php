<?php
  $link_id=mysql_connect('localhost','root','123456') or mysql_error();
  if($link_id){
      echo "mysql is connnected by zhangcai.";
   }else{
  echo  mysql_error();
   }
?>
