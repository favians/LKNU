from blueprints import db
from flask_restful import fields


class Penyaluran(db.Model):
    __tablename__ = "penyaluran"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    yatim_duafa = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    peyaluran = db.Column(db.String(100), nullable=False)
    cara_bayar = db.Column(db.String(100), nullable=False)
    rekening = db.Column(db.String(100), nullable=True)
    penerima = db.Column(db.String(100), nullable=True)
    bukti = db.Column(db.String(100), nullable=True)
    keterangan = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'yatim_duafa': fields.String,
        'alamat': fields.String,
        'peyaluran' : fields.String,
        'cara_bayar' : fields.String,
        'rekening' : fields.String,
        'penerima' : fields.String,
        'bukti' : fields.String,
        'keterangan': fields.String,
        'client_id': fields.String,
    }

    response_field_penyaluran = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, yatim_duafa, alamat, peyaluran, cara_bayar, rekening, penerima, bukti, keterangan, client_id):
        self.created_at = created_at
        self.yatim_duafa = yatim_duafa
        self.alamat = alamat
        self.peyaluran = peyaluran
        self.cara_bayar = cara_bayar
        self.rekening = rekening
        self.penerima = penerima
        self.bukti = bukti
        self.keterangan = keterangan
        self.client_id = client_id

    def __repr__(self):
        return '<Penyaluran %r>' % self.id