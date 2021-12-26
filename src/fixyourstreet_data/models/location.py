class Location():

    def __init__(self, *args, **kwargs):
        self.id = int(kwargs['locationid'])
        self.latitude = float(kwargs['locationlatitude'])
        self.longitude = float(kwargs['locationlongitude'])
        self.name = kwargs['locationname']

    def serialize(self):
        return {
            'locationid': self.id,
            'locationlatitude': self.latitude,
            'locationlongitude': self.longitude,
            'locationname': self.name
        }
