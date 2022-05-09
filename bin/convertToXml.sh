#!/bin/bash
rm -rf xml
mkdir xml
./bin/imp2xml.py imp/01.Gen.1.imp imp/02.Gen.2.imp > xml/01-Gen.xml
./bin/imp2xml.py imp/03.Exod.imp > xml/03.Exod.xml
./bin/imp2xml.py imp/04.Lev.imp > xml/04.Lev.xml
./bin/imp2xml.py imp/05.Num.imp > xml/05.Num.xml
./bin/imp2xml.py imp/06.Deut.imp > xml/06.Deut.xml
./bin/imp2xml.py imp/07.JoshB.imp > xml/07.JoshB.xml
./bin/imp2xml.py imp/08.JoshA.imp > xml/08.JoshA.xml
./bin/imp2xml.py imp/09.JudgesB.imp > xml/09.JudgesB.xml
./bin/imp2xml.py imp/10.JudgesA.imp > xml/10.JudgesA.xml
./bin/imp2xml.py imp/11.Ruth.imp > xml/11.Ruth.xml
./bin/imp2xml.py imp/12.1Sam.imp > xml/12.1Sam.xml
./bin/imp2xml.py imp/13.2Sam.imp   > xml/13.2Sam.xml
./bin/imp2xml.py imp/14.1Kings.imp > xml/14.1Kings.xml
./bin/imp2xml.py imp/15.2Kings.imp > xml/15.2Kings.xml
./bin/imp2xml.py imp/16.1Chron.imp > xml/16.1Chron.xml
./bin/imp2xml.py imp/17.2Chron.imp > xml/17.2Chron.xml
./bin/imp2xml.py imp/18.1Esdras.imp > xml/18.1Esdras.xml
./bin/imp2xml.py imp/19.2Esdras.imp > xml/19.2Esdras.xml
./bin/imp2xml.py imp/20.Esther.imp > xml/20.Esther.xml
./bin/imp2xml.py imp/21.Judith.imp > xml/21.Judith.xml
./bin/imp2xml.py imp/22.TobitBA.imp > xml/22.TobitBA.xml
./bin/imp2xml.py imp/23.TobitS.imp > xml/23.TobitS.xml
./bin/imp2xml.py imp/24.1Macc.imp > xml/24.1Macc.xml
./bin/imp2xml.py imp/25.2Macc.imp > xml/25.2Macc.xml
./bin/imp2xml.py imp/26.3Macc.imp > xml/26.3Macc.xml
./bin/imp2xml.py imp/27.4Macc.imp > xml/27.4Macc.xml
./bin/imp2xml.py imp/28.Psalms1.imp imp/29.Psalms2.imp > xml/28.Psalms.xml
./bin/imp2xml.py imp/30.Odes.imp > xml/30.Odes.xml
./bin/imp2xml.py imp/31.Proverbs.imp > xml/31.Proverbs.xml
./bin/imp2xml.py imp/32.Qoheleth.imp > xml/32.Qoheleth.xml
./bin/imp2xml.py imp/33.Canticles.imp > xml/33.Canticles.xml
./bin/imp2xml.py imp/34.Job.imp > xml/34.Job.xml
./bin/imp2xml.py imp/35.Wisdom.imp > xml/35.Wisdom.xml
./bin/imp2xml.py imp/36.Sirach.imp > xml/36.Sirach.xml
./bin/imp2xml.py imp/37.PsSol.imp > xml/37.PsSol.xml
./bin/imp2xml.py imp/38.Hosea.imp > xml/38.Hosea.xml
./bin/imp2xml.py imp/39.Micah.imp > xml/39.Micah.xml
./bin/imp2xml.py imp/40.Amos.imp > xml/40.Amos.xml
./bin/imp2xml.py imp/41.Joel.imp > xml/41.Joel.xml
./bin/imp2xml.py imp/42.Jonah.imp > xml/42.Jonah.xml
./bin/imp2xml.py imp/43.Obadiah.imp > xml/43.Obadiah.xml
./bin/imp2xml.py imp/44.Nahum.imp > xml/44.Nahum.xml
./bin/imp2xml.py imp/45.Habakkuk.imp > xml/45.Habakkuk.xml
./bin/imp2xml.py imp/46.Zeph.imp > xml/46.Zeph.xml
./bin/imp2xml.py imp/47.Haggai.imp > xml/47.Haggai.xml
./bin/imp2xml.py imp/48.Zech.imp > xml/48.Zech.xml
./bin/imp2xml.py imp/49.Malachi.imp > xml/49.Malachi.xml
./bin/imp2xml.py imp/50.Isaiah1.imp imp/51.Isaiah2.imp> xml/50.Isaiah.xml
./bin/imp2xml.py imp/52.Jer1.imp imp/53.Jer2.imp> xml/52.Jer.xml
./bin/imp2xml.py imp/54.Baruch.imp > xml/54.Baruch.xml
./bin/imp2xml.py imp/55.EpJer.imp > xml/55.EpJer.xml
./bin/imp2xml.py imp/56.Lam.imp > xml/56.Lam.xml
./bin/imp2xml.py imp/57.Ezek1.imp imp/58.Ezek2.imp > xml/57.Ezek.xml
./bin/imp2xml.py imp/59.BelOG.imp > xml/59.BelOG.xml
./bin/imp2xml.py imp/60.BelTh.imp > xml/60.BelTh.xml
./bin/imp2xml.py imp/61.DanielOG.imp > xml/61.DanielOG.xml
./bin/imp2xml.py imp/62.DanielTh.imp > xml/62.DanielTh.xml
./bin/imp2xml.py imp/63.SusOG.imp > xml/63.SusOG.xml
./bin/imp2xml.py imp/64.SusTh.imp > xml/64.SusTh.xml

