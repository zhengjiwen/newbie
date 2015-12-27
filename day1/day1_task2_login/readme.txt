day1作业二 ：登入接口 操作手册

本程序因调用os.system模块，需在linux下执行###
支持多用户，检测用户存在，容错次数显示
如用户被禁用需将'用户名'.list中 第三个字段改为0。
或执行resetting.sh脚本
例: cat zjw.list
zjw 123 2 <== 将2改为0即可正常登入。	


1.执行程序
chmod 755 login.py 
./login.py

2.根据提示输入用户名密码   username=zjw password=123 
3.用户名密码在 '用户名'.list 文件中定义。

