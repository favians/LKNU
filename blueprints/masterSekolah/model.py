from blueprints import db
from flask_restful import fields


class MasterSekolah(db.Model):
    __tablename__ = "master_sekolah"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    nama_sekolah = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    kabupaten = db.Column(db.String(100), nullable=False)
    kecamatan = db.Column(db.String(100), nullable=False)
    desa = db.Column(db.String(100), nullable=False)
    no_telepon = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    kontak_person = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'nama_sekolah': fields.String,
        'alamat': fields.String,
        'kabupaten' : fields.String,
        'kecamatan' : fields.String,
        'desa' : fields.String,
        'no_telepon' : fields.String,
        'email': fields.String,
        'kontak_person': fields.String,
        'client_id': fields.String,
    }

    response_field_sekolah = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, nama_sekolah, alamat, kabupaten, kecamatan, desa, no_telepon, email, kontak_person, client_id):
        self.created_at = created_at
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.desa = desa
        self.no_telepon = no_telepon
        self.email = email
        self.kontak_person = kontak_person
        self.client_id = client_id

    def __repr__(self):
        return '<Master Sekolah %r>' % self.id