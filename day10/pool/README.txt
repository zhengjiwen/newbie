作业：一个线程池

测试demo使用
python bin/start.py

######################
ps.使用线程池的函数必须加入一个self参数并在结尾加上如下两行代码
例：
def test(self,):
	self.q.put_nowait(1)
	print "要什么自行车."
#######################

模块使用方法
import main

定义对象 test=main.crazy(最大线程数)
开启线程 test.apply_pool(target=函数名,(参数,))


