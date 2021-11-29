import unittest
from database.db_service import (
    db_servise as dbs
)

from entity.user import User


class TestDbServise(unittest.TestCase):
    def setUp(self):
        dbs.delete_all_users()
        self.user_Joppe = User('joppe', 'salasana', 1)

    def test_create_user(self):
        dbs.add_user(self.user_Joppe.username,
                     self.user_Joppe.password, self.user_Joppe.teacher)
        users = dbs.all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0], self.user_Joppe.username)

    def test_check_user_not_exist(self):

        result = dbs.check_user(self.user_Joppe.username,
                                self.user_Joppe.password)
        self.assertEqual(result, None)

    def test_check_user_exist(self):
        dbs.add_user(self.user_Joppe.username,
                     self.user_Joppe.password, self.user_Joppe.teacher)
        result = dbs.check_user(self.user_Joppe.username,
                                self.user_Joppe.password)
        self.assertEqual(result[0], self.user_Joppe.username)