from bleach import clean
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.model import Model
from flask_sqlalchemy import SQLAlchemy


def login(model: Model, username: str, password: str) -> str:
    """
    authenticates account and creates JSON Web Token

    :model: SQLAlchemy database model
    :username: Username to authenticate
    :password: Password to authenticate
    :return: JSON Web Token
    """
    account = model.query.filter(model.username == clean(username)).first()

    if account and pbkdf2_sha256.verify(clean(password), account.password):
        return {'jwt': create_access_token(identity=account.id)}
    else:
        abort(401, message='Invalid username or password')


def signup(db: SQLAlchemy, model: Model, username: str, password: str) -> None:
    """
    inserts account into database

    :db: SQLAlchemy database session
    :model: SQLAlchemy database model 
    :username: Username to authenticate
    :password: Password to authenticate
    """
    try:
        account = model(username=clean(username), password=pbkdf2_sha256.hash(clean(password)))
        db.session.add(account)
        db.session.commit()
    except SQLAlchemyError:
        abort(409, message='Username already exists')