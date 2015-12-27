#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-04 17:43:00
# author: 郑集文
# Description: find,add,delet file

if __name__=='__main__':
	pass

import os,func,json

#main
while True:

	print '''
	-----------------------------\n
		1、获取ha记录

		2、增加ha记录

		3、删除ha记录

		4、回滚

		5、备份

		0、退出
	-----------------------------\n'''

	num=raw_input("\n请输入命令序号: ")
	
	#file_path=raw_input('请输入文件路径：')

#查找
	if num=='1':
		find_content=raw_input("\n请输入backend 例'www.oldboy.org'： ")
		find_list=func.find(find_content)
		find_list.pop(1)
		if len(find_list)==0 :
			os.system('clear')
			print "未找到结果:"
			continue
		os.system('clear')
		print '%sbackend:%s%s'%('*'*33,find_content,'*'*33)
		for i in range(len(find_list)):
			content=find_list[i]
			content=content.strip()
			print '%s\n'%content,
		print '\n%s\n\n'%('*'*66)

#add		
	elif num=='2':
		print '\n如{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}} 注意要用双引号。'
		read=raw_input('\n请按格式输入要添加的记录：')
		read_dict=json.loads(read)
		#func.add(read,file_path)
		cunzai=func.add(read_dict)
		if cunzai > 0:
			os.system('clear')
			print "\n\n添加失败，内容已经存在。\n\n"
		else:
			os.system('clear')
			print "\n\nserver 添加成功。\n\n"

#delete
	elif num=='3':
		print '\n如{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}} 注意要用双引号。'
		read=raw_input('\n请按提示格式输入要删除的记录：')
		read_dict=json.loads(read)
		line_num=func.delete(read_dict)
		if line_num==0:
			os.system('clear')
			print "\n\n未找到此backend，删除失败。\n\n"
		elif line_num>0:
			os.system('clear')
			print "\n\nserver，删除成功。\n\n"
			

#quit
	elif num=='0':
		os.system('clear')
		break

#rollback
	elif num=='4':
		if os.path.exists('conf.txt.bak'):
			func.rollback()
			os.system('clear')
			print "\n\n\t回滚成功。\n\n"
		else:
			os.system('clear')
			print "\n\n无备份文件，回滚失败,请执行备份命令备份文件。\n\n"
#backup
	elif num=='5':
		func.backup()
		os.system('clear')
		print "\n\n备份成功。\n\n"

#errors
	else:
		os.system('clear')
		print '请输入正确序号。'
	
