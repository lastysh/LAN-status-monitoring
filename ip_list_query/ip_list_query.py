#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
import base64
import os
import requests
import shutil


PRIVATE_DIR = "../../private_files/"


cfg = configparser.ConfigParser()
cfg.read(PRIVATE_DIR+"users_config"+os.sep+"users.ini")
USERNAME=cfg.get("USERS", "user1").encode()
PASSWORD=cfg.get("PASSWORDS", "password1").encode()
encoded = base64.b64encode(USERNAME+":".encode()+PASSWORD)

get_url = "http://192.168.1.1/ER3260_ipmac.cfg"
headers = {"Authorization": b"Basic " + encoded}
query_res = requests.get(get_url, headers=headers)
filename = PRIVATE_DIR + "ip_list_file" + os.sep + os.path.split(query_res.url)[-1]
filename_split = os.path.splitext(filename)
old_filename = filename_split[0]+"_old"+filename_split[1]

if os.path.exists(filename):
	shutil.move(filename, old_filename)

with open(filename, "wb") as f:
	f.write(query_res.content)