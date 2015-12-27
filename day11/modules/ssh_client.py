#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-22 06:54:09
# author: 郑集文

import select
import sys
import socket
import termios
import tty
import paramiko
from modules import log


class ssh_client(object):

	def __init__(self,ip,port,username,passwd,hostname,user):

		self.tran = paramiko.Transport((ip,port,))
		self.tran.start_client()
		self.tran.auth_password(username,passwd)
		self.chan = self.tran.open_session()
		self.chan.get_pty()
		self.chan.invoke_shell()
		self.oldtty = termios.tcgetattr(sys.stdin)
		self.log=log.Log()
		self.log.logger.error('user:%s login host:%s'%(user,hostname))
	
	def connect(self):
		try:
			tty.setraw(sys.stdin.fileno())
			self.chan.settimeout(0.0)

			while True:
				r,w,e = select.select([self.chan,sys.stdin],[],[],1)
				if self.chan in r:
					try:
						x = self.chan.recv(1024)
						if len(x) == 0:
							print '\r\n*** EOF\r\n',
							break
						sys.stdout.write(x)
						sys.stdout.flush()
					except socket.timeout:
						pass
				if sys.stdin in r:
					x = sys.stdin.read(1)
					if len(x) == 0:
						break
					self.chan.send(x)

		finally:
			termios.tcsetattr(sys.stdin,termios.TCSADRAIN, self.oldtty)

