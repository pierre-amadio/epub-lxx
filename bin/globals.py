#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#needs 2 chapter (toc&forewords) before the actual content.
indexOffset=3

bookInfo=[]
bookInfo.append({'id': 'Gen', 'prefix': '01', 'postfix': ''})
bookInfo.append({'id': 'Exod', 'prefix': '02', 'postfix': ''})
bookInfo.append({'id': 'Lev', 'prefix': '03', 'postfix': ''})
bookInfo.append({'id': 'Num', 'prefix': '04', 'postfix': ''})
bookInfo.append({'id': 'Deut', 'prefix': '05', 'postfix': ''})
bookInfo.append({'id': 'Josh', 'prefix': '06', 'postfix': 'A'})
bookInfo.append({'id': 'Josh', 'prefix': '06', 'postfix': 'B'})
bookInfo.append({'id': 'Judg', 'prefix': '07', 'postfix': 'A'})
bookInfo.append({'id': 'Judg', 'prefix': '07', 'postfix': 'B'})
bookInfo.append({'id': 'Ruth', 'prefix': '08', 'postfix': ''})
bookInfo.append({'id': '1Sam', 'prefix': '09', 'postfix': ''})
bookInfo.append({'id': '2Sam', 'prefix': '10', 'postfix': ''})
bookInfo.append({'id': '1Kgs', 'prefix': '11', 'postfix': ''})
bookInfo.append({'id': '2Kgs', 'prefix': '12', 'postfix': ''})
bookInfo.append({'id': '1Chr', 'prefix': '13', 'postfix': ''})
bookInfo.append({'id': '2Chr', 'prefix': '14', 'postfix': ''})
bookInfo.append({'id': '1Esd', 'prefix': '15', 'postfix': ''})
bookInfo.append({'id': 'Ezra', 'prefix': '16', 'postfix': ''})
bookInfo.append({'id': 'Neh', 'prefix': '17', 'postfix': ''})
bookInfo.append({'id': 'Esth', 'prefix': '18', 'postfix': ''})
bookInfo.append({'id': 'Jdt', 'prefix': '19', 'postfix': ''})
bookInfo.append({'id': 'Tob', 'prefix': '20', 'postfix': 'BA'})
bookInfo.append({'id': 'Tob', 'prefix': '20', 'postfix': 'S'})
bookInfo.append({'id': '1Macc', 'prefix': '21', 'postfix': ''})
bookInfo.append({'id': '2Macc', 'prefix': '22', 'postfix': ''})
bookInfo.append({'id': '3Macc', 'prefix': '23', 'postfix': ''})
bookInfo.append({'id': '4Macc', 'prefix': '24', 'postfix': ''})
bookInfo.append({'id': 'Ps', 'prefix': '25', 'postfix': ''})
bookInfo.append({'id': 'Prov', 'prefix': '27', 'postfix': ''})
bookInfo.append({'id': 'Eccl', 'prefix': '28', 'postfix': ''})
bookInfo.append({'id': 'Song', 'prefix': '29', 'postfix': ''})
bookInfo.append({'id': 'Job', 'prefix': '30', 'postfix': ''})
bookInfo.append({'id': 'Wis', 'prefix': '31', 'postfix': ''})
bookInfo.append({'id': 'Sir', 'prefix': '32', 'postfix': ''})
bookInfo.append({'id': 'PssSol', 'prefix': '33', 'postfix': ''})
bookInfo.append({'id': 'Hos', 'prefix': '34', 'postfix': ''})
bookInfo.append({'id': 'Amos', 'prefix': '35', 'postfix': ''})
bookInfo.append({'id': 'Mic', 'prefix': '36', 'postfix': ''})
bookInfo.append({'id': 'Joel', 'prefix': '37', 'postfix': ''})
bookInfo.append({'id': 'Obad', 'prefix': '38', 'postfix': ''})
bookInfo.append({'id': 'Jonah', 'prefix': '39', 'postfix': ''})
bookInfo.append({'id': 'Nah', 'prefix': '40', 'postfix': ''})
bookInfo.append({'id': 'Hab', 'prefix': '41', 'postfix': ''})
bookInfo.append({'id': 'Zeph', 'prefix': '42', 'postfix': ''})
bookInfo.append({'id': 'Hag', 'prefix': '43', 'postfix': ''})
bookInfo.append({'id': 'Zech', 'prefix': '44', 'postfix': ''})
bookInfo.append({'id': 'Mal', 'prefix': '45', 'postfix': ''})
bookInfo.append({'id': 'Isa', 'prefix': '46', 'postfix': ''})
bookInfo.append({'id': 'Jer', 'prefix': '47', 'postfix': ''})
bookInfo.append({'id': 'Bar', 'prefix': '48', 'postfix': ''})
bookInfo.append({'id': 'Lam', 'prefix': '49', 'postfix': ''})
bookInfo.append({'id': 'EpJer', 'prefix': '50', 'postfix': ''})
bookInfo.append({'id': 'Ezek', 'prefix': '51', 'postfix': ''})
bookInfo.append({'id': 'Sus', 'prefix': '53', 'postfix': 'OG'})
bookInfo.append({'id': 'Sus', 'prefix': '53', 'postfix': 'Th'})
bookInfo.append({'id': 'Dan', 'prefix': '54', 'postfix': 'OG'})
bookInfo.append({'id': 'Dan', 'prefix': '54', 'postfix': 'Th'})
bookInfo.append({'id': 'Bel', 'prefix': '55', 'postfix': 'OG'})
bookInfo.append({'id': 'Bel', 'prefix': '55', 'postfix': 'Th'})
bookInfo.append({'id': 'Odes', 'prefix': '57', 'postfix': ''})

def getBookIndex(id,prefix,postfix):
    cnt=0
    for i in bookInfo:
        if(id==i["id"] and prefix==i['prefix'] and postfix==i["postfix"]):
                return cnt
        cnt+=1

