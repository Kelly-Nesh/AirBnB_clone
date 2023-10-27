#!/usr/bin/python3
"""Testing the city module"""

import unittest
import re
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.name = "Toilet"
        self.city.save()

    def test_str_not_none(self):
        self.assertIsNotNone(self.city.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.city), rgx)

    def test_id(self):
        self.assertIsNotNone(self.city.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.city.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.city.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.city.to_dict(), dict)

    def test_save_updated_at(self):
        self.city.save()
        save_1 = self.city.updated_at
        self.city.save()
        save_2 = self.city.updated_at
        self.assertLess(save_1, save_2)
