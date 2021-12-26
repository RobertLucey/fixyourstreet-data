import ast
import json

from fixyourstreet_data.models.media import Media
from fixyourstreet_data.models.category import Categories
from fixyourstreet_data.models.incident import Incident
from fixyourstreet_data.models.generic import (
    GenericObject,
    GenericObjects,
)


class Reports(GenericObjects):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('child_class', Report)
        super().__init__(*args, **kwargs)


class Report(GenericObject):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.incident = Incident(**kwargs['incident'])
        if isinstance(kwargs['media'], list) or kwargs['media'] is None:
            self.media = None
        else:
            if kwargs['media']['id']is None:
                self.media = None
            else:
                self.media = Media(**kwargs['media'])

        if isinstance(kwargs['categories'], str):
            try:
                self.categories = Categories(data=json.loads(kwargs['categories']))
            except:
                self.categories = Categories(data=ast.literal_eval(kwargs['categories']))
        else:
            self.categories = Categories(data=kwargs['categories'])

    @staticmethod
    def parse(data):
        return Report(**data)

    def serialize(self):
        return {
            'incident': self.incident.serialize(),
            'media': self.media.serialize() if self.media is not None else None,
            'categories': self.categories.serialize()
        }
