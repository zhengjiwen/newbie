#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-10 12:18:03
# author: 郑集文
# Description:

import SocketServer
import os,time,json
import hashlib
 
class MyServer(SocketServer.BaseRequestHandler):

 
	def handle(self):
		conn=self.request
		
		with open('user.txt','r') as f:
			user_dict=json.load(f)

		while True:
			conn.sendall('请输入用户名：')
			username=conn.recv(1024)
			if username in user_dict:
				conn.sendall('ok')
				passwd=conn.recv(1024)
				passwdhx=hashlib.md5(passwd)
				passwdhx=passwdhx.hexdigest()
				if passwdhx in user_dict[username]:
					conn.sendall('ok')
					conn.recv(1024)
					break
				else:
					conn.sendall('ok')
		

		conn.sendall('选择 1.执行命令 2.收发文件 0.退出')
		data=conn.recv(1024)
		
		#exe
		if data=='1':
			self.exe(conn)	
		#down_tran
		elif data=='2':
			self.dtfile(conn)
		#exit
		elif data=='0':
			pass
		
	def exe(self,conn):
		flag=conn.recv(1024)
		if flag=='y':
			return 0
		elif flag=='n':
			pass
		conn.sendall('请输入要执行的命令：')
		cmd=conn.recv(1024)
		ret=os.popen(cmd)

		while True:
			dt=ret.read(1024)
			if not dt:
				conn.send('ole')
			else:
				conn.send('0')
			flag=conn.recv(1024)
			if flag=='ole':
				self.exe(conn)
			elif flag=='1':
				conn.sendall(dt)
			


		conn.recv(1024)
		self.exe(conn)

	def	dtfile(self,conn): 
		conn.sendall('请选择 1.下载文件 2.上传文件 0.退出:')
		data=conn.recv(1024)

		#down
		if data=='1':
			conn.sendall('请输入下载文件路径: ')
			path=conn.recv(1024)
			conn.sendall('请输入本地路径：')
			conn.recv(1024)
			self.down(path,conn)
		
		#tran	
		elif data=='2':
			conn.sendall('请输入本地文件路径：')
			conn.recv(1024)
			conn.sendall('请输入上传目标主机文件路径: ')
			filename=conn.recv(1024)
			conn.send('ole')
			
			self.tran(filename,conn)


		elif data=='0':
			pass
			

	def down(self,filename,conn):
		with open(filename,'r') as f:
			while True:
				word=f.read(1024)
				if not word:	
					conn.send(word)
					break
				conn.send(word)
				
			
	def tran(self,filename,conn):
		with open(filename,'w') as f:
			while True:
				data=conn.recv(1024)
				if not data:
					break
				f.write(data)
		


if __name__=='__main__':
	pass

#ip=raw_input('请输入绑定IP: ')
#while True:
#	try:
#		port=int(raw_input('请输入绑定端口号: '))
#		if port<0:
#			print "\n请输入0~65535范围内的正整数。\n"
#		elif port>65535:
#			print "\n请输入0~65535范围内的正整数。\n"
#		else:
#			break
#	except ValueError,e:
#		print "\n请输入0~65535范围内的正整数。\n"

server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
server.serve_forever()
