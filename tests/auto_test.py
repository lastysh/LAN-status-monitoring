# coding=utf-8

import unittest  # , time as _time
import os
import sys
import configparser
from selenium import webdriver
import pymysql

pymysql.install_as_MySQLdb()

sys.path.append("../")
PRIVATE_DIR = "../private_files"
cfg = configparser.ConfigParser()
cfg.read(os.path.join(PRIVATE_DIR, 'users_config', 'users.ini'))
dbuser = cfg.get('DBACCOUNT', 'user')
dbpasswd = cfg.get('DBACCOUNT', 'password')


class QueryTest(unittest.TestCase):
    def setUp(self):
        from query.ip_list_query import query_ip, PRIVATE_DIR, FILENAME
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
        from ping.ping_test import get_result, FirstTup, ip_status_dict
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
        import MySQLdb  # noqa
        self.conn_func = MySQLdb.connect
        self.conn = self.cur = None

    def test_db(self):
        self.conn = self.conn_func(host='localhost', user=dbuser, passwd=dbpasswd, db='ip_test', charset='utf8')
        self.cur = self.conn.cursor()
        e_res = 0
        try:
            self.cur.execute("select * from ns_test_ips")
        except pymysql.err.ProgrammingError:
            e_res = 1
        # self.assertTrue(self.cur.fetchall())
        self.assertEqual(e_res, 0)

    def tearDown(self):
        if self.cur is not None:
            self.cur.close()
            self.cur = None
        if self.conn is not None:
            self.conn.close()
            self.conn = None


class WebTest(unittest.TestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1'
        self.port = '8000'
        self.base_url = self.host + ':' + self.port
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_web(self):
        self.driver.get(self.base_url)
        title = self.driver.title
        self.assertEqual(title, u"主页")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
