#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-25 22:28:00
# author: 郑集文
import os,json,ConfigParser,time

def addform(dizhi):
	dt=time.strftime('%Y')
	ny=int(dt)+1
	config = ConfigParser.ConfigParser()
	config.read('duizhangdan/%s.txt'%dizhi)
	for mon in range(1,13):
		asd='%s-%s'%(ny,mon)
		config.add_section(asd)
	config.write(open('duizhangdan/%s.txt'%dizhi,'w'))

with open('card.txt','r') as cf: 
	card_dict=json.load(cf)

for dizhi in card_dict.keys():
	addform(dizhi)
