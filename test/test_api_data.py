from utils.api_data import get_api_data
import unittest

class TestXmlParser(unittest.TestCase):
    def test_transaction_to_json(self):
        expected = {
            "Model": "Sierra",
            "Manufacturer": "GENERAL MOTORS LLC",
            "PlantCountry": "UNITED STATES (USA)",
            "VehicleType": "INCOMPLETE VEHICLE"
        }

        result = get_api_data('1GDJC33648F200204','2008')

        self.assertDictEqual(result, expected)


if __name__ == '__main__':
    unittest.main()