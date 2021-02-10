from gelbooru.enums import TagType
from gelbooru.base import XMLClass



class Tag(XMLClass):

    BASE_URL = "http://gelbooru.com/index.php?page=dapi&s=tag&q=index"

    def __init__(self, **kwargs):
        self.type = TagType(int(kwargs['type']))
        self.count = int(kwargs['count'])
        self.name = kwargs['name']
        self.ambiguous = bool(kwargs['ambiguous'])
        self.id = int(kwargs['id'])

    @classmethod
    def from_name(cls, name):
        return cls.search(name=name)[0]

    def __str__(self):
        return self.name



