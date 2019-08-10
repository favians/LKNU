from blueprints import db
from flask_restful import fields


class PenerimaanDonasi(db.Model):
    __tablename__ = "penerimaan_donasi"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    donatur = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=True)
    no_telepon = db.Column(db.String(100), nullable=True)
    donasi = db.Column(db.String(100), nullable=True)
    cara_bayar = db.Column(db.String(100), nullable=True)
    rekening = db.Column(db.String(100), nullable=False)
    bukti_transfer = db.Column(db.String(255), nullable=False)
    penerima = db.Column(db.String(100), nullable=False)
    bukti_terima = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'donatur': fields.String,
        'alamat': fields.String,
        'no_telepon' : fields.String,
        'donasi': fields.String,
        'cara_bayar': fields.String,
        'rekening': fields.String,
        'bukti_transfer': fields.String,
        'penerima': fields.String,
        'bukti_terima': fields.String,
        'client_id': fields.String,
    }

    response_field_penerimaan_donasi = {
        'page': fields.Integer,
        'total_page': fields.Integer,
        'per_page': fields.Integer    
    }

    def __init__(self, created_at, donatur, alamat, no_telepon, donasi, cara_bayar, rekening, bukti_transfer, penerima, bukti_terima, client_id):
        self.created_at = created_at
        self.donatur = donatur
        self.alamat = alamat
        self.no_telepon = no_telepon
        self.donasi = donasi
        self.cara_bayar = cara_bayar
        self.rekening = rekening
        self.bukti_transfer = bukti_transfer
        self.penerima = penerima
        self.bukti_terima = bukti_terima
        self.client_id = client_id

    def __repr__(self):
        return '<PenerimaanDonasi %r>' % self.id