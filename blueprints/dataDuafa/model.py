from blueprints import db
from flask_restful import fields


class DataDuafa(db.Model):
    __tablename__ = "data_duafa"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    kabupaten = db.Column(db.String(100), nullable=False)
    kecamatan = db.Column(db.String(100), nullable=False)
    desa = db.Column(db.String(100), nullable=False)
    no_telepon = db.Column(db.String(100), nullable=True)
    no_ktp = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(100), nullable=True)
    photo = db.Column(db.String(255), nullable=True)
    pekerjaan = db.Column(db.String(100), nullable=True)
    tanggungan = db.Column(db.String(100), nullable=True)
    rekom = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)

    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'nama': fields.String,
        'alamat': fields.String,
        'kabupaten' : fields.String,
        'kecamatan' : fields.String,
        'desa' : fields.String,
        'no_telepon' : fields.String,
        'no_ktp' : fields.String,
        'status' : fields.String,
        'photo' : fields.String,
        'pekerjaan' : fields.String,
        'tanggungan' : fields.String,
        'rekom': fields.String,
        'client_id': fields.Integer,
    }

    response_field_sekolah = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, nama, alamat, kabupaten, kecamatan, desa, no_telepon, no_ktp, status, photo, pekerjaan, tanggungan, rekom, client_id):
        self.created_at = created_at
        self.nama = nama
        self.alamat = alamat
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.desa = desa
        self.no_telepon = no_telepon
        self.no_ktp = no_ktp
        self.status = status
        self.photo = photo
        self.pekerjaan = pekerjaan
        self.tanggungan = no_telepon
        self.rekom = rekom
        self.client_id = client_id

    def __repr__(self):
        return '<Data Duafa %r>' % self.id