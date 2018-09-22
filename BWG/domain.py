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
token = '$id,$token'

data = {
    'login_token': token,
    'format': 'json',
    'lang': 'cn',
    'error_on_empty': 'no',
    'domain': 'cocolate.cc',
    'record_id': '$id',
    'sub_domain': '$sub',
    'record_type': '$type',
    'record_line': '默认',
    'value': ip,
}
url = "https://dnsapi.cn/Record.Modify"
r = requests.post(url, data=data, timeout=5)
