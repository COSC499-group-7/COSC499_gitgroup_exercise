import unittest
import integerasc

numbers = [1,10,7,6,8,9]
test = integerasc.sort_integer_asc(numbers)
expected_output = [1,6,7,8,9,10]

class integerAscTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test, expected_output)
if __name__ == '__main__':
    unittest.main()