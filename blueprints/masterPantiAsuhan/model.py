from blueprints import db
from flask_restful import fields


class MasterPantiAsuhan(db.Model):
    __tablename__ = "master_panti_asuhan"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    nama_panti_asuhan = db.Column(db.String(100), nullable=False)
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
        'nama_panti_asuhan': fields.String,
        'alamat': fields.String,
        'kabupaten' : fields.String,
        'kecamatan' : fields.String,
        'desa' : fields.String,
        'no_telepon' : fields.String,
        'email': fields.String,
        'kontak_person': fields.String,
        'client_id': fields.String,
    }

    response_field_panti = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, nama_panti_asuhan, alamat, kabupaten, kecamatan, desa, no_telepon, email, kontak_person, client_id):
        self.created_at = created_at
        self.nama_panti_asuhan = nama_panti_asuhan
        self.alamat = alamat
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.desa = desa
        self.no_telepon = no_telepon
        self.email = email
        self.kontak_person = kontak_person
        self.client_id = client_id

    def __repr__(self):
        return '<Master Panti Asuhan %r>' % self.id