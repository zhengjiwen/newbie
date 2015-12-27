#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-12-27 05:15:50
# Description:

import MySQLdb
from conf import setting
database=setting.database
class Sql(object):
	
	def __init__(self):
		self.conn = MySQLdb.connect( 
								host=database['host'],
								user=database['user'],
								passwd=database['passwd'],
								db=database['db'],
									)

		self.cur = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)	

	def sql_fetch(self,sql_word):
		reCount = self.cur.execute(sql_word)
		dict_sql= self.cur.fetchall()
		return (reCount,dict_sql)

	def sql_other(self,sql_word):
		reCount = self.cur.execute(sql_word)
		self.conn.commit()
		return reCount

	def delete_group(self,groupname):
		sql_word="delete from host_group where groupname='%s'"%(groupname)
		reCount=self.sql_other(sql_word)
		return reCount

	def delete_host(self,group_id):
		sql_word="delete from host where group_id='%s'"%(group_id)
		reCount=self.sql_other(sql_word)
		return reCount

	def select_group_id(self,groupname):
		sql_word="select id from host_group where groupname='%s'"%(groupname)
		group_id=self.sql_fetch(sql_word)
		group_id=int(group_id[1][0]['id'])
		return group_id
	
	def select_group(self,username):
		sql_word='select id,groupname  from host_group where owner="%s" and enable=1;'%(username)
		group_dict=self.sql_fetch(sql_word)
		group_dict=group_dict[1]
		return group_dict	

	def select_host(self,group_id):
		sql_word='select id,hostname,ip_addr,port,username,passwd from host where group_id="%s";'%(group_id)
		group_dict=self.sql_fetch(sql_word)
		group_dict=group_dict[1]
		return group_dict	

	def insert_group(self,groupname,owner):
		sql_word="insert into host_group (enable,groupname,owner) values('%s','%s','%s');"%(1,groupname,owner)
		reCount=self.sql_other(sql_word)
		sql_word="select id from host_group where groupname='%s'"%(groupname)
		group_id=self.sql_fetch(sql_word)
		#(1L, ({'id': 13L},))
		group_id=int(group_id[1][0]['id'])
		return group_id
		
	def insert_host(self,group_id,*host_list):
			#IP PORT USERNAME PASSWD MENO HOSTNAME
			reCount = self.cur.executemany('insert into host(ip_addr,port,username,passwd,memo,hostname,group_id) values(%s,%s,%s,%s,%s,%s,%s)',host_list)
			self.conn.commit()
			return reCount
