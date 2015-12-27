#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-27 02:11:35
# Description:

import paramiko
import os
__author__ = 'Jiwen Zheng'

import os
import sys 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from modules import db
from modules import menu

if __name__ == '__main__':
	menu.main()
