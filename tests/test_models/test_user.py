#!/usr/bin/python3
"""Testing the user module"""

import unittest
import re
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.name = "Toilet"
        self.user.save()
    def test_str_not_none(self):
        self.assertIsNotNone(self.user.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.user), rgx)

    def test_id(self):
        self.assertIsNotNone(self.user.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.user.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.user.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.user.to_dict(), dict)

    def test_save_updated_at(self):
        self.user.save()
        save_1 = self.user.updated_at 
        self.user.save()
        save_2 = self.user.updated_at
        self.assertLess(save_1, save_2)
