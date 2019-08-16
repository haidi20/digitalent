# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:04:20 2019

@author: haidinata
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

#  fetch html
response = urlopen('https://www.facebook.com/groups/442974152553174/')
html_doc = response.read()

#parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

#format the parsed html file
strhtm = soup.prettify()

# print the first few char
print(soup.find_all('.text_exposed_root'))