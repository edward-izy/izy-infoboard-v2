from app.models.sprint import Sprint
from app.utils import err_resp, message, internal_err_resp
from flask_sqlalchemy_session import  current_session
from .dto import SprintDto
from sqlalchemy.exc import NoResultFound

logger = SprintDto.api.logger

def get_all():
    """ Get all sprints """
    try:
        sprints = current_session.query(Sprint).all()

        res = []
        for sprint in sprints:
            new = {
                "sprint": sprint.sprint,
                "development_start": str(sprint.development_start),
                "development_end": str(sprint.development_end),
                "test_start": str(sprint.test_start),
                "test_end": str(sprint.test_end),
                "production_date": str(sprint.production_date),
                "state": sprint.state
            }
            res.append(new)
        return res


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def post_sprint(sprint):
    try:
        sprint = Sprint(
            sprint=sprint["sprint"],
            development_start=sprint["development_start"],
            development_end=sprint["development_end"],
            test_start=sprint["test_start"],
            test_end=sprint["test_end"],
            production_date=sprint["production_date"],
            state=sprint["state"]
        )
        current_session.add(sprint)
        current_session.flush()
        current_session.commit()

        new = {
            "sprint": sprint.sprint,
            "development_start": str(sprint.development_start),
            "development_end": str(sprint.development_end),
            "test_start": str(sprint.test_start),
            "test_end": str(sprint.test_end),
            "production_date": str(sprint.production_date),
            "state": sprint.state
        }
        return new


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def get_by_sprint(sprint):
    try:
        sprint = current_session.query(Sprint).filter_by(sprint=sprint).first()
        new = {
            "sprint": sprint.sprint,
            "development_start": str(sprint.development_start),
            "development_end": str(sprint.development_end),
            "test_start": str(sprint.test_start),
            "test_end": str(sprint.test_end),
            "production_date": str(sprint.production_date),
            "state": sprint.state
        }
        return new


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def update_sprint(sprint):
    try:
        prev = current_session.query(Sprint).filter_by(sprint=sprint['sprint']).first()
        logger.info(prev)
        prev.sprint = sprint["sprint"]
        prev.development_start = sprint["development_start"]
        prev.development_end = sprint["development_end"]
        prev.test_start = sprint["test_start"]
        prev.test_end = sprint["test_end"]
        prev.production_date = sprint["production_date"]
        prev.state = sprint["state"]

        current_session.flush()
        current_session.commit()

        new = {
            "sprint": prev.sprint,
            "development_start": str(prev.development_start),
            "development_end": str(prev.development_end),
            "test_start": str(prev.test_start),
            "test_end": str(prev.test_end),
            "production_date": str(prev.production_date),
            "state": prev.state
        }
        logger.info(new)
        return new


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def delete_sprint(sprint):
    try:
        sprint = current_session.query(Sprint).filter_by(sprint=sprint).first()
        current_session.delete(sprint)
        current_session.flush()
        current_session.commit()
        new = {
            "sprint": sprint.sprint,
            "development_start": str(sprint.development_start),
            "development_end": str(sprint.development_end),
            "test_start": str(sprint.test_start),
            "test_end": str(sprint.test_end),
            "production_date": str(sprint.production_date),
            "state": sprint.state
        }
        return new


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400