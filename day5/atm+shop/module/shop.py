#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-10-20 19:56:16
# author: 郑集文

import json,os
from collections import Counter
from card import *

@auth
def shangpin(dizhi):
	#new商品dict
	with open('shangpin.txt','r') as sf:
		shangpin_dict=json.load(sf)	

	#购物list
	gwlist=[]
	while True:
		sl(**shangpin_dict)
		#商品号
		spm=raw_input("请输入想要加入购物车的商品 q退出: ")
		if spm in shangpin_dict:
			gwlist.append(spm)
		elif spm=='q':
			os.system('clear')
			#出现次数
			cxcc=dict(Counter(gwlist))
			os.system('clear')
			print '加入购物车成功。\n\n'
			break
		else:
			os.system('clear')
			print "商品不存在，请重新输入。\n\n"

	for k,v in cxcc.items():
		print "%s\t%s件\n"%(k,v),

	qian=[]
	for shangpin in cxcc.keys():
		qian.append(int(shangpin_dict[shangpin])*int(cxcc[shangpin]))
	money=0
	for i in qian:
		money+=int(i)	

	print "\n\n共计%s元。\n\n"%money
	flag=raw_input("\n请输入代码 1.立即购买。 0.退出：")
	if flag=='1':
		ads=zhifu(dizhi,money)
		if ads:
			print "支付成功。共花费%s。\n\n"%money
	elif flag=='0':
		quit()
	else:
		os.system('clear')
		print "输入错误，请重新输入。\n\n"


		

#	for k,v in cxcc.items():
#		a='%s'%(nspd[k].keys())
#		spname=a[1:-1]
#		moneynum=shangpin_dict.get(spname)*v
#		moneynum=
		
		


def addsp():
	sp_dict={}
	try:
		with open('shangpin.txt','r') as sf:
			sp_dict=json.load(sf)	
	except ValueError:
		pass
			
	while True:
		spn=raw_input('请输入商品名 （q退出）：')
		if spn=='q':
			break
		if spn in sp_dict:
			os.system('clear')
			print "商品已存在。\n\n"
			continue
		money=raw_input("请输入商品价格：")
		os.system('clear')
		print "\n请继续添加。\n\n"
		sp_dict[spn]=int(money)
		
	with open('shangpin.txt','w') as sf:
		json.dump(sp_dict,sf)
	os.system('clear')
	print "商品添加成功。\n\n"


def sl(**kwargs):
	print "%s\n"%('*'*33)
	print "商品名\t价格\n"
	for k,v in kwargs.items():
		print "%s\t%s\n"%(k,v),
	print "\n%s\n"%('*'*33)
