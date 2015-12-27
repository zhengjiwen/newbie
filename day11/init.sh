#!/bin/bash
# Pw @ 2015-12-27 22:16:55
# Description:

db_name="ssh"
db_username='root'
db_passwd='asdasd'

mysql -u"$db_username" -p"$db_passwd" -e "create database $db_name;" 2>/dev/null 1>&2
mysql -uroot $db_name < init.sql
