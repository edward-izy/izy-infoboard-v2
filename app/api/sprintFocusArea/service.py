from flask import current_app
from flask_sqlalchemy_session import  current_session
from app import db
from app.models.sprintfocusarea import SprintFocusArea
from app.utils import err_resp, message, internal_err_resp
from app.models.user import User


def get_all():
    """ Get user data by username """
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

    except Exception as e:
        return e


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

    except Exception as e:
        return e


def get_by_id(id):
    try:
        sfa = current_session.query(SprintFocusArea).filter_by(id=id).first()

        res = {
            "id": sfa.id,
            "sprint": sfa.sprint,
            "title": sfa.title,
            "description": sfa.description
        }

        return res

    except Exception as e:
        return e


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

    except Exception as e:
        return e


def update_sfa(sfa):
    try:
        prev = current_session.query(SprintFocusArea).filter_by(id=sfa['id']).first()
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

    except Exception as e:
        return e


def delete_sfa(id):
    try:
        sfa = current_session.query(SprintFocusArea).filter_by(id=id).first()
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

    except Exception as e:
        return e