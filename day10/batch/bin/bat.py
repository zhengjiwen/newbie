#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-12 01:40:22
# Description:

__author__ = 'Jiwen Zheng'

import os
import sys 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from modules import bat_main

if __name__ == '__main__':
    Entrypoint = bat_main.ArgvHandler(sys.argv)
