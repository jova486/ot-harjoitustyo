import unittest
from database.db_service import (
    db_servise as dbs
)

from entity.user import User


class TestDbServise(unittest.TestCase):
    """TestiLuokka, jossa tietokantahakuihin liittyvät testit.

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

    def test_create_user(self):
        """Testaa onnistuuko käyttäjän lisääminen.

        Args:
            self
        """
        dbs.add_user(self.user_joppe.username,
                     self.user_joppe.password, self.user_joppe.teacher)
        users = dbs.all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0], self.user_joppe.username)

    def test_create_user_exists(self):
        """Testaa löytyykö lisätty käyttäjä.

        Args:
            self
        """
        dbs.add_user(self.user_joppe.username,
                     self.user_joppe.password, self.user_joppe.teacher)

        self.assertFalse(dbs.add_user(self.user_joppe.username,
                                      self.user_joppe.password, self.user_joppe.teacher))

    def test_check_user_not_exist(self):
        """Testaa löytyykö lisäämätön käyttäjä check_user metodilla.

        Args:
            self
        """
        result = dbs.check_user(self.user_joppe.username,
                                self.user_joppe.password)
        self.assertEqual(result, None)

    def test_check_user_exist(self):
        """Testaa löytyykö lisätty käyttäjä check_user metodilla. Lisätään käyttäjä metodilla add_user ja
        testataan löytyykö tietokannasta käyttäjänimi check_user metodilla.

        Args:
            self
        """
        dbs.add_user(self.user_joppe.username,
                     self.user_joppe.password, self.user_joppe.teacher)
        result = dbs.check_user(self.user_joppe.username,
                                self.user_joppe.password)
        self.assertEqual(result[0], self.user_joppe.username)

    def test_add_empty_word_list(self):
        """Testaa paluttaako sanalistan tallentava metodi False
           mikäli tallennettava sanalista on tyhjä.

        Args:
            self
        """
        name = "testi"
        wlist = []

        self.assertFalse(dbs.add_word_list(
            name, "English", self.user_joppe.username, wlist))

    def test_add_not_empty_word_list(self):
        """Testaa paluttaako sanalistan tallentava metodi True
           mikäli tallennettava sanalista on asianmukainen.

        Args:
            self
        """
        name = "testi"
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        self.assertTrue(dbs.add_word_list(
            name, "English", self.user_joppe.username, wlist))

    def test_add_two_list_with_same_name(self):
        """Testaa paluttaako sanalistan tallentava metodi False
           mikäli yritetään tallentaa kaksi saman nimistä listaa.

        Args:
            self
        """
        name = "testi"
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        dbs.add_word_list(name, "English", self.user_joppe.username, wlist)
        self.assertFalse(dbs.add_word_list(
            name, "English", self.user_joppe.username, wlist))

    def test_get_word_lists_names(self):
        """Testaa ovatko sanalistat tallentuneet ja palutuvatko oikeat nimet

        Args:
            self
        """
        names = ["testi1", "testi2"]
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        dbs.add_word_list(names[0], "English", self.user_joppe.username, wlist)
        dbs.add_word_list(names[1], "English", self.user_joppe.username, wlist)
        self.assertEqual(dbs.get_word_lists_names(), names)

    def test_edit_word_list(self):
        """Testaa korvautuuko sanalista oikein

        Args:
            self
        """
        name = "testi"
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        wlist2 = [("neljä", "four"), ("viisi", "five"), ("kuusi", "six")]
        dbs.add_word_list(name, "English", self.user_joppe.username, wlist)
        dbs.edit_word_list(name, "English", wlist2)
        self.assertEqual(dbs.get_word_list(name, "English"), wlist2)

    def test_edit_word_list_empty(self):
        """Testaa paluttaako tyhlä lista False

        Args:
            self
        """
        name = "testi"
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        wlist2 = []
        dbs.add_word_list(name, "English", self.user_joppe.username, wlist)
        self.assertFalse(dbs.edit_word_list(name, "English", wlist2))

    def test_get_wordlists_by_language(self):
        """Testaa onko kielen perusteella palautuva lista oikein

        Args:
            self
        """
        names = ["testi1", "testi2", "testi3", "testi4"]
        wlist = [("yksi", "one")]
        languages = ["Englanti", "Ruotsi", "Englanti", "Ruotsi"]
        for i, name in enumerate(names):
            dbs.add_word_list(
                name, languages[i], self.user_joppe.username, wlist)
        self.assertEqual(dbs.get_wordlists_by_language(
            "Englanti"), ["testi1", "testi3"])

    def test_save_statistics(self):
        """Testaa talentuvatko tulokset oikein

        Args:
            self
        """

        tulokset = [8, 6, 8, 9]
        for i in tulokset:
            dbs.save_statistics(self.user_joppe.username, "testi1", i/10)

        result = dbs.get_statistics(self.user_joppe.username, "testi1")
        verify = []
        for i in result.values():
            verify.append(i/10)
        self.assertEqual(verify, tulokset)
