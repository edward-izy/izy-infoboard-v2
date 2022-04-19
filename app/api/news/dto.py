import logging
import os

from flask_restx import Namespace, fields
from config import config_by_name


class NewsDto:

    api = Namespace("news", description="News related operations.")
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].format_handler)
    api.logger.addHandler(config_by_name[os.getenv('FLASK_CONFIG')].news_fh)
    api.logger.setLevel(logging.DEBUG)


    post_news = api.model(
        "Post news object",
        {
            "title": fields.String,
            "description": fields.String,
            "image_path": fields.String,
            "active": fields.Boolean,
        }
    )

    update_news = api.model(
        "Update news object",
        {
            "id": fields.Integer,
            "title": fields.String,
            "description": fields.String,
            "image_path": fields.String,
            "active": fields.Boolean,
        }
    )

    news_response = api.model(
        "News Data Response",
        {
            "id": fields.String,
            "title": fields.String,
            "description": fields.String,
            "image_path": fields.String,
            "active": fields.Boolean
        }
    )

    news_delete_response = api.model(
        "News Data Response",
        {
            "id": fields.Integer,
            "title": fields.String,
            "description": fields.String,
            "image_path": fields.String,
            "active": fields.Boolean
        },
    )

