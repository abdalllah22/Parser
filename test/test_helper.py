import os 
import unittest
from utils.helper import Helpers
class TestHelper(unittest.TestCase):
    helpers = Helpers()
    
    def test_get_format_of_file(self):
        expected = ['csv','xml']
        result = self.helpers.get_format_of_file('csv')
        self.assertIn(result, expected)
    
    def test_get_file_name(self):
        expected = ['file1.xml', 'file2.xml', 'file3.xml' ]
        result = self.helpers.get_file_name('file1.xml')
        self.assertIn(result, expected)
    
    def test_select_all_xml_files(self):
        expected = ['file1.xml', 'file2.xml', 'file3.xml' ]
        result = self.helpers.select_all_xml_files()
        self.assertListEqual(result, expected)
    
    def test_match_csv_files(self):
        expected = [None , 'Switch Files !!']
        result = self.helpers.match_csv_files('vehicles','customer')
        self.assertIn(result, expected)



if __name__ == '__main__':
    unittest.main()