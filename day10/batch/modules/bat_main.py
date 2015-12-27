#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-12 01:41:49
# Description:

__author__ = 'Jiwen Zheng'

import sys 
from conf import settings
import json
import os
import threading
import time
import paramiko

class ArgvHandler(object):

	def __init__(self,args):
		self.args = args
		self.argv_parser()
		self.handle()

	def argv_parser(self):

		if len(self.args) < 3:
			self.help_msg()
			sys.exit('err3')
		elif len(self.args) > 5:
			self.help_msg()
			sys.exit('err4')
		else:
			mandatory_fields = ["cmd","tran"]
			count=0
			for i in mandatory_fields:
				if i in self.args:
					count+=1
			if count==0:
				self.help_msg()
				sys.exit("\033[31;1mno such argv\033[0m")
			try:
				if count>1:
					self.help_msg()
					sys.exit("\033[1;31;40m 参数只能存在一个\033[0m")

				if len(self.args)==4:
					if hasattr(self,self.args[1]):
						self.group=self.args[2]
						self.l_file=self.args[2]
						self.command=self.args[3]
						self.r_file=''
					else:
						self.help_msg()
						sys.exit("error 4")

				elif len(self.args)==5:
					if hasattr(self,self.args[1]):
						self.group=self.args[2]
						self.l_file=self.args[3]
						self.r_file=self.args[4]
					else:
						self.help_msg()
						sys.exit("error 5")
						

				elif len(self.args)==3:
					if hasattr(self,self.args[1]):
						self.command=self.args[2]
						self.group=''
					else:
						self.help_msg()
						sys.exit()

				elif len(self.args)==1:
					self.help_msg()
					sys.exit()
				else:
					self.help_msg()
					sys.exit()

			except (IndexError,ValueError):
				self.help_msg()
				sys.exit()
		

	def help_msg(self):
		msg = '''
cmd	group_name 'command' / exe 'command'	:指定主机组的批量执行命令 / 全部主机批量执行命令 
tran	group_name local_file remotepath / tran local_file remotepath	:传送文件到指定主机组 / 传送文件到所有主机组'''
		print(msg)

	def handle(self):
		func=getattr(self,self.args[1])
		all_dict=self.load_group()
		if not self.group:
			for host_group in all_dict:
				group_host_dict=all_dict[host_group]
				for host in group_host_dict:
					t = threading.Thread(target=func, args=(host,group_host_dict[host],))
					t.start()

		elif self.group:
			try:
				group_host_dict=all_dict[self.group]
			except KeyError:
				if self.args[1]=='cmd':
					sys.exit('\033[1;31;49mno such group\033[0m')
				else:
					self.group=''
					self.handle()	
					sys.exit()

			for host in group_host_dict:
				t = threading.Thread(target=func, args=(host,group_host_dict[host],))
				t.start()

	def cmd(self,ip,host):
		host=host[1:-2]
		host=host.split(',')

		port=host[0][5:]
		username=host[1][9:]
		passwd=host[2][7:]	
		memo=host[3][5:]

		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,int(port),username,passwd)
		stdin, stdout, stderr = ssh.exec_command(self.command)
		print("\t%s\n%s"%(memo,stdout.read()))
		ssh.close()

	def tran(self,ip,host):
		if not self.r_file:
			l_file=self.l_file
			r_file=self.command	
		else:
			l_file=self.l_file
			r_file=self.r_file

		host=host[1:-2]
		host=host.split(',')

		port=host[0][5:]
		username=host[1][9:]
		passwd=host[2][7:]	
		memo=host[3][5:]

		t = paramiko.Transport((ip,int(port)))
		t.connect(username = username, password=passwd)
		sftp = paramiko.SFTPClient.from_transport(t)
		localpath=l_file
		remotepath=r_file
		try:
			sftp.put(localpath,remotepath)
		except OSError:
			print "l_file=%s"%l_file
			print "r_file=%s"%r_file
			print "\033[1;31;39mno such file\033[0m"
		t.close()

	def load_group(self):
		group_file=settings.GROUP_FILE

		assert os.path.exists(group_file)

		try:
			with open(group_file,'r') as f:
				all_dict=json.load(f)	
		except Exception:
			sys.exit('\033[1;31;40m 主机文件损坏\033[0m')
		return all_dict
