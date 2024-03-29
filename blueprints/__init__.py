from flask import Flask, request
import json

##database import###
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import Manager

##JWT import
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from datetime import timedelta

#wrap
from functools import wraps


app = Flask(__name__)
app.config['APP_DEBUG'] = True

#################
# JWT
###############

app.config['JWT_SECRET_KEY'] = 'Sfasdlah8xPnS73nS3dhb'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)
    
def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['status']:
            return {'status':'failed', 'message':'FORBIDDEN | Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


def non_internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['status']:
            return {'status':'failed', 'message':'FORBIDDEN | Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


####Database####


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://a:b@c:3306/LKNU'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)  # command 'db' dapat menjalankan semua command MigrateCommand

###########Middleware#############
@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    app.logger.warning("REQUEST_LOG\t%s", 
        json.dumps({
            'uri':request.full_path,
            'code':response.status,
            'method':request.method,
            'request':requestData,
            'response':json.loads(response.data.decode('utf-8'))}))

    return response


###############################
# Import blueprints
###############################

from blueprints.auth import bp_auth
from blueprints.client.resources import bp_client
from blueprints.strukturOrganisasi.resources import bp_strukturOrganisasi
from blueprints.masterSekolah.resources import bp_masterSekolah
from blueprints.masterPantiAsuhan.resources import bp_masterPantiAsuhan
from blueprints.donatur.resources import bp_donatur
from blueprints.dataDuafa.resources import bp_dataDuafa
from blueprints.dataYatim.resources import bp_dataYatim
from blueprints.penerimaanDonasi.resources import bp_penerimaanDonasi
from blueprints.penyaluran.resources import bp_penyaluran

app.register_blueprint(bp_auth, url_prefix='/login')
app.register_blueprint(bp_client, url_prefix='/client' )
app.register_blueprint(bp_strukturOrganisasi, url_prefix='/strukturorganisasi' )
app.register_blueprint(bp_masterSekolah, url_prefix='/mastersekolah' )
app.register_blueprint(bp_masterPantiAsuhan, url_prefix='/masterpantiasuhan' )
app.register_blueprint(bp_donatur, url_prefix='/donatur' )
app.register_blueprint(bp_dataDuafa, url_prefix='/dataduafa' )
app.register_blueprint(bp_dataYatim, url_prefix='/datayatim' )
app.register_blueprint(bp_penerimaanDonasi, url_prefix='/penerimaandonasi' )
app.register_blueprint(bp_penyaluran, url_prefix='/penyaluran' )

db.create_all()
