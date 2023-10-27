#!/usr/bin/python3
"""Testing the state module"""

import unittest
import re
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.name = "Toilet"
        self.state.save()

    def test_str_not_none(self):
        self.assertIsNotNone(self.state.__str__())

    def test_str_correct_format(self):
        rgx = re.compile(r"\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.state), rgx)

    def test_id(self):
        self.assertIsNotNone(self.state.id)

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.state.created_at)

    def test_created_at_correct_timing(self):
        self.assertLess(self.state.created_at, datetime.now())

    def test_to_dict(self):
        self.assertIsInstance(self.state.to_dict(), dict)

    def test_save_updated_at(self):
        self.state.save()
        save_1 = self.state.updated_at
        self.state.save()
        save_2 = self.state.updated_at
        self.assertLess(save_1, save_2)
