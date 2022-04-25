from flask import current_app
from flask_sqlalchemy_session import  current_session
from app import db
from sqlalchemy.exc import NoResultFound
from app.models.sprintfocusarea import SprintFocusArea
from app.utils import err_resp, message, internal_err_resp
from app.models.user import User
import logging

logger = logging.getLogger('api')

def get_all():
    try:
        sfas = current_session.query(SprintFocusArea).all()
        res = []
        for sfa in sfas:
            new = {
                "id": sfa.id,
                "sprint": sfa.sprint,
                "title": sfa.title,
                "description": sfa.description
            }
            res.append(new)
        return res


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def post_sfa(sfa):
    try:
        sfa = SprintFocusArea(
            sprint=sfa["sprint"],
            title=sfa["title"],
            description=sfa["description"],
        )
        current_session.add(sfa)
        current_session.flush()
        current_session.commit()

        new = {
            "id": sfa.id,
            "sprint": sfa.sprint,
            "title": sfa.title,
            "description": sfa.description
        }
        return new


    except NoResultFound as e:
        logger.exception(e)
        return {'error': 'news not found'}, 400

    except Exception as e:
        logger.exception(e)
        return {'error': 'unknown'}, 400


def get_by_id(id):
    try:
        sfa = current_session.query(SprintFocusArea).filter_by(id=id).one()

        res = {
            "id": sfa.id,
            "sprint": sfa.sprint,
            "title": sfa.title,
            "description": sfa.description
        }

        return res



    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def get_by_sprint(sprint):
    try:
        sfas = current_session.query(SprintFocusArea).filter_by(sprint=sprint).all()
        res = []
        for sfa in sfas:
            res_sfa = {
                "id": sfa.id,
                "sprint": sfa.sprint,
                "title": sfa.title,
                "description": sfa.description
            }
            res.append(res_sfa)
        return res


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def update_sfa(sfa):
    try:
        prev = current_session.query(SprintFocusArea).filter_by(id=sfa['id']).one()
        prev.id = sfa["id"]
        prev.sprint = sfa["sprint"]
        prev.title = sfa["title"]
        prev.description = sfa["description"]

        current_session.flush()
        current_session.commit()
        res = {
            "id": prev.id,
            "sprint": prev.sprint,
            "title": prev.title,
            "description": prev.description
        }
        return res


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400


def delete_sfa(id):
    try:
        sfa = current_session.query(SprintFocusArea).filter_by(id=id).one()
        current_session.delete(sfa)
        current_session.flush()
        current_session.commit()
        res = {
            "id": sfa.id,
            "sprint": sfa.sprint,
            "title": sfa.title,
            "description": sfa.description
        }
        return res


    except NoResultFound as e:

        logger.exception(e)

        return {'error': 'news not found'}, 400


    except Exception as e:

        logger.exception(e)

        return {'error': 'unknown'}, 400