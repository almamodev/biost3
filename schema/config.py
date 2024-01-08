from marshmallow import Schema
from marshmallow.fields import List, Str


class ConfigSchema(Schema):
    keys: List = List(Str(), required=True)