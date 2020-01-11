import unittest
from flask import abort, url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        # pass in test configurations
        config_name = "testing"
        return app

class TestStatsGeneration(TestCase):
    def test_connection(self):
        response = self.client.get(url_for("/get_package"))
        self.assertEqual(response.status_code, 200)

    def test_package_retrieval(self):
        response = self.client.get(url_for("/get_package"))
        package = response.json()

        self.assertTrue("number of members" in response.json(), msg = None)
        self.assertTrue(package["num_of_members"] > 0 and package["num_of_members"] <= 20, msg = None)

        self.assertTrue("popularity" in response.json(), msg = None)
        self.assertTrue(package["popularity"] > 0 and package["popularity"] <= 100, msg = None)

        self.assertTrue("pretentiousness" in response.json(), msg = None)
        self.assertTrue(package["pretentiousness"] > 0 and package["pretentiousness"] <= 100, msg = None)
    
    def test_health_check(self):
        response = self.client.get(url_for("/health-check"))
        self.assertTrue(response.content, "OK")
