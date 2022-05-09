#!/bin/bash
#Let s also reorder book according to sword-1.9.0/include/canon_lxx.h
#01 Gen #02 Exod #03 Lev #04 Num #05 Deut #06 Josh #07 Judg #08 Ruth #09 1Sam 
#10 2Sam #11 1Kgs #12 2Kgs #13 1Chr #14 2Chr #15 1Esd #16 Ezra #17 Neh #18 Esth #19 Jdt 
#20 Tob #21 1Macc #22 2Macc #23 3Macc #24 4Macc #25 Ps #26 PrMan #27 Prov #28 Eccl #29 Song 
#30 Job #31 Wis #32 Sir #33 PssSol #34 Hos #35 Amos #36 Mic #37 Joel #38 Obad #39 Jonah 
#40 Nah #41 Hab #42 Zeph #43 Hag #44 Zech #45 Mal #46 Isa #47 Jer #48 Bar #49 Lam 
#50 EpJer #51 Ezek #52 PrAzar #53 Sus #54 Dan #55 Bel #56 1En #57 Odes 


rm -rf clean
mkdir clean


cp xml/01-Gen.xml clean/01-Gen.xml
cp xml/03.Exod.xml  clean/02-Exod.xml
cp xml/04.Lev.xml clean/03-Lev.xml
cp xml/05.Num.xml clean/04-Num.xml
cp xml/06.Deut.xml clean/05-Deut.xml

#./bin/5-clean-combine-subtype.py xml/07.JoshB.xml xml1/08.JoshA.xml  specific/
cp xml/07JoshB.xml clean/06-JoshB.xml 
cp xml/08JoshA.xml clean/06-JoshA.xml 

#./bin/5-clean-combine-subtype.py xml/09.JudgesB.xml  xml1/10.JudgesA.xml  specific/
cp xml/10.JudgesA.xml clean/07-JudgesA.xml
cp xml/09.JudgesB.xml clean/07-JudgesB.xml

cp xml/11.Ruth.xml clean/08-Ruth.xml
cp xml/12.1Sam.xml clean/09-1Sam.xml
cp xml/13.2Sam.xml clean/10-2Sam.xml
cp xml/14.1Kings.xml clean/11-1Kgs.xml
cp xml/15.2Kings.xml clean/12-2Kgs.xml
cp xml/16.1Chron.xml clean/13-1Chr.xml
cp xml/17.2Chron.xml clean/14-2Chr.xml
cp xml/18.1Esdras.xml clean/15-1Esd.xml
./bin/clean2esdras.py xml/19.2Esdras.xml clean 
cp xml/20.Esther.xml clean/18-Esth.xml
cp xml/21.Judith.xml clean/19-Jdt.xml

#./bin/5-clean-combine-subtype.py xml/22.TobitBA.xml  xml1/23.TobitS.xml  specific/
cp xml/22.TobitBA.xml clean/20-TobitBA.xml
cp xml/23.TobitS.xml clean/20-TobitS.xml

cp xml/24.1Macc.xml clean/21-1Macc.xml
cp xml/25.2Macc.xml clean/22-2Macc.xml
cp xml/26.3Macc.xml clean/23-3Macc.xml
cp xml/27.4Macc.xml clean/24-4Macc.xml
cp xml/28.Psalms.xml clean/25-Ps.xml
#prayer of manashe is already in odes.
cp xml/31.Proverbs.xml clean/27-Prov.xml
cp xml/32.Qoheleth.xml clean/28-Eccl.xml
cp xml/33.Canticles.xml clean/29-Song.xml
cp xml/34.Job.xml clean/30-Job.xml
cp xml/35.Wisdom.xml clean/31-Wis.xml
./bin/cleanSirach.py xml/36.Sirach.xml  clean/
./bin/cleanPssol.py xml/37.PsSol.xml  clean/
cp xml/38.Hosea.xml clean/34-Hos.xml
cp xml/40.Amos.xml clean/35-Amos.xml
cp xml/39.Micah.xml clean/36-Mic.xml
cp xml/41.Joel.xml clean/37-Joel.xml
cp xml/43.Obadiah.xml clean/38-Obad.xml
cp xml/42.Jonah.xml clean/39-Jonah.xml
cp xml/44.Nahum.xml clean/40-Nah.xml
cp xml/45.Habakkuk.xml clean/41-Hab.xml
cp xml/46.Zeph.xml clean/42-Zeph.xml
cp xml/47.Haggai.xml clean/43-Hag.xml
cp xml/48.Zech.xml clean/44-Zech.xml
cp xml/49.Malachi.xml clean/45-Mal.xml
cp xml/50.Isaiah.xml clean/46-Isa.xml
cp xml/52.Jer.xml clean/47-Jer.xml
cp xml/54.Baruch.xml clean/48-Bar.xml
#cp xml/56.Lam.xml clean/49-Lam-Lam.xml
./bin/cleanLam.py xml/56.Lam.xml  clean
#cp xml/55.EpJer.xml clean/50-EpJer.xml
./bin/cleanEpjer.py xml/55.EpJer.xml clean
cp xml/57.Ezek.xml clean/51-Ezek.xml
#TODO: what about 52 PrAzar the prayer of azariah in the book of daniel ()

#./bin/5-clean-combine-subtype.py xml/63.SusOG.xml  xml1/64.SusTh.xml  specific/
cp  xml/64.SusTh clean/53-SusTh.xml
cp  xml/63.susOG.xml clean/53-SusOG.xml

#./bin/5-clean-combine-subtype.py xml/61.DanielOG.xml  xml1/62.DanielTh.xml  tmp/
cp xml/62.DanielTh.xml clean/54-DanielTh.xml
./bin/cleanDan.py xml/61.DanielOG.xml clean

#./bin/5-clean-combine-subtype.py xml/59.BelOG.xml  xml1/60.BelTh.xml  specific/
cp xml/60.BelTh.xml clean/55-BelTh.xml
cp xml/59.BelOG.xml clean/55-BelOG.xml


#missing 1Enoch 
./bin/cleanOdes.py xml/30.Odes.xml clean/

