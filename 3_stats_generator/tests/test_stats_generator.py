import unittest
from flask import abort, url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        # pass in test configurations
        config_name = "testing"
        return app

class TestStatsGeneration(TestBase):
    def test_connection(self):
        response = self.client.get(url_for("generate_band_info"))
        self.assertEqual(response.status_code, 200)

    def test_package_retrieval(self):
        response = self.client.get(url_for("generate_band_info"))
        package = response.json

        self.assertTrue("number of members" in package)
        self.assertTrue(package["number of members"] > 0 and package["number of members"] <= 20)

        self.assertTrue("popularity" in package)
        self.assertTrue(package["popularity"] > 0 and package["popularity"] <= 100)

        self.assertTrue("pretentiousness" in package)
        self.assertTrue(package["pretentiousness"] > 0 and package["pretentiousness"] <= 100)
    
    def test_health_check(self):
        response = self.client.get(url_for("health_check"))
        self.assertTrue(response.data, "OK")
