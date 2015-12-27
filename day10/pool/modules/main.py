#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-20 05:29:03
# author: 郑集文

import Queue
import threading
import time

class crazy(object):
	
	def __init__(self,num=1):
		if num < 1:
			raise ValueError("Number of processes must be at least 1")
		self.q=Queue.Queue(num)
		for i in range(num):
			self.q.put(num)	

	def apply_pool(self,target,args):
		self.q.get()
		a=threading.Thread(target=target,args=(self,)+args)
		a.start()

def test(self,num):
	print 'id=%s start'%num
	time.sleep(2)
	self.q.put_nowait(1)
	print 'id=%s end'%num
