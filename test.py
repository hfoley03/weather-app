import unittest
from main import get_geocode
from main import get_data

class TestGeocode(unittest.TestCase):
    def test_galway_geocode(self):
        
        correct_result = "53.14399, -9.46949"
        result = get_geocode("Galway, Ireland")
        self.assertEqual(result, correct_result)

    def test_new_york_geocode(self):
    
        correct_result = "40.71273, -74.00602"
        result = get_geocode("New York")
        self.assertEqual(result, correct_result)

    def test_invalid_input_geocode(self):
        
        correct_result = None
        result = get_geocode("asdfghjkjhgfdsa")
        self.assertEqual(result, correct_result)

    def test_dict_keys_get_data_function(self):
        correct_result = {'startTime': '', 'values': {'temperature': 0, 'cloudCover': 0, 'windSpeed': 0, 'precipitationIntensity': 0}}
        result = get_data("53.14399, -9.46949")
        assert (result[0].keys() == correct_result.keys())
    
    def test_invalid_input_get_data_function(self):
        correct_result = None
        result = get_data("12345, 1334444")
        self.assertEqual(result, correct_result)

    def test_invalid_input_string_get_data_function(self):
        correct_result = None
        result = get_data("This is a string")
        self.assertEqual(result, correct_result)

    def test_invalid_arg_amount_get_data_function(self):
        correct_result = None
        result = get_data("12345")
        self.assertEqual(result, correct_result)



if __name__ == '__main__':
    unittest.main() 