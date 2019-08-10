import datetime
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs

from blueprints import internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

from .model import Penyaluran
from blueprints import db, app
from sqlalchemy import desc
# 'client' penamaan (boleh diganti)

bp_penyaluran = Blueprint('penyaluran', __name__)
api = Api(bp_penyaluran)


class PenyaluranResource(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='args', help='invalid id', required=True)
        args = parser.parse_args()

        qry = Penyaluran.query.get(args["id"])

        if qry is not None:
            return {"status":"success", "result":marshal(qry, Penyaluran.response_field)}, 200, {'Content-Type':'application/json'}

        return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}


    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('yatim_duafa',location='json', help='invalid yatim_duafa', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('peyaluran',location='json', help='invalid peyaluran', required=True)
        parser.add_argument('cara_bayar',location='json', help='invalid cara_bayar', required=True)
        parser.add_argument('rekening',location='json', help='invalid rekening', required=True)
        parser.add_argument('penerima',location='json', help='invalid penerima')
        parser.add_argument('bukti',location='json', help='invalid bukti')
        parser.add_argument('keterangan',location='json', help='invalid keterangan')
        args = parser.parse_args()
        
        claims = get_jwt_claims()

        qry = Penyaluran(datetime.datetime.now(), args['yatim_duafa'], args['alamat'], args['peyaluran'],args['cara_bayar'],args['rekening'],args['penerima'],args['bukti'],args['keterangan'],claims['id'])

        db.session.add(qry)
        db.session.commit()

        app.logger.debug('DEBUG : %s ', qry)

        return {"status":"success", "result":marshal(qry, Penyaluran.response_field)}, 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('yatim_duafa',location='json', help='invalid yatim_duafa', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('peyaluran',location='json', help='invalid peyaluran', required=True)
        parser.add_argument('cara_bayar',location='json', help='invalid cara_bayar', required=True)
        parser.add_argument('rekening',location='json', help='invalid rekening', required=True)
        parser.add_argument('penerima',location='json', help='invalid penerima')
        parser.add_argument('bukti',location='json', help='invalid bukti')
        parser.add_argument('keterangan',location='json', help='invalid keterangan')
        parser.add_argument('id',location='args', help='invalid id', required=True)
        args = parser.parse_args()

        qry = Penyaluran.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        qry.yatim_duafa = args['yatim_duafa']
        qry.alamat = args['alamat']
        qry.peyaluran = args['peyaluran']
        qry.cara_bayar = args['cara_bayar']
        qry.rekening = args['rekening']
        qry.penerima = args['penerima']
        qry.bukti = args['bukti']
        qry.keterangan = args['keterangan']
        db.session.commit()

        return {"status":"success", "result":marshal(qry, Penyaluran.response_field)}, 200, {'Content-Type':'application/json'}

    
    @jwt_required
    @internal_required
    def delete(self):
        return {"status":"failed", "result":"Delete Not Available Now, Please Contact Developer"}, 403, {'Content-Type':'application/json'}
        
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='json', help='invalid id', required=True)
        args = parser.parse_args()

        qry = Penyaluran.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        db.session.delete(qry)
        db.session.commit()

        return {"status":"success", "result":marshal(qry, Penyaluran.response_field)}, 200, {'Content-Type':'application/json'}

class PenyaluranResourceList(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp',type=int, location='args', default=25)
        parser.add_argument('id',type=int,location='args', help='invalid id')
        parser.add_argument('cara_bayar',location='args', help='invalid cara_bayar')
        args =parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Penyaluran.query

        if args['id'] is not None:
            qry = qry.filter_by(id=args['id'])

        if args['cara_bayar'] is not None:
            qry = qry.filter_by(cara_bayar=args['cara_bayar'])

        result = []
        for row in qry.limit(args['rp']).offset(offset).all():
            result.append(marshal(row, Penyaluran.response_field))
        
        results = {}
        results['page'] = args['p']
        results['total_page'] = len(result) // args['rp'] +1
        results['per_page'] = args['rp']
        results['data'] = result
        
        return {"status":"success", "result":results}, 200, {'Content-Type':'application/json'}

api.add_resource(PenyaluranResource, '','')
api.add_resource(PenyaluranResourceList, '/list')

