#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import subprocess
from multiprocessing.dummy import Pool as mulPool


# IP_FILE_PATH = 


# ip_list = [
# '192.168.42.1',
# '192.168.42.2',
# '192.168.42.3',
# '192.168.42.4',
# '192.168.42.5',
# '192.168.42.6',
# '192.168.42.7',
# '192.168.42.8',
# '192.168.42.9',
# '192.168.42.10',
# '192.168.42.11',
# '192.168.42.12',
# '192.168.42.13',
# ]

ip_list = list()
for i in range(2, 256):
	ip_list.append("192.168.42." + str(i))


def ping_execute(ip):
	# res = subprocess.run("ping 192.168.1.1", shell=True, stdout=subprocess.PIPE)
	res = subprocess.run("ping %s" % ip, shell=True, stdout=subprocess.PIPE)
	info = res.stdout.decode("cp936")
	return info

ip_status_dict = dict()

def get_result(ip):
	state = 1
	ping_res = ping_execute(ip)
	try:
		loss = re.findall(r"丢失 = (\d)", ping_res)[0]
		if loss == 4:
			status = 0
			ip_status_dict[ip] = status
			return
		average = re.findall(r"平均 = (\d+)ms", ping_res)[0]
		overtime = re.findall(r"请求超时", ping_res)
		if average>200 or len(overtime)>0:
			status = 2
			ip_status_dict[ip] = status
	except:
		status = 0
		ip_status_dict[ip] = status

pool = mulPool(250) # 设定进程数
pool.map(get_result, ip_list)
pool.close()
pool.join()


ip_tuple = sorted(ip_status_dict.items(), key=lambda ip: ip[0])
ip_status_dict = dict(ip_tuple)
print(ip_status_dict)

