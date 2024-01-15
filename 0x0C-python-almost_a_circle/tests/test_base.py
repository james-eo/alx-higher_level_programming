#!/usr/bin/python3

import unittest
from  models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj = Base()
        json_string = Base.to_json_string([obj.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_save_to_file(self):
        obj = Base()
        Base.save_to_file([obj])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        instances = Base.from_json_string(json_string)
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Base)
        self.assertEqual(instances[0].id, 1)

    def test_create(self):
        dictionary = {"id": 1}
        obj = Base.create(**dictionary)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        with open("Base.json", "w") as file:
            file.write('[{"id": 1}]')

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Base)
        self.assertEqual(instances[0].id, 1)

    def test_save_to_file_csv(self):
        obj = Base()
        Base.save_to_file_csv([obj])
        with open("Base.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, '1\n')

    def test_load_from_file_csv(self):
        with open("Base.csv", "w") as file:
            file.write('1\n')

        instances = Base.load_from_file_csv()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Base)
        self.assertEqual(instances[0].id, 1)

if __name__ == '__main__':
    unittest.main()

