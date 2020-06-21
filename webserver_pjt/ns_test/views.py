from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ns_test import models
import json
# Create your views here.

import sys
sys.path.append(r"../")
from network_status_test import ping_test


def home(request):
	if request.method == 'GET':
		ip_list = models.Ips.objects.all()
		if len(ip_list) == 0:
			return render(request, 'ipshow/update.html')
		return render(request, 'ipshow/index.html', {'baidu': ip_list[0], 'ip_list': ip_list[1:]})


def index(request):
	return HttpResponseRedirect('/')


def login(request):
	return HttpResponse("<b>功能正在开发中，敬请期待</b>")


def register(request):
	return HttpResponse("<b>功能正在开发中，敬请期待</b>")


def update_state(request):
	if ping_test.main(): return HttpResponse("更新异常！") #无法获取最新的路由表，当前使用的路由表状态更新成功！
	return HttpResponse("更新成功！")

def insert_comment(request):
	if request.method == 'POST':
		xhr_dict = parse_requeset_body(request.body.decode())
		ip_record = models.Ips.objects.get(ip=xhr_dict['ip'])
		comment_record = models.Comment.objects.filter(ip=xhr_dict['ip'])
		if comment_record:
			comment_record[0].comment = xhr_dict['comment']
			comment_record[0].save()
		else:
			new_record = models.Comment.objects.create()
			new_record.ip = xhr_dict['ip']
			new_record.comment = xhr_dict['comment']
			new_record.save()
		ip_record.comment = xhr_dict['comment']
		ip_record.save()
		return HttpResponse("设置成功！")
	else:
		r = HttpResponse()
		error_dict = {'message':'error', 'state':'404'}
		r.content = json.dumps(error_dict)
		return r


def parse_requeset_body(s:str):
	kv_list = s.split('&')
	prb_dict = dict()
	for kv in kv_list:
		key, value = kv.split('=')
		prb_dict[key] = value
	return prb_dict

