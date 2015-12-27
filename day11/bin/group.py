#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-11 19:26:04
# author: 郑集文
# Description:

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from modules import add

if __name__ == '__main__':
	Entrypoint = add.ArgvHandler(sys.argv)
