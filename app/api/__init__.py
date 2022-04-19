import os

from flask_restx import Api
from flask import Blueprint
import config
from .news.controller import api as news_ns
from .sprintFocusArea.controller import api as sfa_ns
from .sprint.controller import api as sprint_ns
from app import config_by_name

flask_config = os.getenv("FLASK_CONFIG")
config = config.config_by_name[flask_config]

api_bp = Blueprint("api", __name__)
api = Api(api_bp, title=config.SWAGGER_TITLE, description=config.SWAGGER_DESCRIPTION, version=config.SWAGGER_VERSION)

# API namespaces
api.add_namespace(news_ns)
api.add_namespace(sfa_ns)
api.add_namespace(sprint_ns)
