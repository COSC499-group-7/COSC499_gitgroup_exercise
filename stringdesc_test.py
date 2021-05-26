import unittest
import stringdesc

class stringDescTest(unittest.TestCase):

   def test(self):
    strings = ['Apple', 'Google', 'Amazon', 'EA', 'Blizzard']
    expected_output = ['Google', 'EA', 'Blizzard', 'Apple', 'Amazon']
    self.assertEqual(stringdesc.sort_string_desc(strings), expected_output)
 
if __name__ == '__main__':
    unittest.main()