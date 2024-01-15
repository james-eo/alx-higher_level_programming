import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4, 5)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect2.width, 3)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.x, 5)
        self.assertEqual(rect2.y, 0)

    def test_validate_attributes(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        rect = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with self.assertLogs() as log:
            rect.display()
            self.assertEqual(log.output, [expected_output])

    def test_str(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(rect), "[Rectangle] (6) 4/5 - 2/3")

    def test_update(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_to_dictionary(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        expected_dict = {'id': 6, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
