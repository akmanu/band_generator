import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Words

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
        # create words
        band_noun = Words(word = "band noun", word_type = "noun", band_or_genre = "band")
        band_adjective = Words(word = "band adjective", word_type = "adjective", band_or_genre = "band")
        genre_noun = Words(word = "genre noun", word_type = "noun", band_or_genre = "genre")
        genre_adjective = Words(word = "genre adjective", word_type = "adjective", band_or_genre = "genre")
        # save to database
        db.session.add(band_noun)
        db.session.add(band_adjective)
        db.session.add(genre_noun)
        db.session.add(genre_adjective)
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
        band_noun = Words.query.filter_by(word_type = "noun", band_or_genre = "band").first()
        band_adjective = Words.query.filter_by(word_type = "adjective", band_or_genre = "band").first()
        genre_noun = Words.query.filter_by(word_type = "noun", band_or_genre = "genre").first()
        genre_adjective = Words.query.filter_by(word_type = "adjective", band_or_genre = "genre").first()

        self.assertEqual(band_noun.word, "band noun")
        self.assertEqual(band_adjective.word, "band adjective")
        self.assertEqual(genre_noun.word, "genre noun")
        self.assertEqual(genre_adjective.word, "genre adjective")
    
    def test_health_check(self):
        response = self.client.get(url_for("health_check"))
        self.assertEqual(response.content, "band adjective band noun")
