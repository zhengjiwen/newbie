#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-16 13:01:56
# author: 郑集文
# Description:
import os
from module import card

if __name__ == '__main__':
	pass
os.system('clear')
print '''\n\n\t\t---------------------------------
	
			0.查询。

			1.提现。

			2.注册。

			3.还款。

			4.转账。

			110.退出

		---------------------------------
	'''
flag=raw_input('请按提示输入命令代号：')
#查询
if flag=='0':
	card.select()
#提现
elif flag=='1':
	card.tixian()
#注册
elif flag=='2':
	card.register()
#还款
elif flag=='3':
	card.chongzhi()
#转账
elif flag=='4':
	card.zhuanzhang()
#退出
elif flag=='110':
	os.system('clear')
	print "\n\n\t\t\t\t\t再见。\n\n"
	exit(0)
