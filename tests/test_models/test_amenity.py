#!/usr/bin/python3
"""Testing the amenity module"""

import unittest
import re
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.name = "Toilet"
        self.amenity.save()
    def test_str_not_none(self):
        self.assertIsNotNone(self.amenity.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.amenity), rgx)

    def test_id(self):
        self.assertIsNotNone(self.amenity.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.amenity.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.amenity.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.amenity.to_dict(), dict)

    def test_save_updated_at(self):
        self.amenity.save()
        save_1 = self.amenity.updated_at 
        self.amenity.save()
        save_2 = self.amenity.updated_at
        self.assertLess(save_1, save_2)
