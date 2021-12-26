from cached_property import cached_property
import reverse_geocoder


class Location():

    def __init__(self, *args, **kwargs):
        self.id = int(kwargs['locationid'])
        self.latitude = float(kwargs['locationlatitude'])
        self.longitude = float(kwargs['locationlongitude'])
        self.name = kwargs['locationname']

    @cached_property
    def reverse_geo(self):
        return dict(reverse_geocoder.search(
            (self.lat, self.lng)
        )[0])

    def serialize(self):
        return {
            'locationid': self.id,
            'locationlatitude': self.latitude,
            'locationlongitude': self.longitude,
            'locationname': self.name,
            'geo': self.reverse_geo
        }
