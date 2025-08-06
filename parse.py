#!/usr/bin/env python3

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = urlopen ('http://192.168.1.100')

page = url.read()
soup = BeautifulSoup (page, features="html.parser")

print (soup)