from datetime import datetime
from database.database_connection import get_database_connection


class DbServise:
    """Tietokannatahauista vastaava luokka.

    """
    def __init__(self):
        """Luokan konstruktori.

        Attributes:
            self._conn: Tietokantayhteys
        """

        self._conn = get_database_connection()

    def add_user(self, username, password, teacher):
        """Tarkistaa onko käyttäjänimi käytössä ja lisää käyttäjän tietokantaan mikäli käyttäjänimi on vapaa.

        Args:
            username: Käyttäjänimi
            password: Salasana
            teacher: 1 = opettaja, 0 = oppilas

        Returns: True mikäli käyttäjän lisääminen onnistuu muuten False
        """
        cursor = self._conn.cursor()

        cursor.execute(
            'select * from users where username = "%s"' % (username)
        )
        if cursor.fetchone():
            return False

        query = "INSERT INTO users(username, password, teacher) VALUES (?, ?, ?)"
        cursor.execute(query, (username, password, teacher))
        self._conn.commit()
        return True

    def check_user(self, username, password):
        """Tarkistaa onko käyttäjänimi tietokannassa.

        Args:
            username: Käyttäjänimi
            password: Salasana

        Returns: Tietokantahaun tulos
        """

        cursor = self._conn.execute(
            'SELECT * from users where USERNAME="%s" and PASSWORD="%s"' % (username, password))
        return cursor.fetchone()

    def all_users(self):
        """Hakee kaikki käyttäjänimet (Luultavasti turha ohjelman toiminnan kannalta)

        Returns: Tietokantahaun tulos
        """

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
        """Tyhjentää tietokantataulun lists

        """

        self._conn.execute("delete from lists")
        self._conn.commit()

    def add_word_list(self, name, language, creator, wlist):
        """Tarkistaa onko sanalistan nimi käytössä ja lisää sanalistan.

        Args:
            name: Sanalistan nimi
            language: Sanalistan kieli
            creator: Sanalistan tekijä
            wlist: Sanalistan sanat

        Returns: True mikäli Sanalistan lisääminen onnistuu muuten False
        """

        cursor = self._conn.execute(
            'SELECT * from lists where NAME="%s" %(name)')
        if cursor.fetchone():

            return False
        data = ""
        for i in wlist:
            data += i[0]+","+i[1]+"\n"
        if len(data) > 0:
            query = "INSERT INTO lists(name, language,creator,data) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (name, language, creator, data))
            self._conn.commit()
            return True
        return False

    def edit_word_list(self, name, language, creator, list):
        """Päivittää olemassa olevan sanalistan.

        Args:
            name: Sanalistan nimi
            language: Sanalistan kieli
            creator: Sanalistan tekijä
            wlist: Sanalistan sanat

        Returns: True mikäli Sanalistan päivittäminen onnistuu muuten False
        """
        cursor = self._conn.cursor()
        data = ""
        for i in list:
            data += i[0]+","+i[1]+"\n"
        if len(data) > 0:

            cursor.execute(
                'UPDATE lists SET language = "%s", data = "%s" where NAME="%s"' % (language, data, name))
            self._conn.commit()

            return True
        return False

    def get_word_list(self, name, language):
        """Hakee sanalistan nimen mukaan.

        Args:
            name: Sanalistan nimi
            language: Sanalistan kieli

        Returns: Paluttaa sanalistan. Mikäli listaa ei ole palutetaan tyhjä lista.
        """
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
        """Hakee tietokannassa olevien sanalistojen nimet ja kielet.

        Returns: Listan tupleja joissa nimet ja kielet
        """

        cursor = self._conn.execute('SELECT * from lists')
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append((row[0], row[1]))
        return wlist

    def get_word_lists_names(self):
        """Hakee tietokannassa olevien sanalistojen nimet.

        Returns: Sanalistojen nimet tai tyhjä lista
        """

        cursor = self._conn.execute('SELECT name from lists')
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append(row[0])
        return wlist

    def get_wordlists_by_language(self, language):
        """Hakee tietokannassa olevien sanalistojen nimet.
        Args:
            language: Haettavan sanalistan kieli

        Returns: Sanalistojen nimet kielen perusteella tai tyhjä lista
        """

        cursor = self._conn.execute(
            'SELECT name from lists where language="%s"' % (language))
        rows = cursor.fetchall()
        wlist = []
        for row in rows:
            wlist.append((row[0]))
        return wlist

    def check_word_list_name(self, name):
        """Tarkistaa onko sanalistan nimi tietokannassa.
        Args:
            language: Haettavan sanalistan kieli

        Returns: Sanalistojen nimet tai tyhjä lista
        """

        cursor = self._conn.execute(
            'SELECT name from lists where NAME="%s"' % (name))
        if cursor.fetchall():
            return True
        return False

    def save_statistics(self, user, name, value):
        """Tallentaa tietojantaan tehdyn harjoituksen tuloksen

        Args:
            user: Käyttäjänimi
            name: Sanalistan nimi
            value: Tallennettava arvo

        """

        cursor = self._conn.cursor()
        query = "INSERT INTO stat(user, name ,date, value) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (user, name, datetime.now(), value))
        self._conn.commit()

    def get_statistics(self, user, name):
        """Hakee tietokannasta käyttäjän tietyn harjoituksen tulokset

        Args:
            user: Käyttäjänimi
            name: Sanalistan nimi

        Returns: dictionary jossa päivämäärät ja tulokset
        """

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
