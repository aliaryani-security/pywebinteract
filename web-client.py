#!/usr/bin/env python3

import requests

url = "http://192.168.1.100"

response = requests.get (url)
print (response.content.decode())