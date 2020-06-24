import os


import sys
sys.path.append("../")
from ping.ping_test import file_parser

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
	record_mac = list()
	record_name = list()
	for ip in ss:
		new_mac = nd[ip][0]
		old_mac = od[ip][0]
		new_name = nd[ip][1]
		old_name = od[ip][1]
		if new_mac != old_mac: # mac
			# print(">> {0}: mac地址从 {1} 更改为 {2}".format(ip, new_mac, old_mac))
			record_mac.append("<font color='red'>&lt;M&gt;</font> {0}：<font color='green'>mac地址</font>从 {1} 更改为 {2}".format(ip, new_mac, old_mac))
		if new_name != old_name: # name
			# print(">> {0}: 名称从 {1} 更改为 {2}".format(ip, new_name, old_name))
			record_name.append("<font color='red'>&lt;M&gt;</font> {0}：<font color='green'>名称</font>从 {1} 更改为 {2}".format(ip, new_name, old_name))
	return record_mac, record_name


def diff_compare():
	global no_use
	try:
		new_rtb, old_rtb = get_routetable()
	except:
		return
	nset = set(i[0] for i in new_rtb)
	oset = set(i[0] for i in old_rtb)
	add = nset.difference(oset)
	delete = oset.difference(nset)
	all_ip_set = set('192.168.1.%s' % i for i in range(2, 255))
	no_use = sorted(all_ip_set.difference(nset), key=lambda i: int(i.split('.')[-1]))
	same_set = nset & oset
	return check_modify(same_set, new_rtb, old_rtb)


def write_to_html(pmac, pname):
	html_start = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>每日测试报告</title>
</head>
<body>
<center>
	<h1>TEST_REPORT</h1>
	""".encode()
	html_end = """</center>
</body>
</html>
	""".encode()
	with open("example_report.html", 'wb') as f:
		f.write(html_start)
		f.write('<div style="text-align:left;width: 50%;">\n'.encode())
		for record in pmac:
			f.write('\t<p><strong>%s</strong></p>\n'.encode() % record.encode())
		for record in pname:
			f.write('\t<p><strong>%s</strong></p>\n'.encode() % record.encode())
		f.write('\t</div>\n'.encode())
		if no_use:
			i = 0
			close_tr = 1
			f.write('<h3>No Use IP List:</h3>\n'.encode())
			f.write('<table style="border:3px double;font-weight:bold;" cellpadding="5">\n'.encode())
			for ip in no_use:
				if i%5 == 0:
					close_tr = 0
					f.write('<tr>\n'.encode())
				f.write('<td style="border:1px solid;background:rgb(165,166,167);">%s</td>\n'.encode() % ip.encode())
				if i%5 == 4:
					close_tr = 1
					f.write('</tr>\n'.encode())
				i += 1
			if close_tr:
				f.write('</table>\n'.encode())
			else:
				f.write('</tr>\n</table>\n'.encode())
		f.write(html_end)


if __name__ == '__main__':
	try:
		rdm, rdn = diff_compare()
		write_to_html(rdm, rdn)
		print("报告已生成！")
	except:
		print("程序执行失败！")
