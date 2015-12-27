#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-10 12:20:19
# author: 郑集文
# Description:

import socket
import time

def conn(func):
	def wrapper():
		ip=raw_input('请输入连接ip: ')
		port=int(raw_input('请输入port: '))
		tio=int(raw_input('请输入超时时间: '))
		ip_port = (ip,port)
		sk = socket.socket()
		sk.connect(ip_port)
		sk.settimeout(tio)
		while True:
			data=sk.recv(1024)
			print data
			username=raw_input('请输入：')
			sk.sendall(username)
			flag_=sk.recv(1024)
			if flag_=='ok':
				passwd=raw_input('请输入密码: ')
				sk.sendall(passwd)
				flag_=sk.recv(1024)
				if flag_=='ok':
					sk.send('ol')
					break
				elif flag_=='no':
					print "\n\n密码输入错误\n"

		func(sk)
	return wrapper
	
@conn
def start(sk):
	#选择
	data=sk.recv(1024)
	print 'receive:',data
	inp=raw_input('请选择：')
	sk.send(inp)

	#exe
	if inp=='1':
		exe(sk)

	#tran&down
	elif inp=='2':
		#down_filename
		data=sk.recv(1024)
		print "receive:",data
		info=raw_input("请选择：")
		sk.sendall(info)

		#down
		if info =="1":
			data=sk.recv(1024)
			print "receive:",data
			path=raw_input("输入路径：")
			sk.send(path)
			data=sk.recv(1024)
			print "receive:",data
			path_l=raw_input("输入路径：")
			sk.send(path_l)
			with open(path_l,'w') as f:
				while True:
					data=sk.recv(1024)
					if not data:
						break				
					f.write(data)
			print "success "
			time.sleep(2)
			quit()

		#tran
		elif info =="2":
			#本地主机
			data=sk.recv(1024)
			print "receive:",data
			path=raw_input("输入路径：")
			sk.send(path)
			#目标主机
			data=sk.recv(1024)
			print "receive:",data
			path_l=raw_input("输入路径：")
			sk.send(path_l)
			sk.recv(1024)
			with open(path,'r') as f:
				while True:
					word=f.read(1024)
					if not word:
						break
					sk.send(word)
			print "success。"
			time.sleep(2)

			quit()
		elif info=='0':
			quit()

	#退出
	elif inp=='0':
		quit()

def exe(sk):
	choice=raw_input("是否退出[y/n]:")
	if choice =='y':
		sk.sendall('y')
		quit()
	elif choice =='n':
		sk.sendall('n')
		pass
	data=sk.recv(1024)
	print ':',data
	info=raw_input('请输入：')
	sk.sendall(info)

	while True:
		flag=sk.recv(1024)
		if flag=='ole':
			sk.send('ole')
			break
		elif flag=='0':
			sk.send('1')
		ret=sk.recv(1024)
		print ret

	exe(sk)

if __name__=='__main__':
	pass

start()
