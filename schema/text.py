from marshmallow import Schema, validates_schema
from marshmallow.fields import Raw
from typing import Dict, TextIO, Any
from flask_smorest import abort


class TextSchema(Schema):
    text: Raw = Raw(metadata={'type': 'string', 'format': 'binary'}, required=True)


    @validates_schema
    def validates_text(self, text_data: Dict[str, TextIO], **kwargs: Dict[str, Any]) -> None:
        if text_data['text'].content_type != 'text/csv':
            abort(415, message='Invalid content type')

        
             
                