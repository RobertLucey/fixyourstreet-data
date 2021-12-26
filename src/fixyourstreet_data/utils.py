import os
import json
from functools import reduce

from pandas import (
    read_csv,
    json_normalize,
    DataFrame
)

from fixyourstreet_data.settings import (
    BASE_DIR,
    DATA_FILE_PATH
)
from fixyourstreet_data.models.report import Reports


def dot_to_json(a):
    output = {}
    for key, value in a.items():
        path = key.split('.')
        if path[0] == 'json':
            path = path[1:]
        target = reduce(lambda d, k: d.setdefault(k, {}), path[:-1], output)
        target[path[-1]] = value
    return output


def get_reports():
    os.makedirs(BASE_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE_PATH):
        return Reports()
    else:
        csv_data = read_csv(DATA_FILE_PATH)
        json_data = json.loads(
            csv_data.to_json(orient='records')
        )
        data = []
        for item in json_data:
            # FIXME: for some reason media is added to the csv and overwrites the media.whatever
            del item['media']
            data.append(dot_to_json(item))
        return Reports(data=data)


def save_reports(reports):
    os.makedirs(BASE_DIR, exist_ok=True)
    if isinstance(reports, Reports):
        data = json_normalize(reports.serialize(), max_level=10)
        data.to_csv(DATA_FILE_PATH)
    elif isinstance(reports, list):
        raise NotImplementedError()
    elif isinstance(reports, DataFrame):
        raise NotImplementedError()
