# coding=utf-8

import unittest, time
import os
import sys
sys.path.append("../")

class QueryTest(unittest.TestCase):
	def setUp(self):
		from ip_list_query.ip_list_query import query_ip, PRIVATE_DIR, FILENAME
		self.qi = query_ip
		self.pd = PRIVATE_DIR
		self.fn = FILENAME

	def test_qi(self):
		filepath = os.path.join(self.pd, 'ip_list_file', self.fn)
		if self.qi() == None:
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


if __name__ == '__main__':
	unittest.main()