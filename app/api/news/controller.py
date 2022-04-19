from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required
from logging import getLogger
from .dto import NewsDto
from .service import *

api = NewsDto.api

token_args = reqparse.RequestParser()
token_args.add_argument('Authorization', type=str, location='headers', help='Bearer Token', required=True)

id_args = reqparse.RequestParser()
id_args.add_argument("id", type=int, required=True)


@api.route("/")
class News(Resource):
    @api.doc(
        "Get all news",
        responses={200: ("News response", NewsDto.news_response), 404: "No news found!"},
    )
    @jwt_required()
    @api.expect(token_args)
    def get(self):
        """ Get all news posts """
        api.logger.info("test")
        return get_all(), 200

    @api.doc(
        "Post News",
        responses={200: ("Post news response", NewsDto.news_response), 500: "Server error"},
    )
    @jwt_required()
    @api.expect(token_args, NewsDto.post_news)
    def post(self):
        """ Post new news post """
        print("controller", api.payload)
        return post_news(api.payload)

    @api.doc(
        "Update news post",
        responses={200: ("Update news response", NewsDto.news_response), 404: "News not found!"},
    )
    @jwt_required()
    @api.expect(token_args, NewsDto.update_news)
    def put(self):
        """ Update a spesific news post """
        return update_news(api.payload)


@api.route("/by-id")
class NewsById(Resource):
    @api.doc(
        "Get news by id",
        responses={200: ("News response", NewsDto.news_response), 404: "User not found!"},
    )
    @jwt_required()
    @api.expect(token_args, id_args)
    def get(self):
        """ Get a specific news post by its id """
        args = id_args.parse_args()
        return get_by_id(args["id"])

    @api.doc(
        "Delete news post",
        responses={200: ("News response", NewsDto.news_response), 404: "News Post found!"},
    )
    @jwt_required()
    @api.expect(token_args, id_args)
    def delete(self):
        """ Delete news post by id """
        args = id_args.parse_args()
        return delete_news(args["id"])
