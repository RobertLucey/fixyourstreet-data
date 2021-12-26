import json

from fixyourstreet_data.models.generic import (
    GenericObject,
    GenericObjects,
)


class Categories(GenericObjects):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('child_class', Category)
        super().__init__(*args, **kwargs)

    @staticmethod
    def parse(data):
        # this may be a string
        if isinstance(data, str):
            return json.loads(data)
        elif isinstance(data, list, dict):
            return data
        else:
            raise NotImplementedError()


class Category(GenericObject):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.id = int(kwargs['id'])
        self.title = kwargs['title']

    @property
    def label(self):
        return {
            1: 'graffiti',
            2: 'road_or_path_defects',
            3: 'street_lighting',
            4: 'unknown',
            5: 'leaks_and_drainage',
            6: 'litter_and_illegal_dumping',
            7: 'tree_and_grass_maintenance',
        }[self.id]

    @staticmethod
    def parse(data):
        return Category(
            **data['category']
        )

    def serialize(self):
        return {
            'category': {
                'id': self.id,
                'title': self.title,
                'label': self.label
            }
        }
