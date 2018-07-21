# -*- coding: utf-8 -*-
from pymongo import MongoClient

def Connectors():
    s1 = set()
    connection = MongoClient('192.168.235.55', 27017)
    db = connection.admin
    db.authenticate("admin", "123456")
    db = connection.team_behind_sc
    post_sub = db.Filmmaker_page
    # 連接數據庫
    cur = post_sub.find()
    for c in cur:
        try:
            for i in c['演员'].keys():
                k = c['演员'][i]
                s = k.replace(' ', '.') + 'details.html'
                s1.add(s)
        except:
            pass
    return s1

if __name__ == '__main__':
    s1 = Connectors()
    print(len(s1))