from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ns_test import models
# Create your views here.

import sys
sys.path.append(r"../")
from network_status_test import ping_test


def test_index(request):
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
	if ping_test.main(): return HttpResponse("更新异常！") #无法获取最新的<font style='color:red'>路由表</font>当前状态更新成功！
	return HttpResponse("更新成功！")