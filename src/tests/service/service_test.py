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
        self.user_Joppe = User('joppe', 'salasana', 1)
        '''list = [("leipä","bread"),("voi","butter")]
        for i,l in enumerate(list):
            wls.save_to_wordlist(l[0], l[1], i)
        wls.save_wordlist("Test")'''

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
