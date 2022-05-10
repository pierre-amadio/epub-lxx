#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create the table of contents data.
first arguments: list of xml file.
last argument: where to store the output
"""
import sys
import re
from globals import *
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

playOrderIdCnt=indexOffset+1
data=[]

data.append({
    "navpointId":"1",
    "playOrderId":"1",
    "name":"Table Of Contents",
    "file":"Text/01-TOC.html"
    })

data.append({
    "navpointId":"2",
    "playOrderId":"2",
    "name":"Foreword",
    "file":"Text/02-Foreword.html"
    })

fileCnt=2
for curXmlFileName in sys.argv[1:-1]:
    print(curXmlFileName)
    with open(curXmlFileName) as fp:
        soup=BeautifulSoup(fp,features='xml')
        for book in soup.find_all('div',type="book"):
            curBook={}
            bookOsisId=book["osisID"]
            pattern="clean/(\d+)-%s(\w*).xml"%bookOsisId
            m=re.match(pattern,curXmlFileName)
            if not m:
                print("Cannot parse bookOsisId",curXmlFileName)
                sys.exit()
            prefix=m.group(1)
            postfix=m.group(2)

            bookName="%s %s"%(bookOsisId,postfix)
            bookIndex=getBookIndex(bookOsisId,prefix,postfix)+indexOffset
            fileName="Text/%02d-%s%s.html"%(bookIndex,bookOsisId,postfix)
            curBook["name"]=bookName
            curBook["navpointId"]=fileCnt
            curBook["playOrderId"]=fileCnt
            fileCnt+=1
            curBook["file"]=fileName
            curBook["chapters"]=[]
        
            for chapter in book.find_all("chapter"):
                curChapter={}
                pattern="%s.(\d+)"%bookOsisId
                m=re.match(pattern,chapter["osisID"])
                if not m:
                    print("cannot match",chapter["osisID"])
                    sys.exit()

                curChapterNbr=m.group(1)
                fileName="Text/%02d-%s%s-%s.html"%(bookIndex,bookOsisId,postfix,curChapterNbr)
                curChapter["navpointId"]=fileCnt
                curChapter["playOrderId"]=fileCnt
                fileCnt+=1
                curChapter["name"]="Chapter %s"%curChapterNbr
                curChapter["file"]=fileName
            
                curBook["chapters"].append(curChapter) 

            data.append(curBook)



ncxTemplate = env.get_template("toc.ncx")
ncxOutput = ncxTemplate.render(books=data)

fileOutput="toc.ncx"
with open(fileOutput,"w") as f:
    f.write(ncxOutput)

tocTemplate = env.get_template("TOC.html")
tocOutput = tocTemplate.render(books=data)

fileOutput="%s/01-TOC.html"%sys.argv[-1]
with open(fileOutput,"w") as f:
    f.write(tocOutput)

