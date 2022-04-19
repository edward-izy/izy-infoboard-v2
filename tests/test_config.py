import unittest
import os

from flask import current_app
from app import create_app
from config import basedir


class TestDevelopmentConfig(unittest.TestCase):
    def test_app_is_development(self):
        """ Check if application is running in development mode """
        app = create_app("development")

        self.assertTrue(app.config["DEBUG"])
        self.assertFalse(current_app is None)

        # Test App Parameters
        self.assertFalse(app.config["SWAGGER_TITLE"] is None)
        self.assertFalse(app.config["SWAGGER_DESCRIPTION"] is None)
        self.assertFalse(app.config["SWAGGER_VERSION"] is None)

        # Test DB Parameters
        self.assertFalse(app.config["DB_DIALECT"] is None)
        self.assertFalse(app.config["DB_HOST"] is None)
        self.assertFalse(app.config["DB_PORT"] is None)
        self.assertFalse(app.config["DB_USERNAME"] is None)
        self.assertFalse(app.config["DB_PASSWORD"] is None)
        self.assertFalse(app.config["DB_NAME"] is None)
        self.assertTrue(app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] == False)

        # Test Token Settings
        self.assertFalse(app.config["PUBLIC_KEY"] is None)


class TestProductionConfig(unittest.TestCase):
    def test_app_is_production(self):
        """ Check if application is running in production mode """
        app = create_app("production")

        self.assertTrue(app.config["DEBUG"] is False)
        self.assertFalse(current_app is None)

        # Test App Parameters
        self.assertFalse(app.config["SWAGGER_TITLE"] is None)
        self.assertFalse(app.config["SWAGGER_DESCRIPTION"] is None)
        self.assertFalse(app.config["SWAGGER_VERSION"] is None)

        # Test DB Parameters
        self.assertFalse(app.config["DB_DIALECT"] is None)
        self.assertFalse(app.config["DB_HOST"] is None)
        self.assertFalse(app.config["DB_PORT"] is None)
        self.assertFalse(app.config["DB_USERNAME"] is None)
        self.assertFalse(app.config["DB_PASSWORD"] is None)
        self.assertFalse(app.config["DB_NAME"] is None)
        self.assertTrue(app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] is False)

        # Test Token Settings
        self.assertFalse(app.config["PUBLIC_KEY"] is None)
