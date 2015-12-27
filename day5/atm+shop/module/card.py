#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-16 09:11:20
# author: 郑集文
# Description:
import json,hmac,time,random,re,os,getpass
import code
import ConfigParser

#注册函数
def register():
	"""我是注释"""
	
	#导入字典
	try:
		with open('card.txt','r') as cf:
			card_dict=json.load(cf)
	except ValueError:
		card_dict={}

	#邮箱验证
	p=re.compile(r'^[\w\d]+[\d\w\_\.]+@([\d\w]+)\.([\d\w]+)(?:\.[\d\w]+)?$')
	while True:
		#输入邮箱
		while True:
			s=raw_input('\033[1;31;40mplease input your email: \033[0m')
			os.system('clear')
			s_=raw_input('please input your email again: ')
			if s==s_:
				break
			else:
				os.system('clear')
				print '\n两次输入邮箱地址不同，请重新输入。\n\n'
		if s in card_dict.keys():
			os.system('clear')
			print "邮箱已绑定，请更换邮箱。\n\n"
			continue
		m=p.match(s)
		if m==None:
			os.system('clear')
			print '您输入的邮箱格式不正确，请重新输入。\n'
		else:
			os.system('clear')
			print "验证码已送到%s，请注意查收。\n\n"%s
			break

	idcode=code.yanzhengma(s)

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


	#创建账单
	form(dizhi,date)
		
		

	#写入用户列表到文件
	card_dict[dizhi]={'passwd':hashpw,'balance':15000,'date':date,'email':dizhi,'cishu':3}

	with open('card.txt','w') as cf:
		json.dump(card_dict,cf)


	os.system('clear')
	print "您好，邮箱%s已绑定成功，记得给好评啊！  ---- 一位不原意透露姓名的郑同学。。。"%s





#验证函数	
def auth(func):
	"""
	我是注释
	"""
	def wapper():
		try:
			#导入列表
			with open('card.txt','r') as cf:
				card_dict=json.load(cf)
		except ValueError:
			os.system('clear')
			print '\033[1;33;40m  我累个去，天朝银行这么diao居然没有用户。少年我你骨骼精奇，是万中无一的武学奇才，维护世界和平就靠你了。来天朝银行注册个用户吧 I want to you 思密达\n\n。\033[m'
			flag=raw_input('按要求输入代码，1.注册 2.注册 3.注册 其他.退出（你确定放弃注册？）: ')
			if flag=='1' or flag=='2' or flag=='3':
				register()
				return 0
			else:
				os.system('clear')
				print '\033[5;31;40m \n\n\n\t\t\t\t好样的，放学别走。\n\n\n\n \033[0m'
				return 0
	
		#导入列表		
		if not card_dict:
			with open('card.txt','r') as cf:
				card_dict=json.load(cf)
	
		#输入邮箱
	
		while True:
			dizhi=emailyan()
			if dizhi in card_dict.keys():
				break
	
		#密码判断
		while True:
			if  not (card_dict[dizhi]['cishu'] > 0):
				os.system('clear')
				print "\n\n%s密码输入错误超过三次，被锁定。请联系天朝银行SA。。。"%dizhi
				with open('card.txt','w') as cf:
					json.dump(card_dict,cf)
				break
			passwd=getpass.getpass('please input passwd >>>')
			passwd_=getpass.getpass('\nplease input passwd again >>>')
			if passwd==passwd_:
				h=hmac.new('test')
				h.update(passwd)
				hashpw=h.hexdigest()
				if hashpw==card_dict[dizhi]['passwd']:
					card_dict[dizhi]['cishu']=3
					with open('card.txt','w') as cf:
						json.dump(card_dict,cf)
					os.system('clear')
					print "登入成功。\n\n"
					break
				else:
					card_dict[dizhi]['cishu']=card_dict[dizhi]['cishu']-1
					os.system('clear')
					print '密码错误，请重新输入。您还有%s次机会，(神设定不解释)。\n\n'%(card_dict[dizhi]['cishu'])
					with open('card.txt','w') as cf:
						json.dump(card_dict,cf)
			else:
				os.system('clear')
				print "两次输入密码不一致，重新输入。\n\n"
	
		func(dizhi)

	return wapper
		

#充值函数
@auth
def chongzhi(dizhi):
	"""
	我是注释
	"""
	with open('card.txt','r') as cf:
		card_dict=json.load(cf)
	balance=card_dict[dizhi]['balance']
	os.system('clear')
	money=int(raw_input('请输入要充值的金额：'))
	money_=(money+balance)
	card_dict[dizhi]['balance']=money_
	with open('card.txt','w') as cf:
		json.dump(card_dict,cf)
	os.system('clear')
	print "%s充值成功,余额为%s。"%(dizhi,money_)

	lei='chongzhi'
	form_add(dizhi,money,lei)


#录入邮箱
def emailyan():
	p=re.compile(r'^[\w\d]+[\d\w\_\.]+@([\d\w]+)\.([\d\w]+)(?:\.[\d\w]+)?$')
		#输入邮箱
	while True:
		s=raw_input('\033[1;31;40mplease input your email: \033[0m')
		s_=raw_input('\nplease input your email again: ')
		m=p.match(s)
		if s==s_:
			if m==None:
				os.system('clear')
				print '您输入的邮箱格式不正确，请重新输入。\n'
			else:
				break
		else:
			os.system('clear')
			print '\n两次输入邮箱地址不同，请重新输入。\n\n'
	dizhi=s
	return dizhi


def passwdyan():
	while True:
		#输入密码
		passwd=getpass.getpass("\n\nPlease input passwd >>>")
		passwd_=getpass.getpass("\nPlease input passwd again >>>")
		if passwd==passwd_:
			if passwd:
				os.system('clear')
				print '密码不能为空，请重新输入。\n\n'
			break
		else:
			os.system('clear')
			print "两次输入密码结果不同，请重新输入。\n\n"
			continue
	return passwd


#提现函数
@auth
def tixian(dizhi):
	with open('card.txt','r') as cf:
		card_dict=json.load(cf)
	balance=card_dict[dizhi]['balance']
	os.system('clear')
	try:
		money=int(raw_input('请输入要提现的金额：'))
	except ValueError:
		os.system('clear')
		print "\n请输入数字。\n\n"
	shouxu='%0.2f'%(money*0.05)
	money_=(balance-money-float(shouxu))
	if float(money_) < 0 :
		os.system('clear')
		print "额度不足，请充值。"
	else:
		lei='tixian'
		form_add(dizhi,money,lei)
		card_dict[dizhi]['balance']=money_
		with open('card.txt','w') as cf:
			json.dump(card_dict,cf)
		os.system('clear')
		print "%s提现成功,余额为%s。"%(dizhi,money_)


#查询函数
@auth
def select(dizhi):
	with open('card.txt','r') as cf:
		card_dict=json.load(cf)
	balance=card_dict[dizhi]['balance']
	os.system('clear')
	print "\n%s的剩余额度为%s元。\n\n"%(dizhi,balance)
	nowtime=time.strftime('%Y-%m')
	with open('duizhangdan/%s.txt'%dizhi,'r') as f:
		flag=False
		print "\n\n您目前的账单记录如下：\n\n"
		for i in f:
			if '[' in i:
				if nowtime in i:
					flag=True
				else:
					flag=False
			if flag:
				print i,




#支付
def zhifu(dizhi,money):

	with open('card.txt','r') as cf:
		card_dict=json.load(cf)
	balance=card_dict[dizhi]['balance']
	money_=(balance-money)
	if int(money_) < 0 :
		os.system('clear')
		print "额度不足，请充值。\n\n"
		return 0
	else:

		lei='zhifu'
		
		form_add(dizhi,money,lei)

		card_dict[dizhi]['balance']=money_
		with open('card.txt','w') as cf:
			json.dump(card_dict,cf)

		return card_dict
	

#转账函数
@auth
def zhuanzhang(dizhi):

	with open('card.txt','r') as cf:
		card_dict=json.load(cf)

	while True:
		zhuan=raw_input("\n请输入转账邮箱：")
		zhuan_=raw_input("\n再次输入转账邮箱：")
		if zhuan==zhuan_:
			break
		else:
			os.system('clear')
			print "两次输入邮箱不一致，请重新输入。\n\n"

	while True:
		if zhuan in card_dict:
			break
		else:
			os.system('clear')
			print "天朝银行无此用户，暂不支持跨行转账（转账都不要手续费了，贱民门还想跨行转账？）\n\n"

	money=int(raw_input("请输入转账金额："))

	card_dict_=zhifu(dizhi,money)
	if card_dict_:
		lei='zhuanzhang'

		form_add(zhuan,money,lei)

		balance=card_dict_[zhuan]['balance']
		money_=(money+balance)
		card_dict_[zhuan]['balance']=money_
		with open('card.txt','w') as cf:
			json.dump(card_dict_,cf)
		os.system('clear')
		print "转账成功。\n\n"
		return 0



#添加账单
def form(dizhi,dt):
	os.system('touch duizhangdan/%s.txt'%dizhi)
	date_list=dt.split('-')
	config = ConfigParser.ConfigParser()
	config.read('duizhangdan/%s.txt'%dizhi)
	for i in range(int(date_list[1]),13):
		config.add_section('%s-%s'%(date_list[0],i))
	config.write(open('duizhangdan/%s.txt'%dizhi,'w'))


#插入账单
def form_add(dizhi,num,lei):
	date=time.strftime('%Y-%m')
	date2=time.strftime('%H/%M/%S')
	config = ConfigParser.ConfigParser()
	config.read('duizhangdan/%s.txt'%dizhi)
	config.set(date,"%s_%s"%(date2,lei),int(num))
	config.write(open('duizhangdan/%s.txt'%dizhi,"w"))



