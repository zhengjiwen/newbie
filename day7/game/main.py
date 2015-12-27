#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-20 04:34:45
# author: 郑集文
# Description:
import pickle,random,time,datetime
import os,code,json,getpass,re,hashlib

class game(object):


	'''Create a caracter.'''	
	def __init__(self,un,occupation=['newbee',],gold=1500):
		self.acm=[]
		os.system('clear')
		self.username=un
		name=raw_input('请输入name：')
		self.name=name
		sex=raw_input("\n\n请选择角色sex 1.man 2.woman: ")
		if sex=='1':
			sex='man'
		elif sex=='2':
			sex='woman'
		self.sex=sex
		self.occupation=occupation
		self.gold=gold
		self.month=200
		self.value=10000
		self.story()
		self.choice()

	@staticmethod
	def end():
		'''片尾字幕'''
		with open('end.txt','r') as f:
			os.system('clear')
			for word in f:
				word=word.strip()
				print "%s\n"%word
				time.sleep(3)

	def achievement(self):
		'''成就栏'''
		os.system('clear')
		print "\n\n\t\t\t-*-成就栏-*-\n"
		if self.acm:
			for i in self.acm:
				print "\t\t\t%s\n"%i
		else:
			print '\t\t\t无成就.'
		
	@staticmethod
	def story():
		"""序章"""
		with open('story.txt','r') as f:
			os.system('clear')
			for word in f:
				word=word.strip()
				print "%s\n"%word
				time.sleep(3)
	

	def status(self):
		'''状态栏'''
		os.system('clear')
		print """
 +++++++++++++++++++++++++++++++
- 当前状态：
- Name：%s
- value: %s
- money：%s
- sex: %s
- remainder time：%s months
 +++++++++++++++++++++++++++++++
			"""%(self.name,self.value,self.gold,self.sex,self.month)


	@staticmethod
	def task():
		'''任务栏'''
		os.system('clear')
		print "\t\t\t-*-任务栏-*-"
		print "\n\n任务：在200个月内资产达到1000W。"


	def choice(self):
		'''菜单'''
		self.status()	
		print """
1.spend time\n\n2.学习技能\n\n3.任务\n\n4.保存\n\n5.退出\n\n6.抽奖\n\n7.成就\n
"""
		flag=raw_input("\n请选择: ")
		#over
		if flag=='1':
			self.over()
			self.choice()
		#achievement
		if flag=='7':
			while True:
				os.system('clear')
				self.achievement()
				flag=raw_input('\n\n输入q返回：')
				if flag=='q':
					break
			self.choice()

		#learn
		elif flag=='2':
			self.learn()	
			self.choice()
		#task
		elif flag=='3':
			game.task()
			while True:
				flag=raw_input('\n\n输入q返回：')
				if flag=='q':
					break
			self.choice()

		#quit&save
		elif flag=='4':
			self.quit_save(self.username)
			os.system("clear")
			print "\n\n\t\t\t保存成功。\n\n"
			time.sleep(3)
			self.choice()

		#quit
		elif flag=='5':
			os.system('clear')
			print "\n\n\t\t\t爱玩不玩。"
			time.sleep(3)
			quit()

		#赌博
		elif flag=='6':
			while True:
				a=raw_input("请选择 1.抽奖 2.退出 ：")
				if a=='1':
					qian=foo(self.gold)
					if qian>0:
						if '赌神' not in self.acm:
							self.acm.append('赌神')
					self.gold+=qian
					self.choice()

				elif a=='2':
					self.choice()


	def over(self):
		'''spend time'''

		while True:
			while True:
				os.system('clear')
				a=raw_input('是否穿越 y or n：')
				if a=='y':
					break
				elif a=='n':
					self.choice()
			num_in=int(raw_input("请输入穿越月数："))
			if num_in>self.month:
				os.system('clear')
				print '\n\n留给中国队的时间不够了。'
				time.sleep(3)
			else:
				break
		dian=''
		num=num_in
		while True:
			os.system('clear')
			num-=1
			if num==-1:
				break
			dian+='.'
			if dian=='....':
				dian='.'
			print "穿越中%s\n"%dian,"离穿越结束还有%s个月"%num
			time.sleep(1)
		money=num_in*self.value
		self.gold=int(self.gold)+money
		self.month=self.month-num_in
		print "穿越完成，共收入%s元"%money
		if self.month==0:
			if self.gold>10000000:
				os.system('clear')
				print "you are win. \n\n\t\t\t获得成就:逆 袭"
				if '逆 袭' not in self.acm:
					self.acm.append('逆 袭')
				self.end()	
			else:
				os.system('clear')
				print "you are false\n\n获得成就:失败者\n\n\t\t\t爱玩不玩."
				if '失败者' not in self.acm:
					self.acm.append('失败者')
				time.sleep(3)
				self.end()	

	def learn(self):
		'''技能函数'''
		
		os.system('clear')
		print "\n\t\t\t1.python\n"
		print "\n\t\t\t2.Englishi\n"
		print "学习技能需要耗费36个月。"
		while True:
			a=raw_input("是否学习 y or n: ")	
			if a=='y':
				break
			elif a=="n":
				self.choice()
		flag=raw_input("\n\n请输入你选择学习的技能：")
		if flag=='1':
			if 'python' in self.occupation:
				os.system('clear')
				print "技能python已经学习，请学习其他技能。"
				time.sleep(3)
			else:
				os.system('clear')
				self.value+=10000
				self.occupation.append('python')
				count=0
				idian=''
				while True:
					os.system('clear')
					idian+='.'
					if idian=='....':
						idian='.'
					if count==12:	
						break
					count+=1
					print "\n\n\t\tpython 学习中%s"%idian
					time.sleep(1)
				self.month=self.month-36
				print "新技能get。 value+10000 获得成就：python攻城狮。"
				self.acm.append('python攻城狮')
				time.sleep(3)

		if flag=='2':
			if 'Englishi' in self.occupation:
				os.system('clear')
				print "技能Englishi已经学习，请学习其他技能。"
				time.sleep(3)
			else:
				count=0
				idian=''
				while True:
					os.system('clear')
					idian+='.'
					if idian=='....':
						idian='.'
					if count==12:	
						break
					count+=1
					print "\n\n\t\tEnglishi 学习中%s"%idian
					time.sleep(1)
				self.occupation.append('Englishi')
				os.system('clear')
				self.value+=10000
				print "新技能get。 value+10000 获得成就：高逼格。"
				self.month=self.month-36
				self.acm.append('高逼格')
				time.sleep(3)


	def quit_save(self,username):
		'''保存'''
		riqi=time.strftime('%Y.%m.%d_%H:%M:%S')
		with open('userdir/%s/%s_%s.txt'%(username,riqi,self.name),'w') as f:
			pickle.dump(self,f)
			


def wrapper(func):
	def result():
		dice1=random.randint(1,6)
		dice2=random.randint(1,6)
		dice3=random.randint(1,6)
		ret_list=[]
		ret_list.append(dice1)
		ret_list.append(dice2)
		ret_list.append(dice3)
		num=func(ret_list)
		return num
	return result
 
def dubo(func):
	'''掷骰子'''
	def test(money):
		while True:
			ret='1'
			if ret == '1':
				while True:
					os.system('clear')
					print "\n猜中金额X10倍，否则不返回。\n\n"
					while True:
						os.system('clear')
						a=raw_input('是否退出 y or n: ')
						if a=='y':
							return 0
						elif a=='n':
							break
					jine=int(raw_input('请输入下注金额: '))
					if jine==0:
						os.system('clear')
						print('\n有意思吗。。。\n')
						time.sleep(3)
					elif jine>int(money):
						os.system('clear')
						print('\n带够钱了吗。	\n\n')
						time.sleep(3)
					elif jine<0:
						os.system('clear')
						print('\n\n你还想贷款？\n\n')
						time.sleep(3)
					else:
						break
					
				rets=func()
				print "规则每次投掷三个骰子，猜出点数 三种情况 1.豹子：三个骰子点数相同 例：222 111 333 2.顺子： 三个骰子点数是连数 例：123 234 3.其他可能 例子：1，3，4  5，3，1.\n\n 所猜点数为豹子输入1  顺子输入数字2   其他情况输入三位数字。例：233"
				flag=raw_input("\n\n按提示输入 ：")
				if  flag=='1':
					if rets==1:
						print "Oh no you are win"
						zhuan=jine*10
						time.sleep(3)
						return zhuan
					else:
						print "Yes you are a loser"
						jine=-jine
						time.sleep(3)
						return jine
				elif flag=='2':
					if rets==2:
						print "Oh no you are win"
						zhuan=10*jine
						time.sleep(3)
						return zhuan
					else:
						print "Yes you are a loser"
						jine=-jine
						time.sleep(3)
						return jine
				else:
					list_num=[]
					for i in flag:
						list_num.append(int(i))
					if list_num == rets:
						print "Oh no you are win"
						zhuan=10*jine
						time.sleep(3)
						return zhuan
					else:
						print "Yes you are a loser"
						jine=-jine
						time.sleep(3)
						return jine

	return test

@dubo
@wrapper
def foo(ret_list):
	ret_list.sort()
	shunzi=[[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
	baozi=[[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6]]
	if ret_list in shunzi:
		return 1
	elif ret_list in baozi:
		return 2
	else:
		return ret_list
