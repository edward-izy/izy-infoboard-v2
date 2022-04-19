import logging
import os

from flask_restx import Namespace, fields

from config import config_by_name


class SprintDto:

    api = Namespace("sprint", description="Sprint related operations.")
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].format_handler)
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].sprint_fh)
    api.logger.setLevel(logging.DEBUG)
    post_sprint = api.model(
        "Post sprint object",
        {
            "sprint": fields.String,
            "development_start": fields.Date,
            "development_end": fields.Date,
            "test_start": fields.Date,
            "test_end": fields.Date,
            "production_date": fields.Date,
            "state": fields.Integer,
        }
    )

    update_sprint = api.model(
        "Update sprint object",
        {
            "sprint": fields.String,
            "development_start": fields.Date,
            "development_end": fields.Date,
            "test_start": fields.Date,
            "test_end": fields.Date,
            "production_date": fields.Date,
            "state": fields.Integer,
        }
    )

    sprint_response = api.model(
        "Sprint Data Response",
        {
            "sprint": fields.String,
            "development_start": fields.Date,
            "development_end": fields.Date,
            "test_start": fields.Date,
            "test_end": fields.Date,
            "production_date": fields.Date,
            "state": fields.Integer,
        }
    )

