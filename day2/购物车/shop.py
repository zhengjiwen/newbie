#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-02 19:12:18
# author: 郑集文
# Description: shop module

class shop():
    def __init__(shop):
        pass

    def user(shop,user):
        f=file('%s.txt'%user,'r+')
        user_a=f.readline()
        user_dict={}
        f.close()
        user_b=user_a.strip()
        user_c=user_b.split()
        user_dict[user_c[0]]=user_c[1]
        return user_dict


    def deposit(shop,dep,user):
        deposit=dep
        deposit_dict={}
        f=file('%s.txt'%user,'r+')
        deposit_a=f.readline()
        f.close()
        if deposit_a == '':
            deposit='none'
        else:
            deposit_b=deposit_a.strip()
            deposit_c=deposit_b.split()
            deposit=int(deposit)+int(deposit_c[1])
            deposit="%d"%deposit
            deposit_dict[deposit_c[0]]=deposit
            f.close()
        f=file('%s.txt'%user,'w+')
        f.write('%s %s'%(deposit_c[0],deposit))
        f.close()
        return deposit_dict
    
    
    def pay(shop,pay,user):
        pay=pay
        pay_dict={}
        f=file('%s.txt'%user,'r+')
        pay_a=f.readline()
        f.close()
        pay_b=pay_a.strip()
        pay_c=pay_b.split()
        pay=int(pay_c[1])-int(pay)
        pay="%d"%pay
        pay_dict[pay_c[0]]=pay_c[1]
        f.close()
        f=file('%s.txt'%user,'w+')
        f.write('%s %s'%(pay_c[0],pay))
        f.close()
        return pay
    
    
    def commodity(shop):
        commodity_dict={}
        commodity_f = file('commodity.list','r+')
        while True:
            commodity_c=commodity_f.readline()
            if commodity_c=='':
                commodity_f.close()
                break
            else:
                commodity_a=commodity_c.strip()
                commodity_b=commodity_a.split()
                commodity_dict[commodity_b[0]]=commodity_b[1]
        return commodity_dict
    
