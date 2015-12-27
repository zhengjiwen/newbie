#!/bin/bash
#author: 郑集文
#重置容错次数脚本。
for user_list in `find . -name "*.list"`
do
    echo `awk -F " " {'print $1" "$2" "0'} $user_list ` > $user_list
done
