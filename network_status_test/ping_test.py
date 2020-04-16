#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import subprocess
from multiprocessing.dummy import Pool as mulPool


IP_FILE_PATH = "../../private_files/LAN_ip_list.cfg"


# def file_parser():
with open(IP_FILE_PATH, 'rb') as f:
	while True:
		line = f.readline()
		if line:
			record_tuple = line.split()
			print(record_tuple)

# def ping_execute(ip):
# 	res = subprocess.run("ping %s" % ip, shell=True, stdout=subprocess.PIPE)
# 	info = res.stdout.decode("cp936")
# 	return info


# ip_status_dict = dict()


# def get_result(ip):
# 	ping_res = ping_execute(ip)
# 	try:
# 		loss = re.findall(r"丢失 = (\d)", ping_res)[0]
# 		average = re.findall(r"平均 = (\d+)ms", ping_res)
# 		overtime = re.findall(r"请求超时", ping_res)
# 		unreachable = re.findall(r"无法访问目标主机", ping_res)
# 		print(ip, average, overtime, unreachable)
# 		if len(average) == 0:
# 			status = 0
# 			ip_status_dict[ip] = status
# 			return
# 		elif len(unreachable) > 0:
# 			status = 3  # Ping unstable
# 		elif int(average[0])>200 or len(overtime)>0:
# 			status = 2
# 			ip_status_dict[ip] = status
# 		else:
# 			status = 1
# 			ip_status_dict[ip] = status
# 	except:
# 		status = 0
# 		ip_status_dict[ip] = status

# # pool = mulPool(50) # 设定进程数
# # pool.map(get_result, ip_list)
# # pool.close()
# # pool.join()


# ip_tuple = sorted(ip_status_dict.items(), key=lambda ip: ip[0])
# ip_status_dict = dict(ip_tuple)
# print(ip_status_dict)

