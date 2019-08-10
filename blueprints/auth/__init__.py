from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
import json, hashlib
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.client.model import Clients

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        args = parser.parse_args()

        password = hashlib.md5(args['client_secret'].encode()).hexdigest()

        ###### from database #######
        qry = Clients.query

        qry = qry.filter_by(client_id = args['client_id'])
        qry = qry.filter_by(client_secret = password).first()
         

        claim = marshal(qry, Clients.response_field)

        if qry is not None:
            token = create_access_token(identity=args['client_id'], user_claims=claim)
        else:
            return {'status':'failed', 'result': 'UNAUTHORIZED | invalid key or secret'}, 401

        ######### for testing #####
        # if args['client_id'] == 'altarest' and args['client_secret'] == '10opwAPk3Q2D':
        #     token = create_access_token(identity=args['client_id'])
        # else:
        #     return {'status':'UNAUTHORIZED', 'message': 'invalid key or secret'}, 401

        return {"status":"success",'result': token}, 200, {'Content-Type':'application/json'}

    @jwt_required   # method need auth to run 
    def get(self):
        claims = get_jwt_claims()
        return {"status":"success", 'result': claims}, 200, {'Content-Type':'application/json'}

api.add_resource(CreateTokenResource,'')
