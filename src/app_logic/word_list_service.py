from entity.user import User

from database.db_service import db_servise as dbs


class WordListService:
    """Sovelluslogiikasta vastaava luokka.

    """

    def __init__(self):
        """Luokan konstruktori.

        Attributes:
            user: Käyttäjän tiedot
            dbs: Tietokantaluokka
            wordlist_info: Tallentaa aktiivisen sanalistan tiedot
            active_wordlist: Nykyinen sanalista
            edit: Onko sanalista editoitavana vai uusi
            active_wordlist_name: Nykyinen sanalistan nimi
            active_wordlist_language: Nykyinen sanalistan kieli
        """
        self.user = None
        self.dbs = dbs
        self.wordlist_info = None

        self.active_wordlist = []
        self.edit = False
        self.active_wordlist_name = ""
        self.active_wordlist_language = ""

    def check_user(self, username, password):
        """Kysyy tietokantaluokalta täsmääkö käyttäjänimi ja salasana.
         Mikäli täsmää asetetaan nykyisen käyttäjän tiedot

        Args:
            username: Käyttäjänimi
            password: Salasana


        Returns: True mikäli täsmää muuten False
        """
        row = self.dbs.check_user(username, password)
        if row:
            self.user = User(row[0], row[1], row[2])
            return True
        return False

    def add_user(self, username, password, is_teacher):
        """Luo uuden käyttäjän. Mikäli uuden käyttäjän
           luominen onnistuu asetetaan nykyisen käyttäjän tiedot

        Args:
            username: Käyttäjänimi
            password: Salasana
            is_teacher: Käyttäjärooli 1 = opettaja 0 = oppilas


        Returns: True mikäli uuden käyttäjän luominen onnistuu muuten False
        """

        if self.dbs.add_user(username, password, is_teacher):
            self.user = User(username, password, is_teacher)
            return True
        return False

    def get_teacher(self):
        """Palautetaan nykyisen käyttäjän käyttäjärooli.

        Returns: 1 = opettaja 0 = oppilas
        """
        return self.user.teacher

    def get_wordlist(self):
        """Palautetaan aktiivinen sanalista.

        Returns: aktiivinen sanalista (active_wordlist)
        """

        return self.active_wordlist

    def get_word_translations_list(self):
        """Palautetaan aktiivisen sanalistan käännökset listana.

        Returns: lista käännöksistä
        """
        wlist = []
        for i in self.active_wordlist:
            wlist.append(i[1])

        return wlist

    def get_wordlist_name(self):
        """Palautetaan aktiivisen sanalistan nimi.

        Returns: aktiivisen sanalistan nimi
        """

        return self.active_wordlist_name

    def get_wordlist_info(self):
        """Hakee tietokannassa olevien sanalistojen nimet ja kielet.

        Returns: Listan tupleja joissa nimet ja kielet
        """

        self.wordlist_info = self.dbs.get_word_lists_info()
        return self.wordlist_info

    def get_wordlists_names(self):
        """Hakee tietokannassa olevien sanalistojen nimet.

        Returns: Sanalistojen nimet tai tyhjä lista
        """

        return self.dbs.get_word_lists_names()

    def get_wordlists_by_language(self, language):

        return self.dbs.get_wordlists_by_language(language)

    def get_wordlist_language(self):
        """Palautetaan aktiivisen sanalistan kieli.

        Returns: aktiivisen sanalistan kieli
        """
        return self.active_wordlist_language

    def reset_active_wordlist(self):
        """Palauttaa alkuasetukset.

        """
        self.active_wordlist = []
        self.edit = False
        self.active_wordlist_name = " "
        self.active_wordlist_language = " "

    def open_active_wordlist(self, name):
        """Avaa aktiivisen sanalistan ja asettaa arvot atribuutteihin

        Args:
            name: Sanalistan nimi
            language: Sanalistan kieli

        """
        self.reset_active_wordlist()
        self.active_wordlist = dbs.get_word_list(name)
        self.edit = True
        self.active_wordlist_name = name
        self.active_wordlist_language = dbs.get_word_list_language(name)

    def save_to_wordlist(self, word, translation, index):
        """Lisää sanan aktiiviseen sanalistaan

        Args:
            word: Lisättävä sana
            translation: Sanan käännös
            index: indeksi sanalistassa

        """

        if index >= len(self.active_wordlist):
            self.active_wordlist.append((word, translation))

        else:
            self.active_wordlist[index] = (word, translation)

    def save_wordlist(self, name, language):
        name = name.capitalize()
        language = language.capitalize()

        creator = self.user.username
        if self.edit == True:
            if self.dbs.check_word_list_name(name):
                return self.dbs.edit_word_list(name, language, self.active_wordlist)

            return self.dbs.add_word_list(name, language, creator, self.active_wordlist)

        return self.dbs.add_word_list(name, language, creator, self.active_wordlist)

    def check_word_list_name(self, name):
        if self.edit:
            return False
        return self.dbs.check_word_list_name(name)

    def save_statistics(self, value):

        self.dbs.save_statistics(
            self.user.username, self.get_wordlist_name(), value)

    def get_statistics(self):

        return self.dbs.get_statistics(self.user.username, self.get_wordlist_name())


word_list_Service = WordListService()
