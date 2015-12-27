#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-04 18:13:03
# author: 郑集文
# Description: module

#find
def find(find_content,file_path='conf.txt'):

	#遍历查找
	with open(file_path,'r+U') as f:
		find_list=[]
		while True:
			try:
				content=f.next()
				if (find_content in content and 
					'backend' in content):
					break
			except StopIteration,e:
				break

		#将查找结果加入到列表
		while True:
			try:
				content=f.next()
				content=content.strip()
				find_list.append(content)
			except StopIteration,e:
				break
		return find_list

#rollback
def rollback(file_path='conf.txt'):
	with open('%s.bak'%file_path,'r+') as f,open(file_path,'w+') as f_b:
		while True:
			try:
				line=f.next()
				f_b.write(line)
			except StopIteration,e:
				break

#添加
def add(read_dict,file_path='conf.txt'):
	#输入内容格式化处理
	list_record=[]
	backend_name="%s %s"%('backend',read_dict['backend'])
	for i in read_dict['record'].keys():
		list_record.insert(0,"%s %s"%(i,read_dict['record'][i]))
	kong=' '
	record=kong.join(list_record)
	#backup
	with open(file_path,'r+') as f,open('conf.txt.bak','w') as f_b:
		line_num=0
		while True:
			try:
				line=f.next()
				if ('backend' in line and
					read_dict['backend'] in line):
					line_num=f.tell()
				f_b.write(line)
			except StopIteration,e:
				break
	
	#导入配置文件到列表
		if line_num!=0:
			global cunzai
			index=0
			with open(file_path,'r+') as f:
				line=f.readlines() #line是列表
				for i in range(len(line)):
					if backend_name in line[i]:
						index=i
				cunzai=0
				count=0
				
				#backend，server下标
				while True:
					count+=1
					try:
						if ('\t' not in line[index+count] and
							line[index+count].strip() != ''):
							break
						elif record in line[index+count]:
							cunzai+=1
					except IndexError,e:
						break
	
				#判断backend，server是否已存在。
				if cunzai==0:
					line.insert(index+1,'\t%s\n'%record)
					with open(file_path,'w+') as f:
						for i in line:
							f.write(i)
	
		#判断如果backend不存在。
		else:
			cunzai=0
			with open(file_path,'a+') as f:
				f.write("%s\n"%backend_name)
				f.write('\t%s\n'%record)
	return cunzai 

#备份
def backup(file_path='conf.txt'):
	with open(file_path,'r+') as f,open('conf.txt.bak','w') as f_b:
		while True:
			try:
				line=f.next()
				f_b.write(line)
			except StopIteration,e:
				break


#删除
def delete(read_dict,file_path='conf.txt'):

	#输入格式化处理
	list_record=[]
	backend_name="%s %s"%('backend',read_dict['backend'])
	for i in read_dict['record'].keys():
		list_record.insert(0,"%s %s"%(i,read_dict['record'][i]))
	kong=' '
	record=kong.join(list_record)
	
	#文件备份
	with open(file_path,'r+') as f,open('conf.txt.bak','w') as f_b:
		line_num=0
		while True:
			try:
				line=f.next()
				if ('backend' in line and 
					read_dict['backend'] in line):
					line_num=f.tell()
				f_b.write(line)
			except StopIteration,e:
				break

	#判断backend是否存在
	if line_num!=0:
		global over_index
		index=0	 

		#导入配置文件生成列表
		with open(file_path,'r+') as f:
			line=f.readlines() #line是列表
			for i in range(len(line)):
				if backend_name in line[i]:
					index=i
			cunzai=0
			count=0

			#查找backend下标
			while True:
				count+=1
				try:
					if ('\t' not in line[index+count] and 
						line[index+count].strip() != ''):
						over_index=int(index+count-1)
						break
					elif record in line[index+count]:
						cunzai=int(index+count)
				except IndexError,e:
					over_index=int(index+count-1)
					break

			#删除处理
			if cunzai > 0:
				line.pop(cunzai)
			elif cunzai == 0:
				if index==over_index:
					line.pop(index)

			#最终结果写入配置文件
			with open(file_path,'w+') as f:
				for i in line:
					f.write(i)
	return line_num


def find(find_content,file_path='conf.txt'):
	list_record=[]
	file_path='conf.txt'
	with open(file_path,'r+') as f:
		line_num=0
		while True:
			try:
				line=f.next()
				if ('backend' in line and 
					find_content in line):
					line_num=f.tell()
			except StopIteration,e:
				break
	find_list=[]
	if line_num!=0:
			global over_index
			index=0  
	
			#导入配置文件生成列表
			with open(file_path,'r+') as f:
				line=f.readlines() #line是列表
				for i in range(len(line)):
					if (find_content in line[i] and
						'backend' in line[i]):
						index=i
	
				count=0
				#查找backend下标
				while True:
					count+=1
					try:
						if ('\t' not in line[index+count] and 
							line[index+count].strip() != ''):
							over_index=int(index+count-1)
							break
					except IndexError,e:
						over_index=int(index+count-1)
						break
	
				if index == over_index:
					pass
				else:
					for i in range(index-1,over_index+1):
						find_list.append(line[i])
	return find_list
