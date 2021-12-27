import datetime
import string
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
    def has_greeting(self):
        clean_description = self.clean_description.lower()
        clean_description = clean_description.translate(
            str.maketrans('', '', string.punctuation)
        )
        return set(
            ['hi', 'hello', 'greetings', 'hey', 'dear']
        ).intersection(set(clean_description.split())) != set()

    @property
    def has_thanks(self):
        clean_description = self.clean_description.lower()
        return any([
            'thank you' in clean_description,
            'thanks' in clean_description,
            'cheers' in clean_description,
            'regards' in clean_description,
            'sincerely' in clean_description,
        ]) or 'ta' == clean_description.split()[-1]

    @property
    def clean_description(self):
        clean_description = self.description.replace('-- posted via the fixyourstreet.ie public api', '')
        clean_description = clean_description.replace('\r\n----\r\n\r\n\r\n -- posted via the fixyourstreet.ie public api', '')
        clean_description = clean_description.replace('\r\n\r\n. Submitted via EPA/NIECE Smartphone App.', '')
        clean_description = clean_description.replace('Submitted via EPA/NIECE Smartphone App.', '')
        clean_description = clean_description.replace('----\r\nThis report was originally submitted at FixMyStreet.ie. You can find it at this alternate address:', '')
        clean_description = clean_description.replace('-- posted via fixyourstreet.ie mobile web', '')
        clean_description = clean_description.replace('-- posted via fixyourstreet.ie', '')
        clean_description = clean_description.replace('posted via fixyourstreet.ie', '')
        clean_description = clean_description.replace('-- received via Twitter (Contact us at @fixyourstreet or using the hashtag #fysie). Catch up with us on http://twitter.com/fixyourstreet', '')
        clean_description = clean_description.replace('#Waste/IllegalDumping', '')
        clean_description = clean_description.replace('#Air/Odour', '')
        clean_description = clean_description.replace('#Water', '')
        clean_description = clean_description.replace('#DrinkingWater', '')
        clean_description = clean_description.replace('#PublicLighting', '')
        clean_description = clean_description.replace('#Noise', '')
        clean_description = clean_description.replace('----', '')
        clean_description = clean_description.replace('\r\n.', '.')
        clean_description = clean_description.replace('Ã¢Â€Â™', '\'')
        clean_description = clean_description.replace('Â’', '\'')
        clean_description = clean_description.replace('\'Â€Â™', '\'')
        clean_description = clean_description.replace('Â”', '”')

        clean_description = clean_description.replace('!.', '!')
        clean_description = clean_description.replace('?.', '?')
        clean_description = clean_description.replace(' .', '.')

        clean_description = re.sub(r'https:\/\/fixmystreet\.ie\/report\/\d+', '', clean_description)
        clean_description = re.sub(r' +', ' ', clean_description)
        clean_description = re.sub('(\r\n)+', '\r\n', clean_description)

        lines = clean_description.split('\r\n')
        clean_description = '\r\n'.join([l.strip() for l in lines])

        return clean_description.strip()

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
