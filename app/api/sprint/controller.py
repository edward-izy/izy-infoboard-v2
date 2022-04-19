from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required
from .service import *
from .dto import SprintDto

api = SprintDto.api
data_resp = SprintDto.sprint_response

token_args = reqparse.RequestParser()
token_args.add_argument('Authorization', type=str, location='headers', help='Bearer Token', required=True)

sprint_args = reqparse.RequestParser()
sprint_args.add_argument("sprint", type=str, required=True)


@api.route("/")
class SprintGet(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    @jwt_required()
    @api.expect(token_args)
    def get(self):
        """ Get a specific user's data by their username """
        return get_all()

    @jwt_required()
    @api.expect(token_args, SprintDto.post_sprint)
    def post(self):
        """ Get a specific user's data by their username """
        return post_sprint(api.payload)

    @jwt_required()
    @api.expect(token_args, SprintDto.update_sprint)
    def put(self):
        """ Get a specific user's data by their username """
        return update_sprint(api.payload)


@api.route("/by-sprint")
class SprintGetById(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    @jwt_required()
    @api.expect(token_args, sprint_args)
    def get(self):
        """ Get a specific user's data by their username """
        args = sprint_args.parse_args()
        return get_by_sprint(args["sprint"])

    @jwt_required()
    @api.expect(token_args, sprint_args)
    def delete(self):
        """ Get a specific user's data by their username """
        args = sprint_args.parse_args()
        return delete_sprint(args["sprint"])

