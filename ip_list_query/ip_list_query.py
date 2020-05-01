#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
import base64
import os
import requests
import shutil


PRIVATE_DIR = "../../private_files"
FILENAME = "LAN_ip_list.cfg"
URL = "http://192.168.1.1/ER3260_ipmac.cfg"


cfg = configparser.ConfigParser()
cfg.read(os.path.join(PRIVATE_DIR, 'users_config', 'users.ini'))
USERNAME=cfg.get('USERS', 'user1').encode()
PASSWORD=cfg.get('PASSWORDS', 'password1').encode()

encoded = base64.b64encode(USERNAME+':'.encode()+PASSWORD)
headers = {'Authorization': b'Basic ' + encoded}

query_res = requests.get(URL, headers=headers)
filepath = os.path.join(PRIVATE_DIR, 'ip_list_file', FILENAME)
filepath_split = os.path.splitext(filepath)
old_filepath = filepath_split[0]+"_old"+filepath_split[1]

if os.path.exists(filepath):
	shutil.move(filepath, old_filepath)

with open(filepath, 'wb') as f:
	f.write(query_res.content)