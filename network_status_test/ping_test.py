#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import subprocess
import MySQLdb
from multiprocessing.dummy import Pool as mulPool


IP_FILE_PATH = "../../private_files/ip_list_file/LAN_ip_list.cfg"


def file_parser():
	ip_msg_list = list()
	with open(IP_FILE_PATH, 'r') as f:
		while True:
			line = f.readline()
			if line:
				record_tuple = line.split()
				ip_msg_list.append((record_tuple[1], (record_tuple[0], record_tuple[2])))
			else:
				break
	return ip_msg_list


def ping_execute(ip):
	res = subprocess.run("ping %s" % ip, shell=True, stdout=subprocess.PIPE)
	info = res.stdout.decode("cp936")
	return info


ip_msg_list = file_parser()
ip_status_dict = dict()


def get_result(ip_msg):
	ip = ip_msg[0]
	msg_tup = ip_msg[1]
	ping_res = ping_execute(ip)
	loss = re.findall(r"丢失 = (\d)", ping_res)[0]
	average = re.findall(r"平均 = (\d+)ms", ping_res)
	overtime = re.findall(r"请求超时", ping_res)
	unreachable = re.findall(r"无法访问目标主机", ping_res)
	try:
		if len(average) == 0:
			status = 0
			ip_status_dict[ip] = msg_tup + (status,)
		elif len(unreachable) > 0:
			status = 3  # Ping unstable
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
	cur.execute("select * from ns_test_ips")
	if cur.fetchall():
		cur.execute("truncate ns_test_ips")
		cur.close()
	for item in isl:
		cur = conn.cursor()
		sql = "insert into ns_test_ips values(NULL, '%s', '%s', '%s', '%s', '')" % (item[0], item[1][0], item[1][1], item[1][2])
		cur.execute(sql)
		cur.close()
	conn.commit()
	conn.close()

if __name__ == '__main__':
	pool = mulPool(128) # 设定进程数
	pool.map(get_result, ip_msg_list)
	pool.close()
	pool.join()

	ip_status_list = sorted(ip_status_dict.items(), key=lambda ip: int(ip[0].split(".")[-1]))
	conn = MySQLdb.connect(host="localhost", user="root", passwd="linux20001", db="ip_test")
	write_to_db(conn, ip_status_list)
