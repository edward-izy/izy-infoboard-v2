import logging
import os
import hvac
import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta

from cryptography.hazmat.primitives.asymmetric import rsa

basedir = os.path.abspath(os.path.dirname(__file__))


def load_keys():
    with open("jwtRS256.key.pub", "rb") as f:
        public = serialization.load_pem_public_key(
            f.read(), backend=default_backend()
        )
    with open("jwtRS256.key", "rb") as f:
        private = serialization.load_pem_private_key(
            f.read(), None, backend=default_backend()
        )
    return private, public


def get_token():
    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    url = f'http://192.168.2.12:4000/v1/auth/userpass/login/{user_name}'
    res = requests.post(url, json={"password": password})
    token = res.json()['auth']['client_token']
    return token


def get_client(token):
    client = hvac.Client(
        url='http://192.168.2.12:4000',
        token=token)
    return client


def renew_token(client):
    client.renew_self_token()


def get_kvs(client):
    mount_point = 'kv'
    secret_path = 'jwt/public'

    read_secret_result = client.secrets.kv.v1.read_secret(
        path=secret_path,
        mount_point=mount_point,
    )


token = get_token()
client = get_client(token)


class Config:
    JWT_ALGORITHM = "RS256"
    JWT_DECODE_ALGORITHMS = "RS256"

    private, public = load_keys()
    JWT_PRIVATE_KEY = private
    JWT_PUBLIC_KEY = public

    DEBUG = False
    # JWT Extended config
    ## Set the token to expire every week
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)


class DevelopmentConfig(Config):
    DEBUG = True

    # Get Parameters and Credentials from VAULT
    module_parameters = client.secrets.kv.v1.read_secret(
        path="module/parameters/testModule1",
        mount_point="kv")["data"]
    database_info = client.read(module_parameters["database_credentials_path"])
    db_credentials_expiry_time = datetime.now() + timedelta(seconds=database_info["lease_duration"])
    database_credentials = database_info["data"]

    # --------- Security Parameters ---------
    PUBLIC_KEY = client.secrets.kv.v1.read_secret(path="jwt/public", mount_point="kv")['data']['jwt_public_key']

    # --------- Swagger Parameters ---------
    SWAGGER_TITLE = module_parameters["swagger_title"]
    SWAGGER_DESCRIPTION = module_parameters["swagger_description"]
    SWAGGER_VERSION = module_parameters["swagger_version"]

    # --------- Database Parameters ---------
    DB_DIALECT = module_parameters["database_dialect"]
    DB_HOST = module_parameters["database_host"]
    DB_PORT = module_parameters["database_port"]
    DB_USERNAME = database_credentials["username"]
    DB_PASSWORD = database_credentials["password"]
    DB_NAME = module_parameters["database_name"]

    SQLALCHEMY_DATABASE_URI = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------- Logging ---------
    # Create Log Path / Files
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    if not os.path.exists('logs/app.log'):
        open('logs/app.log', 'x')
    if not os.path.exists('logs/news.log'):
        open('logs/news.log', 'x')
    if not os.path.exists('logs/sprint.log'):
        open('logs/sprint.log', 'x')
    if not os.path.exists('logs/sfa.log'):
        open('logs/sfa.log', 'x')

    # Format Handler
    formatter = logging.Formatter('%(levelname)-s - %(name)-5s %(asctime)-30s line_%(lineno)-d in %(filename)-20s %(message)s')
    format_handler = logging.StreamHandler()
    format_handler.setFormatter(formatter)

    # News File Handler
    news_fh = logging.FileHandler("logs/news.log")
    news_fh.setFormatter(formatter)
    # Sprint File Handler
    sprint_fh = logging.FileHandler("logs/sprint.log")
    # Sprint_Focus_Area File Handler
    sfa_fh = logging.FileHandler("logs/sfa.log")

    w_log = logging.getLogger('werkzeug')
    w_log.setLevel(logging.WARNING)
    w_log.addHandler(format_handler)

    logging.basicConfig(level=logging.WARNING, filename="logs/app.log", format="%(levelname)-s - %(name)-5s %(asctime)-30s line_%(lineno)-d in %(filename)-20s %(message)s")


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # In-memory SQLite for testing
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # Get Parameters and Credentials from VAULT
    module_parameters = client.secrets.kv.v1.read_secret(
        path=os.getenv('KV_PATH'),
        mount_point="kv")["data"]
    database_info = client.read(module_parameters["database_credentials_path"])
    db_credentials_expiry_time = datetime.now() + timedelta(seconds=database_info["lease_duration"])
    database_credentials = database_info["data"]

    # Security Parameters
    PUBLIC_KEY = client.secrets.kv.v1.read_secret(path="jwt/public", mount_point="kv")['data']['jwt_public_key']

    # Swagger Parameters
    SWAGGER_TITLE = module_parameters["swagger_title"]
    SWAGGER_DESCRIPTION = module_parameters["swagger_description"]
    SWAGGER_VERSION = module_parameters["swagger_version"]

    # Database Parameters
    DB_DIALECT = module_parameters["database_dialect"]
    DB_HOST = module_parameters["database_host"]
    DB_PORT = module_parameters["database_port"]
    DB_USERNAME = database_credentials["username"]
    DB_PASSWORD = database_credentials["password"]
    DB_NAME = module_parameters["database_name"]

    SQLALCHEMY_DATABASE_URI = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------- Create Log Path / Files ---------
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    if not os.path.exists('logs/app.log'):
        open('logs/app.log', 'x')
    if not os.path.exists('logs/news.log'):
        open('logs/news.log', 'x')
    if not os.path.exists('logs/sprint.log'):
        open('logs/sprint.log', 'x')
    if not os.path.exists('logs/sfa.log'):
        open('logs/sfa.log', 'x')

    # --------- Format Handler ---------
    formatter = logging.Formatter(
        '%(levelname)-s - %(name)-5s %(asctime)-30s line_%(lineno)-d in %(filename)-20s %(message)s')
    format_handler = logging.StreamHandler()
    format_handler.setFormatter(formatter)

    # --------- News File Handler ---------
    news_fh = logging.FileHandler("logs/news.log")
    news_fh.setFormatter(formatter)
    # --------- Sprint File Handler ---------
    sprint_fh = logging.FileHandler("logs/sprint.log")
    # --------- Sprint_Focus_Area File Handler ---------
    sfa_fh = logging.FileHandler("logs/sfa.log")

    w_log = logging.getLogger('werkzeug')
    w_log.setLevel(logging.WARNING)
    w_log.addHandler(format_handler)

    logging.basicConfig(level=logging.WARNING, filename="logs/app.log",
                        format="%(levelname)-s - %(name)-5s %(asctime)-30s line_%(lineno)-d in %(filename)-20s %(message)s")


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)
