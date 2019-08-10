import datetime
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs

from blueprints import internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

from .model import PenerimaanDonasi
from blueprints import db, app
from sqlalchemy import desc
# 'client' penamaan (boleh diganti)

bp_penerimaanDonasi = Blueprint('penerimaanDonasi', __name__)
api = Api(bp_penerimaanDonasi)


class PenerimaanDonasiResource(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='args', help='invalid id', required=True)
        args = parser.parse_args()

        qry = PenerimaanDonasi.query.get(args["id"])

        if qry is not None:
            return {"status":"success", "result":marshal(qry, PenerimaanDonasi.response_field)}, 200, {'Content-Type':'application/json'}

        return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}


    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('donatur',location='json', help='invalid donatur', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('no_telepon',location='json', help='invalid no_telepon', required=True)
        parser.add_argument('donasi',location='json', help='invalid donasi', required=True)
        parser.add_argument('cara_bayar',location='json', help='invalid cara_bayar', required=True)
        parser.add_argument('rekening',location='json', help='invalid rekening')
        parser.add_argument('bukti_transfer',location='json', help='invalid bukti_transfer')
        parser.add_argument('penerima',location='json', help='invalid penerima')
        parser.add_argument('bukti_terima',location='json', help='invalid bukti_terima')
        args = parser.parse_args()
        
        claims = get_jwt_claims()

        qry = PenerimaanDonasi(datetime.datetime.now(), args['donatur'], args['alamat'], args['no_telepon'],args['donasi'],args['cara_bayar'],args['rekening'],args['bukti_transfer'],args['penerima'],args['bukti_terima'],claims['id'])

        db.session.add(qry)
        db.session.commit()

        app.logger.debug('DEBUG : %s ', qry)

        return {"status":"success", "result":marshal(qry, PenerimaanDonasi.response_field)}, 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('donatur',location='json', help='invalid donatur', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('no_telepon',location='json', help='invalid no_telepon', required=True)
        parser.add_argument('donasi',location='json', help='invalid donasi', required=True)
        parser.add_argument('cara_bayar',location='json', help='invalid cara_bayar', required=True)
        parser.add_argument('rekening',location='json', help='invalid rekening')
        parser.add_argument('bukti_transfer',location='json', help='invalid bukti_transfer')
        parser.add_argument('penerima',location='json', help='invalid penerima')
        parser.add_argument('bukti_terima',location='json', help='invalid bukti_terima')
        parser.add_argument('id',location='args', help='invalid id', required=True)
        args = parser.parse_args()

        qry = PenerimaanDonasi.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        qry.donatur = args['donatur']
        qry.alamat = args['alamat']
        qry.no_telepon = args['no_telepon']
        qry.donasi = args['donasi']
        qry.cara_bayar = args['cara_bayar']
        qry.rekening = args['rekening']
        qry.bukti_transfer = args['bukti_transfer']
        qry.penerima = args['penerima']
        qry.bukti_terima = args['bukti_terima']
        db.session.commit()

        return {"status":"success", "result":marshal(qry, PenerimaanDonasi.response_field)}, 200, {'Content-Type':'application/json'}

    
    @jwt_required
    @internal_required
    def delete(self):
        return {"status":"failed", "result":"Delete Not Available Now, Please Contact Developer"}, 403, {'Content-Type':'application/json'}
        
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='json', help='invalid id', required=True)
        args = parser.parse_args()

        qry = PenerimaanDonasi.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        db.session.delete(qry)
        db.session.commit()

        return {"status":"success", "result":marshal(qry, PenerimaanDonasi.response_field)}, 200, {'Content-Type':'application/json'}

class PenerimaanDonasiResourceList(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp',type=int, location='args', default=25)
        parser.add_argument('id',type=int,location='args', help='invalid book id')
        parser.add_argument('cara_bayar',location='args', help='invalid isbn')
        args =parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = PenerimaanDonasi.query

        if args['id'] is not None:
            qry = qry.filter_by(id=args['id'])

        if args['cara_bayar'] is not None:
            qry = qry.filter_by(cara_bayar=args['cara_bayar'])

        result = []
        for row in qry.limit(args['rp']).offset(offset).all():
            result.append(marshal(row, PenerimaanDonasi.response_field))
        
        results = {}
        results['page'] = args['p']
        results['total_page'] = len(result) // args['rp'] +1
        results['per_page'] = args['rp']
        results['data'] = result
        
        return {"status":"success", "result":results}, 200, {'Content-Type':'application/json'}

api.add_resource(PenerimaanDonasiResource, '','')
api.add_resource(PenerimaanDonasiResourceList, '/list')

