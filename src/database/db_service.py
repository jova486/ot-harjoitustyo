from datetime import datetime
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
        wlist = []
        for row in rows:
            wlist.append(row[0])

        self._conn.commit()
        return wlist

    def delete_all_users(self):
        """
            tyhjentää users taulun
        """

        self._conn.execute("delete from users")
        self._conn.commit()

    def delete_all_word_lists(self):
        """
            tyhjentää lists taulun
        """

        self._conn.execute("delete from lists")

        self._conn.commit()

    def add_word_list(self, name, language, creator, wlist):

        cursor = self._conn.execute(
            'SELECT * from lists where NAME="%s" %(name)')
        if cursor.fetchone():

            return False
        else:
            data = ""
            for i in wlist:
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
                'UPDATE lists SET language = "%s", data = "%s" where NAME="%s"' % (language, data, name))
            self._conn.commit()

            return True
        else:

            return False

    def get_word_list(self, name, language):
        cursor = self._conn.cursor()

        cursor = self._conn.execute(
            'SELECT data from lists where NAME="%s"' % (name))
        rows = cursor.fetchall()
        wlist = []

        for row in rows:
            a = (row[0].split("\n"))
            for i in a:
                if len(i) > 0:
                    b = i.split(",")
                    wlist.append((b[0], b[1]))

        return wlist

    def get_word_lists_info(self):

        cursor = self._conn.execute('SELECT * from lists')
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append((row[0], row[1]))
        return wlist

    def get_word_lists_names(self):

        cursor = self._conn.execute('SELECT name from lists')
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append(row[0])
        return wlist

    def get_wordlists_by_language(self, language):

        cursor = self._conn.execute(
            'SELECT name from lists where language="%s"' % (language))
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append((row[0]))
        return wlist

    def check_word_list_name(self, name):

        cursor = self._conn.execute(
            'SELECT name from lists where NAME="%s"' % (name))
        if cursor.fetchall():
            return True
        else:
            return False

    def save_statistics(self, user, name, value):

        cursor = self._conn.cursor()
        query = "INSERT INTO stat(user, name ,date, value) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (user, name, datetime.now(), value))
        self._conn.commit()

    def get_statistics(self, user, name):

        cursor = self._conn.execute(
            'SELECT date, value from stat where user="%s" AND name = "%s"' % (user, name))
        rows = cursor.fetchall()
        dates = []
        values = []
        for row in rows:
            dates.append(row[0])
            values.append(row[1]*100)
        zip_iter = zip(dates, values)
        return dict(zip_iter)


db_servise = DbServise()
