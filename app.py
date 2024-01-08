from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from view.account import blueprint as account
from view.records import blueprint as records
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS
import model
from db import db
import os
import base64


def main() -> None:
    # APP
    app: Flask = Flask(__name__)

    # APP CONFIG
    app.config['API_TITLE'] = 'api'
    app.config['API_VERSION'] = '1'
    app.config['OPENAPI_VERSION'] = '3.1.0'

    # DB CONFIG
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    migrate: Migrate = Migrate(app, db)

    # API 
    api: Api = Api(app)

    # BLUEPRINT
    api.register_blueprint(account)
    api.register_blueprint(records)

    # JWT CONFIG
    app.config['JWT_SECRET_KEY'] = base64.urlsafe_b64encode(os.urandom(32)).decode()
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
    jwt: JWTManager = JWTManager(app)

    # CORS CONFIG
    cors: CORS = CORS(app, resources={r'*': {'origins': '*'}})

    app.run(debug=True)


if __name__ == '__main__':
    main()