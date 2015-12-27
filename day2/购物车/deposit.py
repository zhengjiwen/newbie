#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-03 09:58:36
# author: 郑集文
# Description: deposit
import shop,os
shop=shop.shop()
#判断用户名
while True:
    user_name=raw_input("\nPlease input you name:")
    file_name=user_name+'.txt'
    if os.path.exists(file_name):
        break	
    else:
        print "\n未找到此用户名请重新输入."
	
#主程序 
deposit_judge=raw_input("\nDo you need to recharge [y/n]?")
if deposit_judge=='y':
    deposit_num=raw_input("\nPlease input your want to deposit money:")
    if deposit_num.isdigit:
        deposit=shop.deposit(deposit_num,user_name)
        while True:
            deposit_judge_1=raw_input('\n充值成功，现在余额为%s，是否继续充值[y/n]?'%shop.user(user_name)[user_name])
            if deposit_judge_1=='y':
                deposit_num=raw_input("\nPlease input your want to deposit money:")
                if deposit_num.isdigit:
                    deposit=shop.deposit(deposit_num,user_name)
                else:
                    print "\n请输入正整数\n。"
            elif deposit_judge_1=='n':
                break
            else:
                print "输入错误请重新输入。"
elif deposit_judge=='n':
    print '\nGo out! You are a ugly and poor man!'
