#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Proverbs numbering is weird:
<chapter osisID="Prov.23">
<chapter osisID="Prov.24">
<chapter osisID="Prov.30">
<chapter osisID="Prov.24">
<chapter osisID="Prov.30">
<chapter osisID="Prov.31">
<chapter osisID="Prov.32">
<chapter osisID="Prov.33">
<chapter osisID="Prov.34">
<chapter osisID="Prov.35">
<chapter osisID="Prov.36">
<chapter osisID="Prov.31">


#Excerpt from the reader's edition:
#some witnesses to the greek version of proverbs contain portion of chs 30-31 inserted within ch24 as reflected in rahlfs-hannhart.
#the reason for this textual divergence remains unclear and we have retained the versifications of the masoretic text for simplicity.

Lets try to do the same.

* There are several 24.22 verses in the xml file. They appear as such in the reade's edition:
Prov.24.22    ἐξαίφνης γὰρ τείσονται τοὺς ἀσεβεῖς τὰς δὲ τιμωρίας ἀμφοτέρων τίς γνώσεται
Prov.24.22.a  λόγον φυλασσόμενος υἱὸς ἀπωλείας ἐκτὸς ἔσται δεχόμενος δὲ ἐδέξατο αὐτόν
Prov.24.22.b  μηδὲν ψεῦδος ἀπὸ γλώσσης βασιλεῖ λεγέσθω καὶ οὐδὲν ψεῦδος ἀπὸ γλώσσης αὐτοῦ οὐ μὴ ἐξέλθῃ
Prov.24.22.c  μάχαιρα γλῶσσα βασιλέως καὶ οὐ σαρκίνη ὃς δ’ ἂν παραδοθῇ συντριβήσεται
Prov.24.22.d  ἐὰν γὰρ ὀξυνθῇ ὁ θυμὸς αὐτοῦ σὺν νεύροις ἀνθρώπους ἀναλίσκει
Prov.24.22.e  καὶ ὀστᾶ ἀνθρώπων κατατρώγει καὶ συγκαίει ὥσπερ φλὸξ ὥστε ἄβρωτα εἶναι νεοσσοῖς ἀετῶν

There are 2 "chapter 24" (v 1-22e and v23-34) in the xml file. Need to be merged into 1.

* xml Chapter 32 is reader's edition chapter 25.
* xml chapter 33 is reader's edition chapter 26
* xml chapter 34 is reader's edition chatper 27
* xml chapter 35 is reader's edition chapter 28
* xml chapter 36 is reader's edition chatper 29
* There are two chapter 30 in the xml file. Need to be merged into 1.
* There are two chapter 31 in the xml file. Need to be merged into 1.
"""
import sys
import re
from bs4 import BeautifulSoup
import copy

inputFile=sys.argv[1]
outputDir=sys.argv[2]
outputFile="27.Proverbs.xml"

with open(inputFile) as fp:
    soup = BeautifulSoup(fp, 'xml')

new=copy.copy(soup)
for chapter in new.find_all("chapter"):
    m=re.match("Prov.(\d+)",chapter["osisID"])
    if not m:
        print("Cannot parse",chatper["osisID"])
        sys.exit()
    curChapter=int(m.group(1))
    if curChapter<=23:
        continue
    print("new chapter to be removed",curChapter)
    chapter.decompose()



