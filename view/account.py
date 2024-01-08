from flask_smorest import Blueprint
from flask.views import MethodView
from schema.account import AccountSchema
from model.account import AccountModel
from service.account import login, signup
from typing import Dict
from db import db


blueprint: Blueprint = Blueprint('account', __name__)


@blueprint.route('/login')
class LoginView(MethodView):
    @blueprint.arguments(AccountSchema)
    @blueprint.response(200)
    def post(self, account_data: Dict[str, str]) -> str:
        """
        login API endpoint

        :account_data: Marshmallow schema data
        :return: JSON web Token
        """
        return login(AccountModel, account_data['username'], account_data['password'])


@blueprint.route('/signup')
class SignupView(MethodView):
    @blueprint.arguments(AccountSchema)
    @blueprint.response(201)
    def post(self, account_data: Dict[str, str]) -> None:
        """
        signup API endpoint

        :account_data: Marshmallow schema data
        """
        signup(db, AccountModel, account_data['username'], account_data['password'])

