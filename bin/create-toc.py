#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create the table of contents data.
first arguments: list of xml file.
second argument: where to store the output
"""
import sys
import re
from globals import *
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

htmlDir=sys.argv[1]
outputDir=sys.argv[2]

"""
for bookData in bookInfo:
    print(bookData)
    bookId=bookData["id"]
    bookPrefix=bookData["prefix"]
    actualPrefix=int(bookPrefix)+indexOffset
    bookPostfix=bookData["postfix"]

    bookHtml="%s/%02d-%s%s.html"%(htmlDir,actualPrefix,bookId,bookPostfix)
    print(bookHtml)
"""

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

            bookName=bookOsisId 
            bookIndex=getBookIndex(bookOsisId,prefix,postfix)+indexOffset
            fileName="Text/%02d-%s%s.html"%(bookIndex,bookOsisId,postfix)
            curBook["name"]=bookName
            curBook["navpointId"]=fileCnt
            curBook["playOrderId"]=fileCnt
            fileCnt+=1
            curBook["file"]=fileName
        
            for chapter in book.find_all("chapter"):
                pattern="%s.(\d+)"%bookOsisId
                m=re.match(pattern,chapter["osisID"])
                if not m:
                    print("cannot match",chapter["osisID"])
                    sys.exit()
                curChapterNbr=m.group(1)
            
            
            """
            ncxTemplate = env.get_template("toc.ncx")
            ncxOutput = bookTemplate.render(book={"name":bookName})

            bookIndex=getBookIndex(bookOsisId,prefix,postfix)+indexOffset
            fileOutput="%s/%02d-%s%s.html"%(outputDir,bookIndex,bookOsisId,postfix)
            with open(fileOutput,"w") as f:
                f.write(bookOutput)
            for chapter in book.find_all("chapter"):
                createChapterHtml(chapter,bookOsisId,bookIndex,postfix)

                
            """         
