from enum import Enum
from gelbooru.base import XMLClass


class TagType(Enum):
    general = 0
    artist = 1
    # 2 seems to be unused
    copyright = 3
    character = 4
    meta = 5
    depreciated = 6


class Tag(XMLClass):

    BASE_URL = "http://gelbooru.com/index.php?page=dapi&s=tag&q=index"

    def __init__(self, **kwargs):
        self.type = TagType(int(kwargs['type']))
        self.count = int(kwargs['count'])
        self.name = kwargs['name']
        self.ambiguous = bool(kwargs['ambiguous'])
        self.id = int(kwargs['id'])


