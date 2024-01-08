from flask_smorest import Blueprint
from flask.views import MethodView
from schema.text import TextSchema
from schema.config import ConfigSchema
from flask_jwt_extended import jwt_required
from service.records import records
from typing import List, Dict, TextIO


blueprint: Blueprint = Blueprint('records', __name__)


@blueprint.route('/records')
class RecordsView(MethodView):
    @jwt_required()
    @blueprint.arguments(TextSchema, location='files')
    @blueprint.arguments(ConfigSchema)
    @blueprint.response(200)
    def post(self, text_data: Dict[str, TextIO], config_data: Dict[str, List[str]]) -> Dict[str, List[Dict[str, str]]]:
        """
        records API endpoint

        :text_data: Marshmallow schema data
        :config_data: Marshmallow schema data
        :return: records
        """
        return records(text_data['text'], config_data['keys'])


            

    