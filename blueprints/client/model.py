from blueprints import db
from flask_restful import fields


class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.String(30), unique=True, nullable=False)
    client_secret = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=True, default=False)
    
    response_field = {
        'id': fields.Integer,
        'created_at': fields.DateTime,
        'client_id': fields.String,
        'status': fields.Boolean,
        # True if internal
    }

    def __init__(self,created_at, client_id,client_secret, status):
        self.created_at = created_at
        self.client_id = client_id
        self.client_secret = client_secret
        self.status = status

    def __repr__(self):
        return '<Client %r>' % self.id