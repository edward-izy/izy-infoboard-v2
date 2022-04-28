import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session
from dotenv import load_dotenv
import config
from datetime import datetime, timedelta
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
import click
from flask_migrate import Migrate
from app import create_app, db
from flask_sqlalchemy_session import current_session


app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.before_first_request
def init_db():
    print("Init DB .......................")
    flask_scoped_session(sessionmaker(bind=create_engine(
        f"{config.config_by_name['development'].DB_DIALECT}://{config.config_by_name['development'].DB_USERNAME}:{config.config_by_name['development'].DB_PASSWORD}@{config.config_by_name['development'].DB_HOST}:{config.config_by_name['development'].DB_PORT}/{config.config_by_name['development'].DB_NAME}", pool_size=5),
                                      autocommit=False, autoflush=False), app)


@app.before_request
def update_db():
    if config.config_by_name[os.getenv('FLASK_CONFIG')].db_credentials_expiry_time < datetime.now():
        while True:
            try:
                print('Getting new credentials....')
                info = config.client.read(config.config_by_name[os.getenv('FLASK_CONFIG')].module_parameters['database_credentials_path'])
                data = info['data']
                print('Updating variables...')
                config.config_by_name[os.getenv('FLASK_CONFIG')].db_credentials_expiry_time = datetime.now() + timedelta(seconds=info['lease_duration'])
                config.config_by_name[os.getenv('FLASK_CONFIG')].DB_USERNAME = data['username']
                config.config_by_name[os.getenv('FLASK_CONFIG')].DB_PASSWORD = data['password']
                print('Creating new connection!')
                current_session.close()
                flask_scoped_session(sessionmaker(bind=create_engine(f"{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_DIALECT}://{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_USERNAME}:{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_PASSWORD}@{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_HOST}:{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_PORT}/{config.config_by_name[os.getenv('FLASK_CONFIG')].DB_NAME}", pool_size=5), autocommit=False, autoflush=False), app)
            except:
                config.client = config.get_client(config.get_token())
                continue
            break

    else:
        print("Experation time:", config.config_by_name["development"].db_credentials_expiry_time)
        print("Credentials valid!")


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
@click.argument("test_names", nargs=-1)
def test(test_names):
    """ Run unit tests """
    import unittest

    if test_names:
        """ Run specific unit tests.

        Example:
        $ flask test tests.test_auth_api tests.test_user_model ...
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)

    else:
        tests = unittest.TestLoader().discover("tests", pattern="test*.py")

    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    # Return 1 if tests failed, won't reach here if succeeded.
    return 1
