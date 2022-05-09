#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
help creating data structure so filename match book
rm tmp.py
for i in `ls clean`; do ./bin/createBookName.py clean/$i >> tmp.py; done
"""
import sys
import re
from globals import *
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

inputFile=sys.argv[1]

with open(inputFile) as fp:
    soup=BeautifulSoup(fp, features='xml')
    for book in soup.find_all('div',type="book"):
        curBook={}
        bookOsisId=book["osisID"]
        pattern="clean/(\d+)-%s(\w*).xml"%bookOsisId
        m=re.match(pattern,inputFile)
        if not m:
            print("Cannot parse inputFile",inputFile)
            sys.exit()
        prefix=m.group(1)
        postfix=m.group(2)
        
        curBook["id"]=bookOsisId
        curBook["prefix"]=prefix
        curBook["postfix"]=postfix
        print("bookInfo.append(%s)"%curBook)


