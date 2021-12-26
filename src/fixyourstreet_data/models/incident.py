from fixyourstreet_data.models.location import Location
from fixyourstreet_data.models.generic import (
    GenericObject,
    GenericObjects,
)


class Incidents(GenericObjects):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('child_class', Incident)
        super().__init__(*args, **kwargs)


class Incident(GenericObject):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.id = int(kwargs['incidentid'])
        self.active = int(kwargs['incidentactive'])
        self.date = kwargs['incidentdate']
        self.description = kwargs['incidentdescription']
        self.mode = int(kwargs['incidentmode'])
        self.title = kwargs['incidenttitle']
        self.verified = int(kwargs['incidentverified'])

        if 'incidentlocation' in kwargs:
            self.location = Location(**kwargs['incidentlocation'])
        else:
            self.location = Location(**kwargs)

    def serialize(self):
        return {
            'incidentid': self.id,
            'incidentactive': self.active,
            'incidentdate': self.date,
            'incidentdescription': self.description,
            'incidentmode': self.mode,
            'incidenttitle': self.title,
            'incidentverified': self.verified,
            'incidentlocation': self.location.serialize()
        }
