import re

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

    @property
    def clean_description(self):
        string = self.description.replace('-- posted via the fixyourstreet.ie public api', '')
        string = string.replace('\r\n----\r\n\r\n\r\n -- posted via the fixyourstreet.ie public api', '')
        string = string.replace('\r\n\r\n. Submitted via EPA/NIECE Smartphone App.', '')
        string = string.replace('Submitted via EPA/NIECE Smartphone App.', '')
        string = string.replace('----\r\nThis report was originally submitted at FixMyStreet.ie. You can find it at this alternate address:', '')
        string = string.replace('-- posted via fixyourstreet.ie mobile web', '')
        string = string.replace('-- posted via fixyourstreet.ie', '')
        string = string.replace('#Waste/IllegalDumping', '')
        string = string.replace('----', '')

        string = re.sub(r'https:\/\/fixmystreet\.ie\/report\/\d+', '', string)

        return string.strip()


    def serialize(self, minimal=True):
        data = {
            'incidentid': self.id,
            'incidentactive': self.active,
            'incidentdate': self.date,
            'incidentdescription': self.description,
            'incidentmode': self.mode,
            'incidenttitle': self.title,
            'incidentverified': self.verified,
            'incidentlocation': self.location.serialize(minimal=minimal)
        }

        if not minimal:
            data['clean_description'] = self.clean_description

        return data
