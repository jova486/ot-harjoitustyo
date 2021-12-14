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
        self.user_Joppe = User('joppe', 'salasana', 1)

    def test_create_user(self):
        """Testaa onnistuuko käyttäjän lisääminen.

        Args:
            self
        """
        dbs.add_user(self.user_Joppe.username,
                     self.user_Joppe.password, self.user_Joppe.teacher)
        users = dbs.all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0], self.user_Joppe.username)

    def test_create_user_exists(self):
        """Testaa löytyykö lisätty käyttäjä.

        Args:
            self
        """
        dbs.add_user(self.user_Joppe.username,
                     self.user_Joppe.password, self.user_Joppe.teacher)

        self.assertFalse(dbs.add_user(self.user_Joppe.username,
                                      self.user_Joppe.password, self.user_Joppe.teacher))

    def test_check_user_not_exist(self):
        """Testaa löytyykö lisäämätön käyttäjä check_user metodilla.

        Args:
            self
        """
        result = dbs.check_user(self.user_Joppe.username,
                                self.user_Joppe.password)
        self.assertEqual(result, None)

    def test_check_user_exist(self):
        """Testaa löytyykö lisätty käyttäjä check_user metodilla. Lisätään käyttäjä metodilla add_user ja
        testataan löytyykö tietokannasta käyttäjänimi check_user metodilla.

        Args:
            self
        """
        dbs.add_user(self.user_Joppe.username,
                     self.user_Joppe.password, self.user_Joppe.teacher)
        result = dbs.check_user(self.user_Joppe.username,
                                self.user_Joppe.password)
        self.assertEqual(result[0], self.user_Joppe.username)

    def test_add_empty_word_list(self):
        """Testaa paluttaako sanalistan tallentava metodi False
           mikäli tallennettava sanalista on tyhjä.

        Args:
            self
        """
        name = "testi"
        wlist = []

        self.assertFalse(dbs.add_word_list(
            name, "English", self.user_Joppe.username, wlist))

    def test_add_not_empty_word_list(self):
        """Testaa paluttaako sanalistan tallentava metodi True
           mikäli tallennettava sanalista on asianmukainen.

        Args:
            self
        """
        name = "testi"
        wlist = [("yksi", "one"), ("kaksi", "two"), ("kolme", "tree")]
        self.assertTrue(dbs.add_word_list(
            name, "English", self.user_Joppe.username, wlist))
