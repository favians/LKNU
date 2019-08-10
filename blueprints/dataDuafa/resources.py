import datetime
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs

from blueprints import internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

from .model import DataDuafa
from blueprints import db, app
from sqlalchemy import desc
# 'client' penamaan (boleh diganti)

bp_dataDuafa = Blueprint('dataDuafa', __name__)
api = Api(bp_dataDuafa)


class DataDuafaResource(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='args', help='invalid id', required=True)
        args = parser.parse_args()

        qry = DataDuafa.query.get(args["id"])

        if qry is not None:
            return {"status":"success", "result":marshal(qry, DataDuafa.response_field)}, 200, {'Content-Type':'application/json'}

        return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama',location='json', help='invalid nama', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('kabupaten',location='json', help='invalid kabupaten', required=True)
        parser.add_argument('kecamatan',location='json', help='invalid kecamatan', required=True)
        parser.add_argument('desa',location='json', help='invalid desa', required=True)
        parser.add_argument('no_telepon',location='json', help='invalid no_telepon')
        parser.add_argument('no_ktp',location='json', help='invalid no_ktp')
        parser.add_argument('status',location='json', help='invalid status')
        parser.add_argument('photo',location='json', help='invalid photo')
        parser.add_argument('pekerjaan',location='json', help='invalid pekerjaan')
        parser.add_argument('tanggungan',location='json', help='invalid tanggungan')
        parser.add_argument('rekom',location='json', help='invalid rekom')
        args = parser.parse_args()
        
        claims = get_jwt_claims()

        qry = DataDuafa(datetime.datetime.now(), args['nama'], args['alamat'], args['kabupaten'],args['kecamatan'],args['desa'],args['no_telepon'],args['no_ktp'],args['status'],args['photo'],args['pekerjaan'],args['tanggungan'],args['rekom'],claims["id"])

        db.session.add(qry)
        db.session.commit()

        app.logger.debug('DEBUG : %s ', qry)

        return {"status":"success", "result":marshal(qry, DataDuafa.response_field)}, 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama',location='json', help='invalid nama', required=True)
        parser.add_argument('alamat',location='json', help='invalid alamat')
        parser.add_argument('kabupaten',location='json', help='invalid kabupaten', required=True)
        parser.add_argument('kecamatan',location='json', help='invalid kecamatan', required=True)
        parser.add_argument('desa',location='json', help='invalid desa', required=True)
        parser.add_argument('no_telepon',location='json', help='invalid no_telepon')
        parser.add_argument('no_ktp',location='json', help='invalid no_ktp')
        parser.add_argument('status',location='json', help='invalid status')
        parser.add_argument('photo',location='json', help='invalid photo')
        parser.add_argument('pekerjaan',location='json', help='invalid pekerjaan')
        parser.add_argument('tanggungan',location='json', help='invalid tanggungan')
        parser.add_argument('rekom',location='json', help='invalid rekom')
        parser.add_argument('id',location='args', help='invalid id')
        args = parser.parse_args()
        
        qry = DataDuafa.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        qry.nama = args['nama']
        qry.alamat = args['alamat']
        qry.kabupaten = args['kabupaten']
        qry.kecamatan = args['kecamatan']
        qry.desa = args['desa']
        qry.no_telepon = args['no_telepon']
        qry.no_ktp = args['no_ktp']
        qry.status = args['status']
        qry.photo = args['photo']
        qry.pekerjaan = args['pekerjaan']
        qry.tanggungan = args['tanggungan']
        qry.rekom = args['rekom']
        db.session.commit()

        return {"status":"success", "result":marshal(qry, DataDuafa.response_field)}, 200, {'Content-Type':'application/json'}

    
    @jwt_required
    @internal_required
    def delete(self):
        return {"status":"failed", "result":"Delete Not Available Now, Please Contact Developer"}, 403, {'Content-Type':'application/json'}
        
        parser = reqparse.RequestParser()
        parser.add_argument('id',location='json', help='invalid id', required=True)
        args = parser.parse_args()

        qry = DataDuafa.query.get(args["id"])

        if qry is None:
            return {'status':'failed',"result":"ID Not Found"}, 404, {'Content-Type':'application/json'}

        db.session.delete(qry)
        db.session.commit()

        return {"status":"success", "result":marshal(qry, DataDuafa.response_field)}, 200, {'Content-Type':'application/json'}

class DataDuafaResourceList(Resource):

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp',type=int, location='args', default=25)
        parser.add_argument('id',type=int,location='args', help='invalid book id')
        parser.add_argument('kabupaten',location='args', help='invalid isbn')
        parser.add_argument('kecamatan',location='args', help='invalid isbn')
        parser.add_argument('desa',location='args', help='invalid isbn')
        args =parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = DataDuafa.query

        if args['id'] is not None:
            qry = qry.filter_by(id=args['id'])

        if args['kabupaten'] is not None:
            qry = qry.filter_by(kabupaten=args['kabupaten'])

        if args['kecamatan'] is not None:
            qry = qry.filter_by(kecamatan=args['kecamatan'])

        if args['desa'] is not None:
            qry = qry.filter_by(desa=args['desa'])

        result = []
        for row in qry.limit(args['rp']).offset(offset).all():
            result.append(marshal(row, DataDuafa.response_field))
        
        results = {}
        results['page'] = args['p']
        results['total_page'] = len(result) // args['rp'] +1
        results['per_page'] = args['rp']
        results['data'] = result
        
        return {"status":"success", "result":results}, 200, {'Content-Type':'application/json'}

api.add_resource(DataDuafaResource, '','')
api.add_resource(DataDuafaResourceList, '/list')

