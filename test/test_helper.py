import os 
import unittest
from utils.helper import ( get_format_of_file, get_file_name,
                            select_all_xml_files, match_csv_files ) 


class TestHelper(unittest.TestCase):
    
    def test_get_format_of_file(self):
        expected = ['csv','xml']
        result = get_format_of_file('csv')
        self.assertIn(result, expected)
    
    def test_get_file_name(self):
        expected = ['file1.xml', 'file2.xml', 'file3.xml' ]
        result = get_file_name('file1.xml')
        self.assertIn(result, expected)
    
    def test_select_all_xml_files(self):
        expected = ['file1.xml', 'file2.xml', 'file3.xml' ]
        result = select_all_xml_files()
        self.assertListEqual(result, expected)
    
    def test_match_csv_files(self):
        expected = [None , 'Switch Files !!']
        result = match_csv_files('vehicles','customer')
        self.assertIn(result, expected)



if __name__ == '__main__':
    unittest.main()