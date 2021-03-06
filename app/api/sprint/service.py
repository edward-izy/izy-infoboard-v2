from app.models.sprint import Sprint
from app.utils import err_resp, message, internal_err_resp
from flask_sqlalchemy_session import  current_session


def get_all():
    """ Get user data by username """
    try:
        sprints = current_session.query(Sprint).all()

        res = []
        for sprint in sprints:
            new = {
                "spint": sprint.sprint,
                "development_start": sprint.development_start,
                "development_end": sprint.development_end,
                "test_start": sprint.test_start,
                "test_end": sprint.test_end,
                "production_date": sprint.production_date,
                "state": sprint.state
            }
            res.append(new)
        return res

    except Exception as e:
        return e


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
            "spint": sprint.sprint,
            "development_start": sprint.development_start,
            "development_end": sprint.development_end,
            "test_start": sprint.test_start,
            "test_end": sprint.test_end,
            "production_date": sprint.production_date,
            "state": sprint.state
        }
        return new

    except Exception as e:
        return e


def get_by_sprint(sprint):
    try:
        sprint = current_session.query(Sprint).filter_by(sprint=sprint).first()
        new = {
            "spint": sprint.sprint,
            "development_start": sprint.development_start,
            "development_end": sprint.development_end,
            "test_start": sprint.test_start,
            "test_end": sprint.test_end,
            "production_date": sprint.production_date,
            "state": sprint.state
        }
        return new

    except Exception as e:
        return e


def update_sprint(sprint):
    try:
        prev = current_session.query(Sprint).filter_by(sprint=sprint['sprint']).first()
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
            "spint": prev.sprint,
            "development_start": prev.development_start,
            "development_end": prev.development_end,
            "test_start": prev.test_start,
            "test_end": prev.test_end,
            "production_date": prev.production_date,
            "state": prev.state
        }
        return new

    except Exception as e:
        return e


def delete_sprint(sprint):
    try:
        sprint = current_session.query(Sprint).filter_by(sprint=sprint).first()
        current_session.delete(sprint)
        current_session.flush()
        current_session.commit()
        new = {
            "spint": sprint.sprint,
            "development_start": sprint.development_start,
            "development_end": sprint.development_end,
            "test_start": sprint.test_start,
            "test_end": sprint.test_end,
            "production_date": sprint.production_date,
            "state": sprint.state
        }
        return new

    except Exception as e:
        return e