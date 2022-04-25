import flask_sqlalchemy_session
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required
import config
import config
from .dto import SprintFocusAreaDto
from .service import *

from ... import utils

api = SprintFocusAreaDto.api
data_resp = SprintFocusAreaDto.sfa_response

token_args = reqparse.RequestParser()
token_args.add_argument('Authorization', type=str, location='headers', help='Bearer Token', required=True)

id_args = reqparse.RequestParser()
id_args.add_argument("id", type=int, required=True)

sprint_args = reqparse.RequestParser()
sprint_args.add_argument("sprint", type=str, required=True)


@api.route("/")
class SFA(Resource):
    @api.doc(
        "Dummy",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    @jwt_required()
    @api.expect(token_args)
    def get(self):
        """ GET all SFA's """
        return get_all()

    @jwt_required()
    @api.expect(token_args, SprintFocusAreaDto.post_sfa)
    def post(self):
        """ Create SFA """
        return post_sfa(api.payload)

    @jwt_required()
    @api.expect(token_args, SprintFocusAreaDto.update_sfa)
    def put(self):
        """ Update SFA """
        return update_sfa(api.payload)


@api.route("/by-id")
class SFAByID(Resource):
    @api.doc(
        "Dummy2",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    @jwt_required()
    @api.expect(token_args, id_args)
    def get(self):
        """ Get SFA by ID """
        args = id_args.parse_args()
        return get_by_id(args["id"])

    @jwt_required()
    @api.expect(token_args, id_args)
    def delete(self):
        """ Delete SFA by ID """
        args = id_args.parse_args()
        return delete_sfa(args["id"])


@api.route("/by-sprint")
class SFABySprintID(Resource):
    @api.doc(
        "Dummy3",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    @jwt_required()
    @api.expect(token_args, sprint_args)
    def get(self):
        """ Get SFA by sprint """
        args = sprint_args.parse_args()
        return get_by_sprint(args["sprint"])
