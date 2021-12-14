import unittest
from database.db_service import (
    db_servise as dbs
)
from app_logic.wordList_service import (
    word_list_Service as wls
)

from entity.user import User


class TestServise(unittest.TestCase):
    def setUp(self):
        dbs.delete_all_users()
        dbs.delete_all_word_lists()
        self.user_Joppe = User('joppe', 'salasana', 1)

    def setUpWordlists(self):
        wlist = [("yksi", "one"), ("kaksi", "two")]
        for i, l in enumerate(wlist):
            wls.save_to_wordlist(l[0], l[1], i)
        wls.save_wordlist("Test", "English")

        wlist = [("kolme", "tree"), ("neljä", "four")]
        for i, l in enumerate(wlist):
            wls.save_to_wordlist(l[0], l[1], i)
        wls.save_wordlist("Test2", "English")


    def test_create_user(self):

        self.assertTrue(wls.add_user(self.user_Joppe.username,
                                     self.user_Joppe.password, self.user_Joppe.teacher))

        self.assertTrue(wls.check_user(self.user_Joppe.username,
                                       self.user_Joppe.password))

    def test_check_user_not_exist(self):

        self.assertFalse(wls.check_user("Kaaleppi",
                                        "qwerty"))

    def test_check_get_teacher(self):
        self.assertTrue(wls.add_user(self.user_Joppe.username,
                                     self.user_Joppe.password, self.user_Joppe.teacher))

        self.assertEqual(wls.get_teacher(), 1)

    def test_check_get_teacher2(self):
        self.assertTrue(wls.add_user(self.user_Joppe.username,
                                     self.user_Joppe.password, self.user_Joppe.teacher))

        self.assertNotEqual(wls.get_teacher(), 0)

    def test_get_active_wordlists_name(self):
        self.setUpWordlists()

        wls.open_active_wordlist("Test2", "English")
        self.assertEqual(wls.get_wordlist_name(), "Test2")

    def test_get_wordlist_info(self):
        self.setUpWordlists()

        self.assertEqual(wls.get_wordlist_info(), [
                         ("Test", "English"), ("Test2", "English")])

    def test_get_wordlist_info_for_empty(self):
        wlist = []
        self.assertEqual(wls.get_wordlist_info(), wlist)

    def test_get_word_translations_list(self):

        self.setUpWordlists()
        wls.open_active_wordlist("Test", "English")

        self.assertEqual(wls.get_word_translations_list(), ["one", "two"])
