from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ns_test import models
# Create your views here.

# import sys
# sys.path.append(r"../..")
# from network_status_test import *

def test_index(request):
	if request.method == 'GET':
		ip_list = models.Ips.objects.all()
		return render(request, 'ipshow/index.html', {'baidu': ip_list[0], 'ip_list': ip_list[1:]})

def index(request):
	return HttpResponseRedirect('/')

def login(request):
	return HttpResponse("<b>功能正在开发中，敬请期待</b>")


def register(request):
	return HttpResponse("<b>功能正在开发中，敬请期待</b>")
