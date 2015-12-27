#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import os,sys
import socket
import json
import hashlib
from progressbar import Bar,Percentage,ProgressBar,RotatingMarker


class Client(object):

	def __init__(self,sys_argv):
		self.args = sys_argv
		self.argv_parser()
		self.response_code = {
			'200': "pass user authentication",
			'201': "wrong username or password",
			'202': "invalid username or password",
			'300': "Ready to get file from server",
			'301': "Ready to send to  server",
			'302': "File doesn't exist on ftp server",
		}

		self.handle()
	def help_msg(self):
		msg = '''
		-s ftp_server_addr	:ftp server ip address, mandatory
		-p ftp_server_port	:ftp server port , mandatory
		'''
		print(msg)

	def instruction_msg(self):
		msg = '''
		get ftp_file		: download file from ftp server
		put local  remote   : upload local file to remote
		ls				  : list files on ftp server
		cd  path			: change dir on ftp server

		'''
	def argv_parser(self):
		if len(self.args) < 5:
			self.help_msg()
			sys.exit()
		else:
			mandatory_fields = ["-p","-s"]
			for i  in mandatory_fields:
				if i not in self.args:
					sys.exit("\033[31;1mLack of argument [%s]\033[0m" % i)
			try:
				self.ftp_host = self.args[self.args.index("-s") + 1]
				self.ftp_port = int(self.args[self.args.index("-p") + 1])
			except (IndexError,ValueError):
				self.help_msg()
				sys.exit()

	def connect(self,host,port):
		try:
			self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #实例化socket
			self.sock.connect((host,port)) #连接socket服务器
		except socket.error as e:
			sys.exit("\033[31;1m%s\033[0m" %e)

	def auth(self):
		retry_count = 0
		while retry_count < 3:
			username = raw_input("\033[32;1mUsername:\033[0m").strip()
			if len(username) == 0 : continue
			password = raw_input("\033[32;1mPassword:\033[0m").strip()
			if len(password) == 0 : continue
			raw_json = json.dumps({
				'username': username,
				'password': password
			})
			auth_str = "user_auth|%s" %(raw_json)
			self.sock.send(auth_str)
			server_response = self.sock.recv(1024)
			response_code = self.get_response_code(server_response)
			print(self.response_code[response_code])
			if response_code == '200':
				self.login_user = username
				self.cwd = "/"
				return  True
			else:
				retry_count +=1
		else:
			sys.exit("\033[31;1mToo many attempts!\033[0m")

	def get_response_code(self,response):
		response_code = response.split("|")
		code =response_code[1]
		return code

	def parse_instruction(self,user_input):
		user_input_to_list = user_input.split()
		func_str = user_input_to_list[0]
		if hasattr(self,'instruction__'+ func_str):
			return True,user_input_to_list
		else:
			return False,user_input_to_list

	def interactive(self):
		try:
			self.logout_flag = False
			while  self.logout_flag is not True:
				user_input = raw_input("[%s]:%s" %(self.login_user,self.cwd)).strip()
				if len(user_input) == 0:continue
				status,user_input_instructions = self.parse_instruction(user_input)
				if status is True:
					func = getattr(self,"instruction__" + user_input_instructions[0])
					func(user_input_instructions)
				else:
					print("\033[31;1mInvalid instruction!\033[0m")
		except KeyboardInterrupt:
			print "\n---  goodbye  ----"
	

	def instruction__rm(self,instructions):
		if len(instructions) == 1:
			print("Input the remote filename which you want to be transmission !")
			return
		else:
			file_name = instructions[1]
			file_name_=os.path.basename(file_name)
			raw_str = "file_rm|%s"% (json.dumps(file_name_))
			self.sock.send(raw_str)
		exist=self.sock.recv(1024)
		if exist=='exists':
			self.sock.send('ok1')
			print "删除%s成功"%file_name
		elif exist=='noexists':
			print "no such file"
			return

	def instruction__ls(self,instructions):
		if len(instructions) == 1:
			print("Input the remote filename which you want to be transmis    sion !")
			return
		else:
			raw_str = "file_ls|ls"
			self.sock.send(raw_str)
			ret=self.sock.recv(4096)	
			ret=ret.strip()
			print ret

	def instruction__put(self,instructions):
		if len(instructions) == 1:
			print("Input the remote filename which you want to be transmission !")
			return
		else:

			file_name = instructions[1]

			file_name_=os.path.basename(file_name)
			raw_str = "file_put|%s"% (json.dumps(file_name_))
			self.sock.send(raw_str)

			self.sock.recv(1024)

			if os.path.exists(file_name):
				self.sock.send('ok')
				file_size = os.path.getsize(file_name)
			else:
				self.sock.send('no')
				print "no such file"
				return

			fl=self.sock.recv(1024)
			if fl=='ok':
				pass

			response_str,code = self.sock.recv(1024).split("|")
			if code == "300": #ready to get file
				self.sock.send("response|301|%s" %(file_size))
				flag_a=self.sock.recv(1024)
				if flag_a=='ok':
					self.sock.send('ok')
				else:
					self.sock.send('no')
					print "空间不足，剩余空间%s字节"%flag_a
					return
				total_file_size = int(file_size)
				received_size = 0
				local_file_obj = open(file_name,"r")
				hs_all=''
				size_=total_file_size/100
				if size_==0:
					size_=1
				pbar=self.p_bar#进度条
				bar_flag=False
				while total_file_size != received_size:
					data=local_file_obj.read(4096)
					self.sock.send(data)
					hs=hashlib.md5(data)
					hs=hs.hexdigest()
					hs_all+=hs
					received_size += len(data)
					percentage=received_size/size_
					if percentage==100:
						pbar.update(100)
						bar_flag=True
						pbar.finish()
					elif percentage>100:
						pbar.update(100)
						bar_flag=True
						pbar.finish()
					else:
						pbar.update(percentage)
				else:
					local_file_obj.close()	
					if not bar_flag:
						pbar.update(100)
						pbar.finish()
					hs_cli=hashlib.md5(hs_all)
					hs_cli=hs_cli.hexdigest()
					flag=self.sock.recv(1024)
					if flag=='ok':
						pass
					self.sock.send(hs_cli)
					flag_m=self.sock.recv(1024)
					if flag_m=='md5ok':
						print("\033[32;1m----file transmission finished-----\033[0m")
						print("md5 true")
					elif flag_m=='md5no':
						print("\n\nmd5 false")

			elif code == '302' : #file doesn't exist
				print(self.response_code[code])


	def instruction__get(self,instructions):
		if len(instructions) == 1:
			print("Input the remote filename which you want to be downloaded!")
			return
		else:
			file_name = instructions[1]
			raw_str = "file_get|%s"% (json.dumps(file_name))
			self.sock.send(raw_str)
			response_str,code,file_size = self.sock.recv(1024).split("|")
			if code == "300": #ready to get file
				self.sock.send("response|301")
				total_file_size = int(file_size)
				received_size = 0
				local_file_obj = open(file_name,"wb")
				hs_all=''
				size_=total_file_size/100
				if size_==0:
					size_=1
				pbar=self.p_bar#进度条
				flag=False
				while total_file_size != received_size:
					data = self.sock.recv(4096)
					hs=hashlib.md5(data)
					hs=hs.hexdigest()
					hs_all+=hs
					received_size += len(data)
					local_file_obj.write(data)
					percentage=received_size/size_
					if percentage>100:
						pbar.update(100)
						flag=True
						pbar.finish()
					elif percentage==100:
						pbar.update(100)
						flag=True
						pbar.finish()
					else:
						pbar.update(percentage)
				else:
					if not flag:
						pbar.update(100)
						pbar.finish()
					print("\033[32;1m----file download finished-----\033[0m")
					hs_cli=hashlib.md5(hs_all)
					hs_cli=hs_cli.hexdigest()
					self.sock.send('ok')
					hs_ser=self.sock.recv(4096)
					if hs_ser==hs_cli:	
						local_file_obj.close()
						print "md5 true"
					else:
						print "client md5:%s"%hs_cli
						print "server md5:%s"%shs_ser
						rm=raw_input("md5错误是否删除文件[y/n]")
						if rm == 'y':
							sys.path.remove(file_name)
						if rm == 'n':
							pass
			elif code == '302' : #file doesn't exist
				print(self.response_code[code])


	@staticmethod
	def GetPathSize(strPath):  
		if not os.path.exists(strPath):  
			return 0;  
		if os.path.isfile(strPath):  
			return os.path.getsize(strPath);  
		nTotalSize = 0;  
		for strRoot, lsDir, lsFiles in os.walk(strPath):  
			for strDir in lsDir:  
				nTotalSize = nTotalSize + GetPathSize(os.path.join(strRoot, strDir));  
			for strFile in lsFiles:  
				nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile));  
		return nTotalSize;


	@property
	def p_bar(self):
   		widgets = ['Download: ', Percentage(), ' ', Bar(marker=RotatingMarker()),]
		pbar = ProgressBar(widgets=widgets, maxval=100).start()
		return pbar


	def handle(self):
		self.connect(self.ftp_host,self.ftp_port)
		if self.auth():
			self.interactive()

