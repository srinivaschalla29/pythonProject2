import sys,os
import mysql.connector
#from mysql.connector import Error
class MysqlDatabaseConnection():
    def connect(self,host,username,passwd,database):
        self.host=host
        self.username=username
        self.passwd=passwd
        self.database=database
        self.connection=mysql.connector.connect(host=self.host,username=self.username,passwd=self.passwd,database=self.database)
        self.cursur=self.connection.cursor()