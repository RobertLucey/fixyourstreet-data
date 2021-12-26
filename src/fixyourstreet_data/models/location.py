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
            (self.latitude, self.longitude)
        )[0])

    def serialize(self, minimal=True):
        data = {
            'locationid': self.id,
            'locationlatitude': self.latitude,
            'locationlongitude': self.longitude,
            'locationname': self.name,
        }

        if not minimal:
            data['geo'] = self.reverse_geo

        return data
