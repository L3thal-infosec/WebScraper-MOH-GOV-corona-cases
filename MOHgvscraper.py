#!/usr/bin/env python
# coding: utf-8

# In[3]:

from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.mohfw.gov.in/'
headers= {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url)
response.status_code
response.content
soup = BeautifulSoup(response.content, 'html.parser')
stat_table =soup.find_all('table', class_ = 'table table-striped' )
len(stat_table)
stat_table = stat_table[0]
for row in stat_table.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)

with open('random.txt', 'w') as r:
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text.ljust(40))
        r.write('\n')
#http://www.whoishostingthis.com/tools/user-agent/

#'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'


