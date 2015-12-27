#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-10-21 21:38:00
# author: 郑集文
# menu program
import time,os

#城市列表文件导入
cf=file('city.list','r+')


city=0

#城市列表定义
citylist=[]


#城市列表导入
while city != '':
        city=cf.readline()
        b=city.strip()
        citylist.append(b)
cf.close()
citylist.pop()


#城市菜单循环
while True:
    zidian={}
    #城市列表输出
    print """####################城市列表##########################
        """
    for i in range(len(citylist)):
        print '(%d)'%i,citylist[i].strip(),'  ',
	zidian[i]=citylist[i]
	if i%4 == 0 :
		print '\n'
    print """\n###############################################"""


    #采集城市选择结果
    cityname=raw_input("请输入您想进入城市代号（如 '(0)==beijing'） 退出请输入'quit':")
    int_cityname='a'
    try:
        int_cityname=int(cityname)
    except ValueError:
        pass


    #城市选择判断
    if type(int_cityname)==int and int_cityname in zidian :
        woqule=zidian[int_cityname]
        zf=file('zone/%s.list'%woqule,'r+')
        zone=0
        zonelist=[]
        while zone != '':
            zone=zf.readline()
            b=zone.strip()
            zonelist.append(b)
        zonelist.pop()
        zf.close()


        #区域菜单循环
        while True:
            #输出区域列表
            print """_______________________________________________
                -------------------区域列表-------------------------"""
            for i in range(len(zonelist)):
                print zonelist[i].strip(),
            print """\n---------------------------------------------"""

            #采集区域选择结果
            zonename=raw_input("请输入您想进入的区域名 (返回输入'back')：")

            #学校列表导入
            if zonename in zonelist :
                sf=file('school/%s.list'%zonename,'r+')
                school=0
                schoollist=[]
                while school != '': 
                    school=sf.readline()
                    b=school.strip()
                    schoollist.append(b)
                schoollist.pop()
                sf.close()

                #学校菜单循环
                while True:
                    #学校列表输出
                    print """+++++++++++++++++++++++++++++++++++++++++
                        +++++++++++++++++++学校列表+++++++++++++++"""
                    for i in range(len(schoollist)):
                        print schoollist[i].strip(),
                    print """\n+++++++++++++++++++++++++++++++++++++++++++++++++++"""
                    
                    #学习选择结果采集
                    schoolname=raw_input("请输入您想进入的学校（如五道口男子职业技术学院）返回输入'back'：")
                    if schoolname in schoollist :
			os.system('clear')
                        print """\n\n欢迎来到%s\n\n"""%schoolname

            #程序结束选择结果采集
			while True:
				choose=raw_input("返回上级菜单输入'back',退出输入'quit'")
				if choose == 'back':
					break	
				elif choose == 'quit':
					exit()
				else:
					os.system('clear')
					print "       \n\n命令'%s'识别失败请重新输入。\n\n"%choose

                    #学校判断
                    elif schoolname == 'back':
                        break

                    elif schoolname not in schoollist :
		    	os.system('clear')
                        print "                 \n\n未找到%s              \n\n"%schoolname

            #区域判断
            elif zonename == 'back':
                break
            
            elif zonename not in zonelist:
    		os.system('clear')
                print "                  \n\n未找到'%s'请重新输入\n\n           "%zonename   

#城市判断
    elif cityname=='quit' :
        break    

    elif int_cityname == 'a':
        os.system('clear')
        print "                    \n\n未找到'%s'请重新输入。\n\n                   "%cityname	
