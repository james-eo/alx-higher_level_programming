import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class.
    """

    def test_init(self):
        """
        Test the initialization of the Square class.
        """
        square1 = Square(2)
        square2 = Square(3, 4, 5)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square1.size, 2)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        self.assertEqual(square2.id, 2)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 4)
        self.assertEqual(square2.y, 5)

    def test_validate_attributes(self):
        """
        Test attribute validation in the Square class.
        """
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(TypeError):
            Square("2")

    def test_area(self):
        """
        Test the area method of the Square class.
        """
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_display(self):
        """
        Test the display method of the Square class.
        """
        square = Square(2)
        expected_output = "##\n##\n"
        with self.assertLogs() as log:
            square.display()
            self.assertEqual(log.output, [expected_output])

    def test_str(self):
        """
        Test the str method of the Square class.
        """
        square = Square(2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (5) 3/4 - 2")

    def test_update(self):
        """
        Test the update method of the Square class.
        """
        square = Square(1, 2, 3, 4)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """
        square = Square(2, 3, 4, 5)
        expected_dict = {'id': 5, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

