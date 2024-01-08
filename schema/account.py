from marshmallow import Schema
from marshmallow.fields import Int, Str


class AccountSchema(Schema):
    id: Int = Int(dump_only=True)
    username: Str = Str(required=True)
    password: Str = Str(required=True)