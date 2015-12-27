#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-11 23:32:00
# Description:

__author__ = 'Jiwen Zheng'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE={ 
			"db_type":'file', #mysql,file,oracle
		}

#主机组文件
#GROUP_FILE = BASE_DIR+'/var/group.json'
GROUP_FILE = BASE_DIR+'/var/group.json'


#添加主机组xls文件存放路径
#ADD_PATH = BASE_DIR+'/var/group/'
ADD_PATH = BASE_DIR+'/var/group/'
