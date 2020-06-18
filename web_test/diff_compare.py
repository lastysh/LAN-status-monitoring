import os


import sys
sys.path.append("../")
from network_status_test.ping_test import file_parser

IP_FILE_DIR = "../../private_files/ip_list_file"

def get_routetable():
	new_cfg_file = IP_FILE_DIR+os.sep+"LAN_ip_list.cfg"
	old_cfg_file = IP_FILE_DIR+os.sep+"LAN_ip_list_old.cfg"
	if os.path.exists(new_cfg_file) and os.path.exists(old_cfg_file):
		new_rtb = file_parser(new_cfg_file)
		old_rtb = file_parser(old_cfg_file)
		return new_rtb, old_rtb
	else:
		print("新旧路由表文件不同时存在，差异比较中止。")


def check_modify(ss, nr, _or):
	nd = dict(nr)
	od = dict(_or)
	for ip in ss:
		new_mac = nd[ip][0]
		old_mac = od[ip][0]
		new_name = nd[ip][1]
		old_name = od[ip][1]
		if new_mac != old_mac: # mac
			print(">> {0}: mac地址从 {1} 更改为 {2}".format(ip, new_mac, old_mac))
		if new_name != old_name: # name
			print(">> {0}: 名称从 {1} 更改为 {2}".format(ip, new_name, old_name))


def diff_compare():
	new_rtb, old_rtb = get_routetable()
	nset = set(i[0] for i in new_rtb)
	oset = set(i[0] for i in old_rtb)
	add = nset.difference(oset)
	delete = oset.difference(nset)
	all_ip_set = set('192.168.1.%s' % i for i in range(2, 255))
	no_use = all_ip_set.difference(nset)
	same_set = nset & oset
	check_modify(same_set, new_rtb, old_rtb)


if __name__ == '__main__':
	diff_compare()
