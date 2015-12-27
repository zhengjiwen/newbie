#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-26 20:57:47
# Description:
#coding:utf-8  

import logging  
from conf import setting

class Log(object):
	def __init__(self):
		logger = logging.getLogger()
		fh = logging.FileHandler(setting.logpath)  
		ch = logging.StreamHandler()  
		formatter = logging.Formatter('%(asctime)s %(name)s %(message)s')  
		fh.setFormatter(formatter)  
		ch.setFormatter(formatter)  
		logger.addHandler(fh)  
		logger.addHandler(ch)  
		self.logger=logger
