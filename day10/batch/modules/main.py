#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-11 21:34:11
# Description:

__author__ = 'Jiwen Zheng'

import sys
from conf import settings
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
		msg = '''-l host_group / -l	: 查看指定主机组 / 查看所有主机组
add host_group		: 导入指定主机组
delete host_group 	: 删除指定主机组'''
		print(msg)

	def show(self):
		db_type=settings.DATABASE['db_type']
		if db_type=='file':
			group_file=settings.GROUP_FILE

			try:
				with open(group_file,'r') as f:
					all_dict=json.load(f)		
			except ValueError:
				sys.exit("No such group")
			show_group=self.show_group
			if show_group:
				print "%s\n"%show_group
				try:
					print all_dict[show_group],
				except KeyError:
					print "no such group"
			else:
				for host in all_dict:
					print "%s\n"%host,
					print all_dict[host],

	def delete(self):
		db_type=settings.DATABASE['db_type']
		if db_type=='file': 
			gname=self.add_group
			group_file=settings.GROUP_FILE
			add_path=settings.ADD_PATH
			try:
				with open(group_file,'r') as f:
					all_dict=json.load(f)
			except Exception:
				sys.exit('无主机组')

			try:
				all_dict.pop(self.add_group)
			except KeyError:
				sys.exit('no such group')
			with open(group_file,'w') as f:
				json.dump(all_dict,f)	
			print "删除成功"


	def add(self):
		db_type=settings.DATABASE['db_type']
		if db_type=='file': 
			gname=self.add_group
			group_file=settings.GROUP_FILE
			add_path=settings.ADD_PATH

			data=xlrd.open_workbook('%s/%s.xls'%(add_path,gname))
			table=data.sheets()[0]
			row_num=table.nrows
			group_dict={}
			for i in range(2,row_num):
				group_dict[table.row_values(i)[0]]='{port:%s,username:%s,passwd:%s,memo:%s,}'%(int(table.row_values(i)[1]),table.row_values(i)[2],table.row_values(i)[3],table.row_values(i)[4])   
			try:
				with open(group_file,'r') as f:
					all_dict=json.load(f)
			except Exception:
				all_dict={}
			all_dict[gname]=group_dict
			with open(group_file,'w') as f:
				json.dump(all_dict,f)
			print "添加成功"

	def handle(self):
		func=getattr(self,self.args[1])
		func()
