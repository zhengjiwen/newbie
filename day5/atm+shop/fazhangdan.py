#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-25 22:15:53
# author: 郑集文

import time,json,os
from module import youjian

nowtime=time.strftime('%Y-%m')

with open('card.txt','r') as cf:
	card_dict=json.load(cf)
for user in card_dict.keys():
	info_list=[]
	with open('duizhangdan/%s.txt'%user,'r') as f:
		flag=False
		for i in f:
			if '[' in i:
				if nowtime in i:
					flag=True
				else:
					flag=False
			if flag:
				info_list.append(i)
	youjian.youjian(user,info_list)
