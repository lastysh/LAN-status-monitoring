#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import subprocess
import MySQLdb
from multiprocessing.dummy import Pool as mulPool


import sys
sys.path.append("../")
from ip_list_query import ip_list_query

IP_FILE_PATH = "../../private_files/ip_list_file/LAN_ip_list.cfg"
InterAddr = "www.baidu.com"
FirstTup = (InterAddr, ('NaN', 'Baidu'))
FIDelayV = "NaN"


def file_parser(ifp):
	ip_msg_list = list()
	with open(ifp, 'r') as f:
		lines = f.readlines()
		for line in lines:
			record_tuple = line.split()
			if record_tuple:
				# element -> (ip, (mac, name))
				ip_msg_list.append((record_tuple[1], (record_tuple[0], record_tuple[2])))
			else:
				continue
	return ip_msg_list


def ping_execute(ip):
	res = subprocess.run('ping %s' % ip, shell=True, stdout=subprocess.PIPE)
	info = res.stdout.decode('cp936')
	return info


def get_result(ip_msg):
	global FIDelayV
	ip = ip_msg[0]
	msg_tup = ip_msg[1]
	ping_res = ping_execute(ip)
	loss = re.findall(r'丢失 = (\d)', ping_res)[0]
	average = re.findall(r'平均 = (\d+)ms', ping_res)
	overtime = re.findall(r'请求超时', ping_res)
	unreachable = re.findall(r'无法访问目标主机', ping_res)
	if ip == InterAddr:
		try:
			FIDelayV = average[0] + " ms"
		except IndexError:
			FIDelayV = "NaN"
	try:
		if len(average) == 0:
			status = 0
			ip_status_dict[ip] = msg_tup + (status,)
		elif len(unreachable) > 0:
			status = 3  # Ping unstable
			ip_status_dict[ip] = msg_tup + (status,)
		elif int(average[0])>200 or len(overtime)>0:
			status = 2
			ip_status_dict[ip] = msg_tup + (status,)
		else:
			status = 1
			ip_status_dict[ip] = msg_tup + (status,)
	except:
		status = 0
		ip_status_dict[ip] = msg_tup + (status,)


def write_to_db(conn, isl):
	cur = conn.cursor()
	cur.execute('select * from ns_test_ips')
	if cur.fetchall():
		cur.execute('truncate ns_test_ips')
		cur.close()
	for item in isl:
		cur = conn.cursor()
		if item[0] == InterAddr:
			sql = "insert into ns_test_ips values(NULL, '%s', '%s', '%s', '%s', '%s')" % (item[0], item[1][0], item[1][1], item[1][2], FIDelayV)
		else:
			sql = "insert into ns_test_ips values(NULL, '%s', '%s', '%s', '%s', '')" % (item[0], item[1][0], item[1][1], item[1][2])
		cur.execute(sql)
		cur.close()
	conn.commit()
	conn.close()


def main():
	global ip_status_dict
	return_code = 0
	if not ip_list_query.query_ip(): return_code = 1
	ip_msg_list = file_parser(IP_FILE_PATH)
	ip_status_dict = dict()
	ip_msg_list.insert(0, FirstTup)
	pool = mulPool(128) # 设定进程数
	pool.map(get_result, ip_msg_list)
	pool.close()
	pool.join()

	InterInfo = (InterAddr, (ip_status_dict.pop(InterAddr)))
	ip_status_list = sorted(ip_status_dict.items(), key=lambda ip: int(ip[0].split('.')[-1]))
	ip_status_list.insert(0, InterInfo)
	conn = MySQLdb.connect(host='localhost', user='root', passwd='linux20001', db='ip_test')
	write_to_db(conn, ip_status_list)
	return return_code


if __name__ == '__main__':
	main()