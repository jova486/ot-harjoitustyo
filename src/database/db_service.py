import sqlite3
from database.database_connection import get_database_connection


class DbServise:
    def __init__(self):

        self._conn = get_database_connection()

    def add_user(self, username, password, teacher):
        cursor = self._conn.cursor()

        cursor.execute(
            'select * from users where username = "%s"' % (username)
        )
        if cursor.fetchone():
            return False

        else:
            query = "INSERT INTO users(username, password, teacher) VALUES (?, ?, ?)"
            cursor.execute(query, (username, password, teacher))
            self._conn.commit()
            return True

    def check_user(self, username, password):

        cursor = self._conn.cursor()
        cursor = self._conn.execute(
            'SELECT * from users where USERNAME="%s" and PASSWORD="%s"' % (username, password))
        return cursor.fetchone()

    def all_users(self):

        cursor = self._conn.cursor()
        cursor = self._conn.execute('SELECT * from users')
        rows = cursor.fetchall()
        list = []
        for row in rows:
            list.append(row[0])

        self._conn.commit()
        return list

    def delete_all_users(self):
        """
            tyhjentää users taulun
        """

        cursor = self._conn.execute("delete from users")
        cursor.execute('delete from users')
        self._conn.commit()

    def add_word_list(self, name, language, creator, list):
        cursor = self._conn.cursor()
        cursor = self._conn.execute(
            'SELECT * from lists where NAME="%s" %(name)')
        if cursor.fetchone():

            return False
        else:
            data = ""
            for i in list:
                data += i[0]+","+i[1]+"\n"
            if len(data) > 0:
                query = "INSERT INTO lists(name, language,creator,data) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (name, language, creator, data))
                self._conn.commit()
                return True
            else:
                return False

    def edit_word_list(self, name, language, creator, list):
        cursor = self._conn.cursor()
        data = ""
        for i in list:
            data += i[0]+","+i[1]+"\n"
        if len(data) > 0:

            cursor.execute(
                'UPDATE lists SET data = "%s" where NAME="%s"' % (data, name))
            self._conn.commit()

            return True
        else:

            return False

    def get_word_list(self, name, language):
        cursor = self._conn.cursor()

        cursor = self._conn.execute(
            'SELECT data from lists where NAME="%s" and language="%s"' % (name, language))
        rows = cursor.fetchall()
        list = []

        for row in rows:
            a = (row[0].split("\n"))
            for i in a:
                if len(i) > 0:
                    b = i.split(",")
                    list.append((b[0], b[1]))

        return list

    def get_word_list_names(self):
        cursor = self._conn.cursor()
        cursor = self._conn.execute('SELECT * from lists')
        rows = cursor.fetchall()
        list = []
        for row in rows:
            list.append((row[0], row[1]))
        return list

    def check_word_list_name(self, name):

        cursor = self._conn.execute(
            'SELECT name from lists where NAME="%s"' % (name))
        if cursor.fetchall():
            return True
        else:
            return False


db_servise = DbServise()
