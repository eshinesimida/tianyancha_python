# -*- coding: utf-8 -*-
import MySQLdb
import uuid
import random
#把爬取得数据存储到mysql数据库中
class tianyanchaDAO(object):
    def __init__(self,host="***********",user="****",password="*******", db="*******"
                         ):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
    
    def saveCompanyCommentinfo1(self,items):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,use_unicode=1,charset='utf8')
        cursor = db.cursor()
        for item in items:

            try:
                cursor.execute("insert into tianyan_1(company,code,category,address,range1,ID, tocompany,name, zhuce_money, touzi,percent,"
                               "time,state,href)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,
                               (item["company"],item["code"],item["category"],item["address"],item["range1"],item["ID"] ,item["tocompany"],item["name"],
                                item["zhuce_money"],item["touzi"],item["percent"],item["time"],item["state"],item["href"]))
            except :
                print item
        db.commit()
        cursor.close()
        db.close()
