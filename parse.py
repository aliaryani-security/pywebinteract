#!/usr/bin/env python3

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = urlopen ('http://192.168.1.100')

page = url.read()
soup = BeautifulSoup (page, features="html.parser")

print (soup)
# This project is intentionally left here!
# I will write a whole new project about beautiful soup later,
# This isn't the right place for it, is it ?!