import datetime
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
    def timestamp(self):
        return datetime.datetime.strptime(self.date, '%Y-%m-%d %H:%M:%S')

    @property
    def clean_description(self):
        string = self.description.replace('-- posted via the fixyourstreet.ie public api', '')
        string = string.replace('\r\n----\r\n\r\n\r\n -- posted via the fixyourstreet.ie public api', '')
        string = string.replace('\r\n\r\n. Submitted via EPA/NIECE Smartphone App.', '')
        string = string.replace('Submitted via EPA/NIECE Smartphone App.', '')
        string = string.replace('----\r\nThis report was originally submitted at FixMyStreet.ie. You can find it at this alternate address:', '')
        string = string.replace('-- posted via fixyourstreet.ie mobile web', '')
        string = string.replace('-- posted via fixyourstreet.ie', '')
        string = string.replace('-- received via Twitter (Contact us at @fixyourstreet or using the hashtag #fysie). Catch up with us on http://twitter.com/fixyourstreet', '')
        string = string.replace('#Waste/IllegalDumping', '')
        string = string.replace('#Air/Odour', '')
        string = string.replace('#Water', '')
        string = string.replace('#DrinkingWater', '')
        string = string.replace('#PublicLighting', '')
        string = string.replace('#Noise', '')
        string = string.replace('----', '')
        string = string.replace('\r\n.', '.')
        string = string.replace('\r\n\r\n', '\r\n')
        string = string.replace('Ã¢Â€Â™', '\'')

        string = re.sub(r'https:\/\/fixmystreet\.ie\/report\/\d+', '', string)
        string = re.sub(r' +', ' ', string)

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
