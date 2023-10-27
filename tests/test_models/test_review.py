#!/usr/bin/python3
"""Testing the review module"""

import unittest
import re
from datetime import datetime
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.name = "Toilet"
        self.review.save()
    def test_str_not_none(self):
        self.assertIsNotNone(self.review.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.review), rgx)

    def test_id(self):
        self.assertIsNotNone(self.review.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.review.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.review.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.review.to_dict(), dict)

    def test_save_updated_at(self):
        self.review.save()
        save_1 = self.review.updated_at 
        self.review.save()
        save_2 = self.review.updated_at
        self.assertLess(save_1, save_2)
