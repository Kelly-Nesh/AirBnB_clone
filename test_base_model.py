#!/usr/bin/python3
"""Contains tests for the basemodel class"""
import unittest
import re
from datetime import datetime
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_str(self):
        self.assertIsNotNone(self.my_model.__str__())
        rgx = re.compile("\[\w+\] \(\S+\) \{.+\}")
        self.assertRegex(str(self.my_model), rgx)

    def test_id(self):
        self.assertIsNotNone(self.my_model.id)

    def test_created_at(self):
        self.assertIsNotNone(self.my_model.created_at)
        self.assertLess(self.my_model.created_at, datetime.now())

    def test_to_dict(self):
        pass
