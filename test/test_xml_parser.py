import json
import unittest
from utils.xml_parser import XMLParser


class TestXmlParser(unittest.TestCase):
    
    
    def test_XMLParser(self):
        
        expected = {
            "file_name": "file1.xml",
            "transaction": [
                {
                    "date": "2020-10-15",
                    "customer": {
                        "customer_id": "ID1011601",
                        "name": "Esmé Babin",
                        "phone": "818-537-1995",
                        "address": "3344 Joy Lane"
                    },
                    "vehicles": [
                        {
                            "id": "V1000",
                            "make": "GMC",
                            "vin_number": "1GDJC33648F200204",
                            "model_year": "2008"
                        },
                        {
                            "id": "V1001",
                            "make": "Chevrolet",
                            "vin_number": "1G1Z464865F214437",
                            "model_year": "2005"
                        }
                    ]
                }
            ]
        }
        
        result = XMLParser('file1.xml')
        self.assertDictEqual(result, expected)
        


if __name__ == '__main__':
    unittest.main()

