import unittest
from database.db_service import (
    db_servise as dbs
)
from app_logic.word_list_service import (
    word_list_Service as wls
)

from entity.user import User


class TestServise(unittest.TestCase):
    """TestiLuokka, sovelluslogiikan testejä.

    """

    def setUp(self):
        """Testit alustava metodi.

        Args:
            self
        """
        dbs.delete_all_users()
        dbs.delete_all_word_lists()
        dbs.delete_all_stat()
        self.user_joppe = User('joppe', 'salasana', 1)

    def setUpWordLists(self):
        """tallentaa tietokantaan sanalistat testejä varten.

        Args:
            self
        """


        wlist = [("yksi", "one"), ("kaksi", "two")]
        for i, entry in enumerate(wlist):
            wls.save_to_wordlist(entry[0], entry[1], i)
        wls.save_wordlist("Test1", "Englanti")

        wlist = [("kolme", "tres"), ("neljä", "cuatro")]
        for i, entry in enumerate(wlist):
            wls.save_to_wordlist(entry[0], entry[1], i)
        wls.save_wordlist("Test2", "Espanja")

    def test_create_user(self):
        """tallentaa tietokantaan käyttäjän ja tarkistaa onko käyttäjänimi tallentunut.

        Args:
            self
        """
        self.assertTrue(wls.add_user(self.user_joppe.username,
                                     self.user_joppe.password, self.user_joppe.teacher))

        self.assertTrue(wls.check_user(self.user_joppe.username,
                                       self.user_joppe.password))

    def test_create_user_exists(self):
        """tallentaa tietokantaan käyttäjän ja yrittää tallentaa saman käyttäjän uudelleen.

        Args:
            self
        """
        self.assertTrue(wls.add_user(self.user_joppe.username,
                                     self.user_joppe.password, self.user_joppe.teacher))

        self.assertFalse(wls.add_user(self.user_joppe.username,
                                     self.user_joppe.password, self.user_joppe.teacher))

    def test_check_user_not_exist(self):
        """Testaa palauttaako check_user False jos käyttäjää ei ole tietokannassa.

        Args:
            self
        """

        self.assertFalse(wls.check_user("Kaaleppi",
                                        "qwerty"))

    def test_check_get_teacher(self):
        """Testaa get_teacher metodilla käyttäjästatus tallentunut oikein.

        Args:
            self
        """
        self.assertTrue(wls.add_user(self.user_joppe.username,
                                     self.user_joppe.password, self.user_joppe.teacher))

        self.assertEqual(wls.get_teacher(), 1)

        self.assertTrue(wls.add_user("Kaapo",
                                     "salasana", 0))

        self.assertEqual(wls.get_teacher(), 0)



    def test_get_wordlists_names(self):

        """Testaa paluttaako get_wordlists_names tallennettujen sanalistojen nimet.

        Args:
            self
        """
        self.setUpWordLists()

        self.assertEqual(wls.get_wordlists_names(), ["Test1","Test2"])

    def test_get_active_wordlists_name(self):

        """Testaa paluttaako get_wordlist_name oikean listan nimen.

        Args:
            self
        """
        self.setUpWordLists()

        wls.open_active_wordlist("Test2")
        self.assertEqual(wls.get_wordlist_name(), "Test2")

    def test_get_wordlist(self):

        """Testaa paluttaako get_wordlist oikein aktiivisen listan.

        Args:
            self
        """
        self.setUpWordLists()

        wls.open_active_wordlist("Test2")
        self.assertEqual(wls.get_wordlist(), [("kolme", "tres"), ("neljä", "cuatro")])



    def test_get_wordlist_info(self):
        """Testaa paluttaako get_wordlist_info oikein sanalistojen nimet ja kielet.

        Args:
            self
        """
        self.setUpWordLists()

        self.assertEqual(wls.get_wordlist_info(), [
                         ("Test1", "Englanti"), ("Test2", "Espanja")])

    def test_get_wordlist_info_for_empty(self):
        wlist = []
        self.assertEqual(wls.get_wordlist_info(), wlist)



    def test_get_word_translations_list(self):

        self.setUpWordLists()
        wls.open_active_wordlist("Test1")

        self.assertEqual(wls.get_word_translations_list(), ["one", "two"])

    def test_get_wordlists_by_language(self):

        self.setUpWordLists()
        self.assertEqual(wls.get_wordlists_by_language("Espanja"), ["Test2"])

    def test_get_wordlist_language(self):

        self.setUpWordLists()
        wls.open_active_wordlist("Test2")

        self.assertEqual(wls.get_wordlist_language(), "Espanja")

    def test_save_statistics(self):
        """Testaa tuloksien tallentamisen ja avaamisen

        Args:
            self
        """
        wls.add_user(self.user_joppe.username,
                                     self.user_joppe.password, 0)
        self.setUpWordLists()
        wls.open_active_wordlist("Test2")


        tulokset = [8, 6, 8, 9]
        for i in tulokset:
            wls.save_statistics(i/10)

        result = wls.get_statistics()
        verify = []
        for i in result.values():
            verify.append(i/10)
        self.assertEqual(verify, tulokset)





