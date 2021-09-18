import unittest
from utils.xml_parser_enriched import XMLParser_enrich


class TestXmlParserEnriched(unittest.TestCase):
    
    
    def test_XMLParser_enrich(self):
        
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
                            "model_year": "2008",
                            "Model": "Sierra",
                            "Manufacturer": "GENERAL MOTORS LLC",
                            "PlantCountry": "UNITED STATES (USA)",
                            "VehicleType": "INCOMPLETE VEHICLE"
                        },
                        {
                            "id": "V1001",
                            "make": "Chevrolet",
                            "vin_number": "1G1Z464865F214437",
                            "model_year": "2005",
                            "Model": "",
                            "Manufacturer": "GENERAL MOTORS LLC",
                            "PlantCountry": "UNITED STATES (USA)",
                            "VehicleType": "PASSENGER CAR"
                        }
                    ]
                }
            ]
        }
        
        result = XMLParser_enrich('file1.xml')
        self.assertDictEqual(result, expected)
        


if __name__ == '__main__':
    unittest.main()

