#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-10-21 19:39:43
# author: 郑集文
# 登入接口
# Version 2.0.3
import os,sys
import getpass
#用户名密码文件
try:
	username=raw_input("请输入用户名：")
	f=file('%s.list'%username,'r+')

	userfile=0
#导入用户名密码字典
	d_user={}
	d_counter={}
	if userfile != '':
		userfile=f.readline()
		if userfile != '':
			user_list=userfile.strip()
			userlist=user_list.split()
			d_user[userlist[0]]=userlist[1]
			d_counter[userlist[0]]=userlist[2]
	f.close()

	#主程序
	while True:
			#counter导入
			dict_counter={}
			af=file('%s.list'%username,'r+')
			b=af.readline()
			x=b.strip()
			y=x.split()
			af.close()
			dict_counter[y[0]]=y[2]
			counter=int(dict_counter[username])
			password=getpass.getpass("\n请输入密码>>>")
			
			#验证判断
			if password==d_user[username] and counter<2 :
				os.system('clear')
				print "\n\n%s登入成功 （我是欢迎界面）\n\n"%username
				fc=file('%s.list'%username,'w+')
				user_name=userlist[0]
				passwd=userlist[1]
				fc.write('%s %s %s'%(user_name,passwd,'1'))
				break
			elif counter>=2:
				os.system('clear')
				print "\n\n输入错误超过三次,禁止登入！\n\n"
				break
			elif username in d_user and password!=d_user[username]:
				os.system('clear')
				print "\n\n密码输入错误,您还有%d次机会。\n\n"%(2-counter)	
			        user_name=y[0]
				passwd=y[1]
				counter+=1
				fc=file('%s.list'%username,'w+')
				fc.write('%s %s %s'%(user_name,passwd,counter))
				fc.close()
except IOError,e:
	print '未找到%s'%username
except NameError,e:
	pass
