from pandas import read_csv
from flask_smorest import abort
from typing import TextIO, List, Dict


def records(text: TextIO, keys: List[str]) -> List[Dict[str, str]]:
    """
    reads the text, configures the data and convert to records

    :text: raw text
    :keys: keys to configure the data
    :return: records
    """
    try:
        return {'records': read_csv(text)[keys].to_dict(orient='records')}
    except KeyError as error:
        abort(404, message=f"Key '{error}' not found")


