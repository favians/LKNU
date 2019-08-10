from blueprints import db
from flask_restful import fields


class Donatur(db.Model):
    __tablename__ = "donatur"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    kabupaten = db.Column(db.String(100), nullable=False)
    kecamatan = db.Column(db.String(100), nullable=False)
    desa = db.Column(db.String(100), nullable=False)
    no_telepon = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    institusi = db.Column(db.String(100), nullable=True)
    
    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'nama': fields.String,
        'alamat': fields.String,
        'kabupaten' : fields.String,
        'kecamatan' : fields.String,
        'desa' : fields.String,
        'no_telepon' : fields.String,
        'email': fields.String,
        'institusi': fields.String,
    }

    response_field_sekolah = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, nama, alamat, kabupaten, kecamatan, desa, no_telepon, email, institusi):
        self.created_at = created_at
        self.nama = nama
        self.alamat = alamat
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.desa = desa
        self.no_telepon = no_telepon
        self.email = email
        self.institusi = institusi

    def __repr__(self):
        return '<Donatur %r>' % self.id