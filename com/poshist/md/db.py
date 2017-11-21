import sqlite3
import logging
class DB(object):

    dbname='value.DB'
    conn = ''
    cursor=''
    def open(self):
        self.conn=sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
    def close(self):

        self.cursor.close()
        self.conn.close()
    def execute(self,sql):
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
    def query(self,sql):
        print(sql)
        self.cursor.execute(sql)
        values=self.cursor.fetchall()
        return values

