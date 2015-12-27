#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-11 21:34:11
# Description:

__author__ = 'Jiwen Zheng'

import sys
from conf import setting
from modules import db
import json
import os
import xlrd

class ArgvHandler(object):
	def __init__(self,args):
		self.args = args
		self.argv_parser()
		self.handle()

	def argv_parser(self):
		if len(self.args) < 2:
			self.help_msg()
			sys.exit()
		elif len(self.args) > 3:
			self.help_msg()
			sys.exit()
		else:
			if '-l' in self.args:
				if len(self.args)==3:
					try:
						self.show_group = self.args[self.args.index("-l") + 1]
						self.show()
						sys.exit()
					except IndexError:
						self.help_msg()
						sys.exit()
				elif len(self.args)==2:
					self.show_group = ''
					self.show()
					sys.exit()
				else:
					print('-l选项只能单独使用。')
					sys.exit()

			mandatory_fields = ["add","delete"]
			count=0
			for i in mandatory_fields:
				if i in self.args:
					count+=1	
			if count>1:
				self.help_msg()
				sys.exit()
				
			if len(self.args)==3:
				if hasattr(self,self.args[1]):
					self.add_group = self.args[2]
				else:
					self.help_msg()
					sys.exit()


	def help_msg(self):
		msg = '''
add host_group		: 导入指定主机组
delete host_group 	: 删除指定主机组'''
		print(msg)


	def delete(self):
		db_type=setting.db_type
		if db_type=='database': 
			gname=self.add_group
			sql=db.Sql()
			group_id=sql.select_group_id(gname)
			sql.delete_host(group_id)
			num=sql.delete_group(gname)
			print 'success'
			

	def add(self):
		db_type=setting.db_type
		if db_type=='database': 
			gname=self.add_group
			add_path=setting.ADD_PATH
			data=xlrd.open_workbook('%s/%s.xls'%(add_path,gname))
			table=data.sheets()[0]
			row_num=table.nrows
			host_list=[]
			sql=db.Sql()
			username=raw_input("请输入用户名：")
			group_id=sql.insert_group(gname,username)
			for i in range(2,row_num):
			#id | hostname | ip_addr         | port | username | passwd | group_id | memo

			#IP PORT USERNAME PASSWD MENO HOSTNAME

				host=(table.row_values(i)[0],table.row_values(i)[1],table.row_values(i)[2],table.row_values(i)[3],table.row_values(i)[4],table.row_values(i)[5],group_id)
				host_list.append(host)


			#group_id,**host_dict
			count=sql.insert_host(group_id,*host_list)
			print "添加成功"

	def handle(self):
		func=getattr(self,self.args[1])
		func()
