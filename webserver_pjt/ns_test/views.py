from django.shortcuts import render
from django.http import HttpResponse
from ns_test import models
# Create your views here.

# import sys
# sys.path.append(r"../..")
# from network_status_test import *

def test_index(request):
	if request.method == 'GET':
		ip_list = models.Ips.objects.all()
		return render(request, "ipshow/index.html", {'ip_list': ip_list})