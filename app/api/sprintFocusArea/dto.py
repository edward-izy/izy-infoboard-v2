import logging
import os

from flask_restx import Namespace, fields

from config import config_by_name


class SprintFocusAreaDto:

    api = Namespace("sprintfocusarea", description="Sprint Focus Area related operations.")
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].format_handler)
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].sfa_fh)
    api.logger.setLevel(logging.DEBUG)
    post_sfa = api.model(
        "Post sfa object",
        {
            "sprint": fields.String,
            "title": fields.String,
            "description": fields.String
        }
    )

    update_sfa = api.model(
        "Update sfa object",
        {
            "id": fields.Integer,
            "sprint": fields.String,
            "title": fields.String,
            "description": fields.String
        }
    )

    sfa_response = api.model(
        "Sfa Data Response",
        {
            "id": fields.Integer,
            "sprint": fields.String,
            "title": fields.String,
            "description": fields.String
        }
    )