from app.models.news import News
from flask_sqlalchemy_session import current_session


def get_all():
    """ Get all news """
    try:
        news = current_session.query(News).all()

        res = []
        for news in news:
            res_obj = {
                'id': news.id,
                'title': news.title,
                'description': news.description,
                'image_path': news.image_path,
                'active': news.active
            }
            res.append(res_obj)
        return res

    except Exception as e:
        return e


def post_news(news):
    """ Post news """
    try:
        news = News(
            title=news["title"],
            description=news["description"],
            image_path=news["image_path"],
            active=news["active"]
        )
        current_session.add(news)
        current_session.flush()
        current_session.commit()
        res = {
            'id': news.id,
            'title': news.title,
            'description': news.description,
            'image_path': news.image_path,
            'active': news.active
        }

        return res

    except Exception as e:
        return {"message": "error"}, 410


def get_by_id(id):
    """ Get news by id """
    try:
        news = current_session.query(News).filter_by(id=id).first()
        res = {
            'id': news.id,
            'title': news.title,
            'description': news.description,
            'image_path': news.image_path,
            'active': news.active
        }
        return res

    except Exception as e:
        return {"News not found"}, 401


def update_news(news):
    """ update news by id """
    try:
        prev = current_session.query(News).filter_by(id=news['id']).first()
        prev.id = news["id"]
        prev.title = news["title"]
        prev.description = news["description"]
        prev.image_path = news["image_path"]
        prev.active = news["active"]

        current_session.flush()
        current_session.commit()
        res = {
            'id': prev.id,
            'title': prev.title,
            'description': prev.description,
            'image_path': prev.image_path,
            'active': prev.active
        }
        return res

    except Exception as e:
        return e


def delete_news(id):
    """ delete news by id """
    try:
        news = current_session.query(News).filter_by(id=id).first()
        current_session.delete(news)
        current_session.flush()
        current_session.commit()
        res = {
            'id': news.id,
            'title': news.title,
            'description': news.description,
            'image_path': news.image_path,
            'active': news.active
        }
        return res

    except Exception as e:
        return e


