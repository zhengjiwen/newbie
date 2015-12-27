#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-03 02:54:07
# author: 郑集文
# Description: 购物车

from shop import shop
import os
#定义方法
shop=shop()

#初始化列表
car_list=[]
car_dict={}

os.system('clear')
print "\nWelcome my shop!\n" 
user_name=raw_input("Please input your name:")

#判断用户名
while True:
    try:
        balance=int(shop.user(user_name)[user_name])
        break
    except IOError,e:
        user_name=raw_input("\n无此用户请重新输入:")

print "\n\n您的余额为%d\n\n"%balance


#主程序
while True:
    balance=int(shop.user(user_name)[user_name])
    if balance>0:
    #商品列表
        commodity_dict=shop.commodity()
    
        border_commodity='Products List'
        border_down="-"*66
        border_commodity=border_commodity.center(66,"-")

        #商品字典
        for k in commodity_dict:
            car_dict[k]=0

        #购买程序
        while True:
            print border_commodity
            count=0
            for k in commodity_dict:
                count+=1
                if count>4:
                    print "\n"
                    count=0
                print "%s:%s   "%(k,commodity_dict[k]),
            print "\n%s"%border_down
            commodity=raw_input("Please input you want to buy '结算输入'b''退出'q':")
            if commodity in commodity_dict:
                car_list.append(commodity)
                os.system('clear')
                print '\n%s已加入购物车。\n'%commodity
                car_dict[commodity]=car_dict[commodity]+1
            elif commodity=='b':
                break
            elif commodity=='q':
                exit()
            else:
                print "\n未找到此商品请重新输入\n"
                print border_commodity
                count=0
                for k in commodity_dict:
                    count+=1
                    if count>4:
                        print "\n"
                        count=0
                    print "%s:%s   "%(k,commodity_dict[k]),
                print "\n%s"%border_down
                
        car_list=list(set(car_list))
        paymoney=0
        print "\n-------------购物车列表------------\n"
        for v in car_list:
            print v,car_dict[v],
            paymoney+=int(car_dict[v])*int(commodity_dict[v])
        print "\n\n------------------------------------\n"
        pay_judge=raw_input("确认购买[y/n]")
        if pay_judge=='y':
            balance=int(shop.user(user_name)[user_name])
            if balance>paymoney:
                pay=shop.pay(paymoney,user_name)
                print "\n购买成功总共花费%d"%paymoney
                print "\n余额为%s"%pay
                exit()
            elif balance<paymoney:
                print "余额不足,请充值。"
                exit()
        elif pay_judge=='n':
            print "\n不买东西还来 放学别走！"
            break

#充值程序    
    else:
        deposit_judge=raw_input("\nYour balance is insufficient! Do you need to recharge [y/n]?")
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
            break
