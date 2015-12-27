#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-16 12:49:12
# author: 郑集文
# Description:

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random

def yanzhengma(dizhi): 

	yanzhengma=random.randint(100000, 999999)

	msg = MIMEText('邮箱验证码: %s'%yanzhengma, 'plain', 'utf-8')
	msg['From'] = formataddr(["爱玩不玩",'jzzjw@139.com'])
	msg['To'] = formataddr(["走人",dizhi])
	msg['Subject'] = "邮箱验证。"
	server = smtplib.SMTP("smtp.139.com", 25)
	server.login("jzzjw@139.com", "asdasdasd")
	server.sendmail('jzzjw@139.com', [dizhi,], msg.as_string())
	server.quit()

	return yanzhengma
