day5 atm+购物车+账单
author 郑集文

#需在linux系统下执行
#绑定邮箱时向邮箱发送随机6位验证码。
#银行帐号为绑定邮箱地址。
#邮箱验证：支持邮箱格式验证。密码验证：密码为空报错。不能超三次错误，输入密码正确后清零，错误超三次后邮箱被锁定。
#商品列表在shangpin.txt
#对账单在duizhangdan目录下。

#atm
1.执行python main.py

#添加商品
1.执行python addshangpin.py

#shop
1.执行python shop.py



#在定时任务中加入
* * * 1-12 * python fazhangdan.py #每月账单
* * 28 12 * python addform.py	   #新增次年账单
