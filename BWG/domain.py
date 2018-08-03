import requests
import os
import socket
import re

p = os.popen('curl ip.3322.net').read()
m = socket.gethostbyname('sss.cocolate.cc')
p = ''.join(p.split())
m = ''.join(m.split())
if(p == m):
    exit(0)

ip = p
token = '51474,20c11de6a42ccb66eae04b342be490ba'

data = {
    'login_token': token,
    'format': 'json',
    'lang': 'cn',
    'error_on_empty': 'no',
    'domain': 'cocolate.cc',
    'record_id': '352248788',
    'sub_domain': 'sss',
    'record_type': 'A',
    'record_line': '默认',
    'value': ip,
}
url = "https://dnsapi.cn/Record.Modify"
r = requests.post(url, data=data, timeout=5)
