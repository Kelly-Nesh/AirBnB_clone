#!/usr/bin/python3
"""Testing the place module"""

import unittest
import re
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.name = "Toilet"
        self.place.save()

    def test_str_not_none(self):
        self.assertIsNotNone(self.place.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.place), rgx)

    def test_id(self):
        self.assertIsNotNone(self.place.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.place.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.place.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.place.to_dict(), dict)

    def test_save_updated_at(self):
        self.place.save()
        save_1 = self.place.updated_at
        self.place.save()
        save_2 = self.place.updated_at
        self.assertLess(save_1, save_2)
