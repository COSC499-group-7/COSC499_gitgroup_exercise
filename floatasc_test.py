import unittest
from floatasc import sort_float_asc

class floatAscTest(unittest.TestCase):
    def test(self):
        floats = [8.2, 21.9, 19.5, 2.2, 50.6, 18.3, 33.2, 3.7]
        sortedFloats = sort_float_asc(floats)
        self.assertEqual((sortedFloats), ([2.2, 3.7, 8.2, 18.3, 19.5, 21.9, 33.2, 50.6]))

if __name__ == '__main__':
    unittest.main()