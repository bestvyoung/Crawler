# -*- coding: utf-8 -*-
import MySQLdb
from scrapy.utils.project import get_project_settings #导入seetings配置

class DBHelper():
    
    
    def __init__(self):
    #    self.settings=get_project_settings()
        
        self.host='127.0.0.1'
        self.port='3306'
        self.user='root'
        self.passwd=''
        self.db='NYOJ'
    
    def connectMysql(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             charset='utf8')
        return conn
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8')
        return conn   
    
    
    def createDatabase(self):
        '''因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不要传sql语句了'''
        conn=self.connectMysql()
        
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    
    def insert(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        

'''测试DBHelper的类'''
class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
               
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 
    def testCreateTable(self):
        sql="create table testtable(id int primary key auto_increment,name varchar(50),url varchar(200))"
        self.dbHelper.createTable(sql)
    
    def testInsert(self):
        sql="insert into testtable(name,url) values(%s,%s)"
        params=("test","test")
        self.dbHelper.insert(sql,*params) 
    def testUpdate(self):
        sql="update testtable set name=%s,url=%s where id=%s"
        params=("update","update","1")
        self.dbHelper.update(sql,*params)
    
    def testDelete(self):
        sql="delete from testtable where id=%s"
        params=("1")
        self.dbHelper.delete(sql,*params)
    
testDBHelper = TestDBHelper()
    #testDBHelper.testCreateDatebase()  #执行测试创建数据库
    #testDBHelper.testCreateTable()     #执行测试创建表
testDBHelper.testInsert()          #执行测试插入数据
    #testDBHelper.testUpdate()          #执行测试更新数据
    #testDBHelper.testDelete()          #执行测试删除数据
