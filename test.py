import unittest
import requests

URL = 'http://localhost:5000'


class TestStringMethods(unittest.TestCase):
    def test_invalid_path_api(self):
        path_api = '/api/ephemeris'
        query = '?day=2020-08-06'
        response = requests.get(URL + path_api + query)

        self.assertEqual(404, response.status_code)

    def test_invalid_date(self):
        path_api = '/api/efemerides'
        query = '?day=20200806'
        response = requests.get(URL + path_api + query)

        self.assertEqual(400, response.status_code)


    def test_valid_date(self):
        path_api = '/api/efemerides'
        query = '?day=2020-08-06'
        response = requests.get(URL + path_api + query)

        self.assertEqual(200, response.status_code)