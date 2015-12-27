#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-16 09:11:20
# author: 郑集文
# Description:
import json,hmac,time,random,re,os,getpass
import code,pickle
from main import *


def register():
	"""注册函数"""
	
	#导入字典
	try:
		with open('user.txt','r') as cf:
			card_dict=json.load(cf)
	except ValueError:
		card_dict={}
	
	cardnum=user_id(**card_dict)

	#邮箱验证
	p=re.compile(r'^[\w\d]+[\d\w\_\.]+@([\d\w]+)\.([\d\w]+)(?:\.[\d\w]+)?$')

	try:
		with open('eml.txt','r') as ef:
			email_list=pickle.load(ef)
	except EOFError:
		email_list=[]
		
	while True:
		#输入邮箱
		while True:
			s=raw_input('\033[1;31;40mplease input your email: \033[0m')
			os.system('clear')
			s_=raw_input('\nplease input your email again: ')
			if s==s_:
				break
			else:
				os.system('clear')
				print '\n两次输入邮箱地址不同，请重新输入。\n\n'
		if s in email_list:
			os.system('clear')
			print "邮箱已绑定，请更换邮箱。\n\n"
			continue
		else:
			email_list.append(s)
		m=p.match(s)
		if m==None:
			os.system('clear')
			print '您输入的邮箱格式不正确，请重新输入。\n'
		else:
			os.system('clear')
			print "发送验证码到%s。"%s
			idcode=code.yanzhengma(s)
			os.system('clear')
			print "验证码已送到%s，请注意查收。\n\n"%s
			break

	dizhi=s

	while True:
		num=raw_input('请输入验证码: ')
		if int(num)==int(idcode):
			break
		else:
			os.system('clear')
			print "验证码输入错误，请重新输入。\n\n"

	#密码
	while True:
		#输入密码
		passwd=getpass.getpass("\n\nPlease input passwd >>>")
		passwd_=getpass.getpass("\nPlease input passwd again >>>")
		if passwd==passwd_:
			if not passwd:
				os.system('clear')
				print '密码不能为空，请重新输入。\n\n'
			else:
				break
		else:
			os.system('clear')
			print "两次输入密码结果不同，请重新输入。\n\n"

	#密码加盐处理
	h=hmac.new('test')
	h.update(passwd)
	hashpw=h.hexdigest()

	#date
	date=time.strftime('%Y-%m')
	#写入用户列表到文件
	card_dict[cardnum]={'passwd':hashpw,'date':date,'email':dizhi,'cishu':3}

	with open('user.txt','w') as cf:
		json.dump(card_dict,cf)

	with open('eml.txt','w') as f:
		pickle.dump(email_list,f)

	os.mkdir('userdir/%s'%cardnum)
	

	os.system('clear')
	print "您好，%s注册成功，记得给A啊！  ---- 一位不原意透露姓名的郑同学。。。"%cardnum
	

def auth(func):
	"""
	验证函数  装饰器
	"""
	def wapper():
		try:
			#导入列表
			with open('user.txt','r') as cf:
				card_dict=json.load(cf)
		except ValueError:
			os.system('clear')
			print '\033[1;33;40m 无用户来注册一个吧。\n\n。\033[m'
			flag=raw_input('按要求输入代码，1.注册 2.注册 3.注册 其他.退出（你确定放弃注册？）: ')
			if flag=='1' or flag=='2' or flag=='3':
				register()
				return 0
			else:
				os.system('clear')
				print '\033[5;31;40m \n\n\n\t\t\t\t好样的，放学别走。\n\n\n\n \033[0m'
				time.sleep(3)
				return 0
	
		#导入列表		
		if not card_dict:
			with open('user.txt','r') as cf:
				card_dict=json.load(cf)
	
		#用户名认证.
		while True:
			cardnum=passwd_yan()
			if cardnum in card_dict:
				break
			else:
				os.system('clear')
				print "\n\n\t\t\t用户名不存在."
				time.sleep(3)
	
		#密码判断
		while True:
			if  not (card_dict[cardnum]['cishu'] > 0):
				os.system('clear')
				print "\n\n%s密码输入错误超过三次，被锁定。请联系天朝银行SA。。。"%cardnum
				with open('user.txt','w') as cf:
					json.dump(card_dict,cf)
				break
			passwd=getpass.getpass('please input passwd >>>')
			passwd_=getpass.getpass('\nplease input passwd again >>>')
			if passwd==passwd_:
				h=hmac.new('test')
				h.update(passwd)
				hashpw=h.hexdigest()
				if hashpw==card_dict[cardnum]['passwd']:
					card_dict[cardnum]['cishu']=3
					with open('user.txt','w') as cf:
						json.dump(card_dict,cf)
					os.system('clear')
					print "登入成功。\n\n"
					break
				else:
					card_dict[cardnum]['cishu']=card_dict[cardnum]['cishu']-1
					os.system('clear')
					print '密码错误，请重新输入。您还有%s次机会，(神设定不解释)。\n\n'%(card_dict[cardnum]['cishu'])
					with open('user.txt','w') as cf:
						json.dump(card_dict,cf)
			else:
				os.system('clear')
				print "两次输入密码不一致，重新输入。\n\n"
		func(cardnum)
	return wapper


def emailyan():

	'''邮箱验证'''
	
	p=re.compile(r'^[\w\d]+[\d\w\_\.]+@([\d\w]+)\.([\d\w]+)(?:\.[\d\w]+)?$')
		#输入邮箱
	while True:
		os.system('clear')
		s=raw_input('\033[1;31;40mplease input your email: \033[0m')
		s_=raw_input('\nplease input your email again: ')
		m=p.match(s)
		if s==s_:
			if m==None:
				os.system('clear')
				print '您输入的邮箱格式不正确，请重新输入。\n'
				time.sleep(3)
			else:
				break
		else:
			os.system('clear')
			print '\n两次输入邮箱地址不同，请重新输入。\n\n'
			time.sleep(3)
	dizhi=s
	return dizhi

def passwdyan():
	'''验证密码'''
	while True:
		#输入密码
		os.system('clear')
		passwd=getpass.getpass("\n\nPlease input passwd >>>")
		passwd_=getpass.getpass("\nPlease input passwd again >>>")
		if passwd==passwd_:
			if passwd:
				os.system('clear')
				print '密码不能为空，请重新输入。\n\n'
				time.sleep(3)
			break
		else:
			os.system('clear')
			print "两次输入密码结果不同，请重新输入。\n\n"
			time.sleep(3)
			continue
	return passwd

def user_id(**kwargs):
	"""用户名验证"""
	while True:
		os.system('clear')
		cardnum=raw_input('please input your username : ')
		cardnum_=raw_input('please input your username again: ')

		if cardnum==cardnum_: 
			if cardnum in kwargs:
				os.system('clear')
				print "username is exist,please input again !\n\n'"
				time.sleep(3)
			else:
				return cardnum
		else:
			os.system('clear')
			print "用户名不一致，请重新输入。\n\n"
			time.sleep(3)
			
def passwd_yan(): 
	while True:
		cardnum=raw_input('please input your username : ')
		cardnum_=raw_input('please input your username again: ')
		if cardnum==cardnum_: 
				break
		else:
			os.system('clear')
			print "用户名不一致，请重新输入。\n\n"
			time.sleep(3)
	return cardnum


@auth
def kaishi(username):
	'''游戏菜单'''
	while True:
		os.system('clear')
		print "*"*66
		print "\n\t\t\t1.新游戏\n"
		print "\t\t\t2.载入存档\n"
		print "\t\t\t3.注册\n"
		print "\t\t\t0.退出\n"
		print "*"*66
		flag=raw_input('\n\n请选择: ')
		if flag=='1':
			game(username)	
		elif flag=='3':
			register()
		elif flag=='2':
			info=os.popen('ls userdir/%s'%username)
			info=info.read()
			if info:
				info=info.strip()
				info=info.split('\n')
				os.system('clear')
				count=0
				flag_list=[]
				for i in info:
					flag_list.append(count)	
					count+=1
				while True:
					if not info:
						print "\n\n无存档。\n\n"
						time.sleep(3)	
						break
					os.system('clear')
					count=0
					print "%s\n"%('*'*66)
					for i in info:
						print '\t\t\t%s. %s\n'%(count,i)
						count+=1
					count=0
					print "\t\t\tq. 返回登入界面"
					print "\n%s"%('*'*66)
					flag=raw_input('\n\n请选择存档：')
					if flag=='q': 
						os.system('clear')
						kaishi()
					if flag.isdigit():
						if int(flag) in flag_list:
							while True:
								os.system('clear')
								xuanze=raw_input('1.载入此存档 2.删除此存档 0.返 回：')
								if xuanze=='1':
									with open('userdir/%s/%s'%(username,info[int(flag)]),'r') as f:
										obj=pickle.load(f)
									obj.choice()
									os.system('clear')
									print "\n\n爱玩不玩.\n\n"
									time.sleep(3)
									quit()
								elif xuanze=='2':
									os.remove('userdir/%s/%s'%(username,info[int(flag)]))
									num=int(flag)
									info.pop(num)
									print "\n\n删除成功.\n\n"
									break
									time.sleep(3)
								elif xuanze=='0':
									break
						else:
							print "\n存档不存在，请重新选择。\n\n" 
					else:
						os.system('clear')
						print "\n你输入的是啥 重新输。"
						time.sleep(3)
			else:
				os.system('clear')
				print '无存档。'
				time.sleep(3)

		elif flag=='0':
			os.system('clear')
			print "\n\n\t\t\t爱玩不玩。"
			time.sleep(3)
			quit()

def ks():
	'''登入界面 入口函数'''
	while True:
		os.system('clear')
		print "-"*66
		print "\n\n\t\t\t1.登 入\n"  
		print "\t\t\t2.注册新用户\n"
		print "\t\t\t3.退 出\n"
		print "-"*66
		flag=raw_input('\n\n请选择：')
		if flag=='1':
			os.system('clear')
			kaishi()
		elif flag=='2':
			os.system('clear')
			register()
			time.sleep(3)
		elif flag=='3':
			os.system('clear')
			print "\n\n\t\t\t爱玩不玩。"
			time.sleep(3)
			quit()
		else:
			os.system('clear')
			print "\n\n你输的啥，重新输。"
			time.sleep(3)
