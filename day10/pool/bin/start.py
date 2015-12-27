#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-20 05:28:49
# author: 郑集文

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import main

pool=main.crazy(5)
test=main.test

for i in range(10):
	pool.apply_pool(target=test,args=(i,))
