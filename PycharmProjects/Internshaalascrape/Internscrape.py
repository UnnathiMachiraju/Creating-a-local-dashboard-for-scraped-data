# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:11:01 2019

@author: unnathi
"""

import bs4

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

import json
from collections import Counter

loc_list = []
intern_list = []

for i in range(253):  # Number of pages plus one
    page_url = "https://internshala.com/internships".format(i)
    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    containers = page_soup.findAll("div", {"class": "internship_meta"})

    for container in containers:
        initial = container.find("div", {"class": "table-cell"})
        internship = str(container.h4['title'])
        intern_list.append(internship)
        details = container.find("div", {"class": "individual_internship_details"})
        location = details.find_all("a", {"class": "location_link"})
        l=[]
        for i in location:
            l.append(i.text)
            loc_list.append(i.text)

    loc_count = Counter(loc_list)
    intern_count = Counter(intern_list)

with open('static/data/location_count.json','w') as f:
    json.dump(loc_count,f)

with open('static/data/intern_count.json','w') as f:
    json.dump(intern_count,f)


