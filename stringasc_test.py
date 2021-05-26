import unittest
import stringasc

class StringAscTest(unittest.TestCase):

   def test(self):
    strings = ['Apple', 'Zenith', 'Dungeon', 'Giraffe', 'Billiards']
    expected_output = ['Apple', 'Billiards', 'Dungeon', 'Giraffe', 'Zenith']
    self.assertListEqual(stringasc.sort_string_asc(strings),expected_output)
 
if __name__ == "__main__":
    unittest.main()