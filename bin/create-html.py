#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
from globals import *
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

inputFile=sys.argv[1]
outputDir=sys.argv[2]

def createChapterHtml(chapter,bookOsisId,bookIndex,postfix):
    chapterId=chapter["osisID"]
    data={}
    m=re.match("(\S+)\.(\d+)",chapterId)
    if not m:
        print("Cannot parse chapter",chapterId)
        sys.exit()
    bookId=m.group(1)
    
    chapterNbr=m.group(2)
    data["nbr"]=chapterNbr
    data["verses"]=[]
   
    titleTxt=""
    for titleNode in chapter.find_all("title"):
        for w in titleNode.find_all("w"):
            titleTxt+="%s "%w.string
    data["title"]=titleTxt

    for node in chapter.find_all("verse"):
        curVerse={}
        m=re.search("\w+\.\d+\.(.*)",node["osisID"])
        if not m:
            print("cannot parse",node["osisID"])
        curVerse["nbr"]=m.group(1)
        
        curVerseSnt=""
        startFlag=True
        for word in node.find_all():
            if not startFlag:
                curVerseSnt+=" "
            else:
                startFlag=False
            curVerseSnt+=word.string

        curVerseSnt+="."
        curVerse["content"]=curVerseSnt
        data["verses"].append(curVerse)

    chapterTemplate = env.get_template("chapter.html")
    chapterOutput = chapterTemplate.render(chapter=data)
    fileOutput="%s/%02d-%s%s-%s.html"%(outputDir,bookIndex,bookOsisId,postfix,chapterNbr)
    with open(fileOutput,"w") as f:
        f.write(chapterOutput)

with open(inputFile) as fp:
    soup=BeautifulSoup(fp, features='xml')
    for book in soup.find_all('div',type="book"):
        bookOsisId=book["osisID"]
        
        pattern="clean/(\d+)-%s(\w*).xml"%bookOsisId
        m=re.match(pattern,inputFile)
        if not m:
            print("Cannot parse inputFile",inputFile)
            sys.exit()
        prefix=m.group(1)
        postfix=m.group(2)

        bookName=bookOsisId 
        bookTemplate = env.get_template("book.html")
        bookOutput = bookTemplate.render(book={"name":bookName})
        bookIndex=getBookIndex(bookOsisId,prefix,postfix)
        fileOutput="%s/%02d-%s%s.html"%(outputDir,bookIndex,bookOsisId,postfix)
        with open(fileOutput,"w") as f:
            f.write(bookOutput)
        for chapter in book.find_all("chapter"):
            createChapterHtml(chapter,bookOsisId,bookIndex,postfix)
            
