from blueprints import db
from flask_restful import fields


class DataYatim(db.Model):
    __tablename__ = "data_yatim"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    kabupaten = db.Column(db.String(100), nullable=False)
    kecamatan = db.Column(db.String(100), nullable=False)
    desa = db.Column(db.String(100), nullable=False)
    tanggal_lahir = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    sekolah = db.Column(db.String(100), nullable=True)
    kelas = db.Column(db.String(100), nullable=True)
    nama_ayah = db.Column(db.String(100), nullable=True)
    status_ayah = db.Column(db.String(100), nullable=True)
    id_ayah = db.Column(db.String(100), nullable=True)
    nama_ibu = db.Column(db.String(100), nullable=True)
    status_ibu = db.Column(db.String(100), nullable=True)
    id_ibu = db.Column(db.String(100), nullable=True)
    wali = db.Column(db.String(100), nullable=True)
    no_telepon = db.Column(db.String(100), nullable=True)
    panti = db.Column(db.String(100), nullable=True)
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
        'tanggal_lahir' : fields.String,
        'photo' : fields.String,
        'sekolah' : fields.String,
        'kelas' : fields.String,
        'nama_ayah' : fields.String,
        'status_ayah' : fields.String,
        'id_ayah' : fields.String,
        'nama_ibu' : fields.String,
        'status_ibu' : fields.String,
        'id_ibu' : fields.String,
        'wali' : fields.String,
        'no_telepon' : fields.String,
        'panti': fields.String,
        'rekom': fields.String,
        'client_id': fields.String,
    }

    response_field_yatim = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, nama, alamat, kabupaten, kecamatan, desa, tanggal_lahir, photo, sekolah, kelas, nama_ayah, status_ayah, id_ayah, nama_ibu, status_ibu, id_ibu, wali, no_telepon, panti, rekom, client_id):
        self.created_at = created_at
        self.nama = nama
        self.alamat = alamat
        self.kabupaten = kabupaten
        self.kecamatan = kecamatan
        self.desa = desa
        self.tanggal_lahir = tanggal_lahir
        self.photo = photo
        self.sekolah = sekolah
        self.kelas = kelas
        self.nama_ayah = nama_ayah
        self.status_ayah = status_ayah
        self.id_ayah = id_ayah
        self.nama_ibu = nama_ibu
        self.status_ibu = status_ibu
        self.id_ibu = id_ibu
        self.wali = wali
        self.no_telepon = no_telepon
        self.panti = panti
        self.rekom = rekom
        self.client_id = client_id

    def __repr__(self):
        return '<Data Yatim %r>' % self.id