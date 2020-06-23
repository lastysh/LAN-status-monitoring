# coding=utf-8

import unittest, time
import os
import sys
import configparser


sys.path.append("../")
PRIVATE_DIR = "../../private_files"
cfg = configparser.ConfigParser()
cfg.read(os.path.join(PRIVATE_DIR,'users_config','users.ini'))
dbuser=cfg.get('DBACCOUNT', 'user')
dbpasswd=cfg.get('DBACCOUNT', 'password')


class QueryTest(unittest.TestCase):
	def setUp(self):
		from ip_list_query.ip_list_query import query_ip, PRIVATE_DIR, FILENAME
		self.qi = query_ip
		self.pd = PRIVATE_DIR
		self.fn = FILENAME

	def test_qi(self):
		filepath = os.path.join(self.pd, 'ip_list_file', self.fn)
		if self.qi():
			self.assertTrue(os.path.exists(filepath))

	def tearDown(self):
		pass


class IpTest(unittest.TestCase):
	def setUp(self):
		from network_status_test.ping_test import get_result, FirstTup, ip_status_dict
		self.gr = get_result
		self.ft = FirstTup
		self.isd = ip_status_dict

	def test_ft(self):
		self.gr(self.ft)
		result = self.isd[self.ft[0]]
		# print(result)
		try:
			self.assertEqual(result[2], 1)
		except AssertionError:
			self.assertEqual(result[2], 2)

	def tearDown(self):
		pass


class DbTest(unittest.TestCase):
	def setUp(self):
		import MySQLdb
		self.conn = MySQLdb.connect

	def test_db(self):
		conn = self.conn(host='localhost', user=dbuser, passwd=dbpasswd, db='ip_test', charset='utf8')
		cur = conn.cursor()
		cur.execute("select * from ns_test_ips")
		self.assertTrue(cur.fetchall())

	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main()