import sqlite3
from database.database_connection import get_database_connection


class DbServise:
    def __init__(self):

        self._conn = get_database_connection()
    def add_user(self, username, password):
        cursor = self._conn.cursor()
        cursor = self._conn.execute('SELECT * from users where USERNAME="%s" %(username)')
        if cursor.fetchone():
            
            return False
        else:
            query = "INSERT INTO users(username, password) VALUES (?, ?)"
            cursor.execute(query, (username, password))
            self._conn.commit()
            return True
            

    def check_user(self,username, password):

        cursor = self._conn.cursor()
        cursor = self._conn.execute('SELECT * from users where USERNAME="%s" and PASSWORD="%s"'%(username,password))
        if cursor.fetchone():
            
            return True
        else:
            return False
    def all_users(self):

        cursor = self._conn.cursor()
        cursor = self._conn.execute('SELECT * from users')
        rows = cursor.fetchall()
        list = []
        for row in rows:
            list.append(row[0])

        return list



    def delete_all_users(self):
        """
            tyhjentää users taulun
        """
        
        cursor = self._conn.execute("delete from users")
        cursor.execute('delete from users')
        self._conn.commit()    

        
db_servise = DbServise()   



