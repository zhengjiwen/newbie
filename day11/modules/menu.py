#!/usr/bin/env python
# coding: utf-8
import ssh_client
import re,os
import textwrap
import sys
import time
from db import Sql
import getpass
try:
	import termios
	import tty
except ImportError:
	print '\033[1;31m仅支持类Unix系统 Only unix like supported.\033[0m'
	time.sleep(3)
	sys.exit()


def color_print(msg, color='red', exits=False):
	"""
	Print colorful string.
	颜色打印字符或者退出
	"""
	color_msg = {'blue': '\033[1;36m%s\033[0m',
				 'green': '\033[1;32m%s\033[0m',
				 'yellow': '\033[1;33m%s\033[0m',
				 'red': '\033[1;31m%s\033[0m',
				 'title': '\033[30;42m%s\033[0m',
				 'info': '\033[32m%s\033[0m'}
	msg = color_msg.get(color, 'red') % msg
	print msg
	if exits:
		time.sleep(2)
		sys.exit()
	return msg


class Nav(object):
	"""
	导航提示类
	"""
	def __init__(self, user):
		self.user = user
		self.search_result = {}
		self.user_perm = {}

	def print_group(self,sql):
		os.system('clear')
		username=getpass.getuser()
		group_dict=sql.select_group(username)
		""" 
		打印用户授权的资产组
		"""
		color_print('\t\t\t[%-3s] %-20s %s' % ('ID', '组名', '备注'), 'title')
		id_list=[]
		for i in  group_dict:
			id_list.append(int(i['id']))	
			print '\t\t\t[%-3s] %-15s %s' % (i['id'],i['groupname'],'null')
		print
		msg = """\n\033[1;32m \t\t### 欢迎使用堡垒机   ### \033[0m
		输入 \033[32mID\033[0m 查看主机组内主机.
		输入 \033[32mQ/q\033[0m 退出.
			"""
		print textwrap.dedent(msg)


		while True:
			option = raw_input("\033[1;32mOpt or ID>:\033[0m ").strip()
			if option in ['Q', 'q', 'exit']:
				sys.exit()
			elif option.isdigit:
				if int(option) in id_list:
					self.print_host(sql,option)
			else:
				print "no such id"
			
	def print_host(self,sql,option):
		host_dict=sql.select_host(option)
		options=option
		print
		color_print('[%-3s] %-12s %-15s  %-5s  %-10s  %s' % ('ID', '主机名', 'IP', '端口', '系统用户', '备注'), 'title')
		id_dict={}
		for i in host_dict:
			id_dict[str(i['id'])]=i
		#{'username': 'root', 'ip_addr': '192.168.153.167', 'passwd': 'asdasd', 'hostname': 'root', 'port': 22L, 'id': 2L}"	
			print '[%-3s] %-15s %-15s  %-5s  %-10s  %s' % (i['id'],i['hostname'],i['ip_addr'], i['port'],i['username'],'null')

		msg = """\n\033[1;32m \t\t### 欢迎使用堡垒机   ### \033[0m
		输入 \033[32mID\033[0m 登入主机.
		输入 \033[32mQ/q\033[0m 退出.
			"""
		print textwrap.dedent(msg)

		option = raw_input("\033[1;32mOpt or ID>:\033[0m ").strip()

		if option in ['Q', 'q', 'exit']:
			sys.exit()
		elif option.isdigit and option in id_dict:
			host=id_dict[option]
			ssh=ssh_client.ssh_client(host['ip_addr'],int(host['port']),host['username'],host['passwd'],host['hostname'],self.user)
			ssh.connect()
		else:
			print "no such id"
		self.print_host(sql,options)
		
		
		
				
	@staticmethod
	def print_nav():
		"""
		Print prompt
		打印提示导航
		"""
		msg = """\n\033[1;32m	###	欢迎使用堡垒机   ### \033[0m

		输入 \033[32mG/g\033[0m 显示您有权限的主机组.
		输入 \033[32mQ/q\033[0m 退出.
		"""
		print textwrap.dedent(msg)

def main():
	"""
	he he
	主程序
	"""
	#if not login_user:  # 判断用户是否存在
	#	color_print('没有该用户，或许你是以root运行的 No that user.', exits=True)

	sql=Sql()
	gid_pattern = re.compile(r'^g\d+$')
	nav = Nav('zhengjiwen')
	nav.print_nav()

	try:
		while True:
			try:
				option = raw_input("\033[1;32mOpt>:\033[0m ").strip()
			except EOFError:
				nav.print_nav()
				continue
			except KeyboardInterrupt:
				sys.exit(0)

			if option in ['G', 'g']:
				nav.print_group(sql)
				continue

			elif option in ['Q', 'q', 'exit']:
				sys.exit()
			else:
				print
				print "no such args"
				print

	except KeyboardInterrupt, e:
		color_print(e)
		time.sleep(5)
		pass

