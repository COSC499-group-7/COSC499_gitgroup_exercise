import integerdesc as method
import unittest

integer = [10,20,30,40,50,60]
test = method.sort_integer_desc(integer)
expected_output = [60,50,40,30,20,10]


class Testintegerdesc(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(test,expected_output)

if __name__ == '__main__':
    unittest.main()
