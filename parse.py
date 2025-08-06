#!/usr/bin/env python3

import urllib3

http = urllib3.PoolManager()

url = "http://192.168.1.100"

response = http.request('GET', url)
print (response.data.decode('utf-8'))