import unittest
import my_calculator


class test_calc(unittest.TestCase):

    def test_add(self):
        result = my_calculator.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest()
