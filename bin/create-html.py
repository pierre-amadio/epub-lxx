#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

inputFile=sys.argv[1]
outputDir=sys.argv[2]

print(inputFile,outputDir)

with open(inputFile) as fp:
    soup=BeautifulSoup(fp, features='xml')
    for book in soup.find_all('div',type="book"):
        bookOsisId=book["osisID"]
        print(bookOsisId)
