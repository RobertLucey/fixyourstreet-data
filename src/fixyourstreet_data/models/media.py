# TODO: should probably do some stuff to download media

class Media():

    def __init__(self, *args, **kwargs):
        self.id = int(kwargs['id'])
        self.type = int(kwargs['type'])
        self.link = kwargs['link']
        self.thumb = kwargs['thumb']

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'link': self.link,
            'thumb': self.thumb
        }
