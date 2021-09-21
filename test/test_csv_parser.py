import unittest
from utils.csv_parser import CSVParser
import unittest.mock as mock



class TestCsvParser(unittest.TestCase):
    csv_parser = CSVParser()
    maxDiff = None
    def test_CSVParser(self):
        
        expected = {
            "_id" : mock.ANY,
            "file_name": mock.ANY,
            "transaction": [
                {
                    "date": "31/01/2020",
                    "customer": {
                        "id": "ID5410",
                        "name": "Melissa T Miller",
                        "address": "2837  Fidler Drive",
                        "phone": "210-624-7306"
                    },
                    "vehicles": [
                        {
                            "id": "V1475",
                            "make": "Ford",
                            "vin_number": "1FTSW3XG5FKB11488",
                            "model_year": 2015,
                            "Model": "Transit",
                            "Manufacturer": "FORD MOTOR COMPANY, USA",
                            "PlantCountry": "UNITED STATES (USA)",
                            "VehicleType": "TRUCK "
                        }
                    ]
                },
                {
                    "date": "25/04/2020",
                    "customer": {
                        "id": "ID9857",
                        "name": "Daniel I Walker",
                        "address": "3853  Hilltop Street",
                        "phone": "413-655-7397"
                    },
                    "vehicles": [
                        {
                            "id": "V3015",
                            "make": "Chevrolet",
                            "vin_number": "1G1ZD5EB6AF0053EX",
                            "model_year": 2010,
                            "Model": "Malibu",
                            "Manufacturer": "GENERAL MOTORS LLC",
                            "PlantCountry": "UNITED STATES (USA)",
                            "VehicleType": "PASSENGER CAR"
                        },
                        {
                            "id": "V2014",
                            "make": "Honda",
                            "vin_number": "JH2SC3327WM200123",
                            "model_year": 1998,
                            "Model": "CBR900",
                            "Manufacturer": "HONDA MOTOR CO., LTD",
                            "PlantCountry": "JAPAN",
                            "VehicleType": "MOTORCYCLE"
                        }
                    ]
                },
                {
                    "date": "16/03/2020",
                    "customer": {
                        "id": "ID6651",
                        "name": "Pauline J Buxton",
                        "address": "1927  Pinnickinick Street",
                        "phone": "360-727-9275"
                    },
                    "vehicles": [
                        {
                            "id": "V786",
                            "make": "Nissan",
                            "vin_number": "JN6JD02S0E0011849",
                            "model_year": 2014,
                            "Model": "Pickup",
                            "Manufacturer": "NISSAN MOTOR COMPANY, LTD",
                            "PlantCountry": "",
                            "VehicleType": "TRUCK "
                        }
                    ]
                }
            ]
        }
        
        path = 'input_data/csv'
        result = self.csv_parser.get_data_from_csv(f'{path}/customers.csv', f'{path}/vehicles.csv')
        self.assertDictEqual(result, expected)
        
        


if __name__ == '__main__':
    unittest.main()

