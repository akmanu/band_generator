import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, routes

class TestBase(TestCase):
    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        return app

class TestServer(TestBase):
    def test_connection(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
