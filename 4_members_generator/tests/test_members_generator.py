import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Names

class TestBase(TestCase):
    def create_app(self):
        # pass in test configurations
        config_name = "testing"
        app.config.update(
            SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+str(getenv("MYSQL_USER"))+":"+str(getenv("MYSQL_PASSWORD"))+"@"+str(getenv("MYSQL_URL"))+"/"+str(getenv("MYSQL_TESTDB")))
        return app
    
    def setUp(self):
        """
        Will be called before every test
        """
        db.session.commit()
        db.drop_all()
        db.create_all()
        # create names
        male_member = Names(name = "male name", name_type = "male")
        female_member = Names(name = "female name", name_type = "female")
        surname = Names(name = "surname", name_type = "surname")
        # save to database
        db.session.add(male_member)
        db.session.add(female_member)
        db.session.add(surname)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestNameGeneration(TestBase):
    def test_connection(self):
        response = self.client.get(url_for("generate_band_info"))
        self.assertEqual(response.status_code, 200)

    def test_package_retrieval(self):
        response = self.client.get(url_for("generate_band_info"))
        self.assertTrue("name" in response.json(), msg = None)
        self.assertTrue("genre" in response.json(), msg = None)
    
    def test_database(self):
        male_member = Names.query.filter_by(name_type = "male").first()
        female_member = Names.query.filter_by(name_type = "female").first()
        surname = Names.query.filter_by(name_type = "surname").first()

        self.assertEqual(male_member.name, "male name")
        self.assertEqual(female_member.name, "female name")
        self.assertEqual(surname.name, "surname")
    
    def test_health_check(self):
        response = self.client.get(url_for("health-check"))
        self.assertEqual(response.status_code, 200)
