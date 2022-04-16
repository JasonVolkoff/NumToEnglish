from django.test import TestCase, Client
from api.constants import ERROR_RESPONSE
import json
# Create your tests here.


class NumToEnglishViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/num_to_english/'

    def testCanMakePostRequest(self):
        input = {"number": "12"}
        jsonInput = json.dumps(input)
        response = self.client.post(
            self.url, jsonInput, content_type="application/json")
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["num_in_english"], "twelve")

    def testCanMakeGetRequest(self):
        response = self.client.get(self.url+"?number=12")
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["num_in_english"], "twelve")

    def testNonNumericalInput(self):
        response = self.client.get(self.url+"?number=abc")
        data = response.json()
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["num_in_english"], ERROR_RESPONSE.INVALID_INPUT)

    def testEmptyInput(self):
        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["num_in_english"], ERROR_RESPONSE.INVALID_INPUT)

    def testNegativeValueInput(self):
        response = self.client.get(self.url+"?number=-12")
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["num_in_english"], "Negative twelve")

    def testZeroValueInput(self):
        response = self.client.get(self.url+"?number=0")
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["num_in_english"], "Zero")

    def testInputValueMaximumMinimum(self):
        sextillion = 10**21
        sextillion_str = str(sextillion)
        response = self.client.get(f"{self.url}?number={sextillion_str}")
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["num_in_english"], "one sextillion")

        # Adding 1 should cause it to go out of allowable range
        sextillion_str = str(sextillion+1)
        response = self.client.get(f"{self.url}?number={sextillion_str}")
        data = response.json()
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["num_in_english"],
                         ERROR_RESPONSE.NUM_OUT_OF_RANGE)

        # Similarly for it's negative value
        sextillion_str = str(-1*sextillion-1)
        response = self.client.get(f"{self.url}?number={sextillion_str}")
        data = response.json()
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["num_in_english"],
                         ERROR_RESPONSE.NUM_OUT_OF_RANGE)


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/'

    def testCanGetTemplate(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
