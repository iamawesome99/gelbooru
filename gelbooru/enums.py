from enum import Enum


class PostRating(Enum):
    safe = "s"
    questionable = "q"
    explicit = "e"


class InvRating(Enum):
    safe = "-s"
    questionable = "-q"
    explicit = "-e"


class SortTypes(Enum):
    id = "id"
    score = "score"
    rating = "rating"
    user = "user"
    height = "height"
    width = "width"
    source = "source"
    updated = "updated"
    random = "random"


class SortOrder(Enum):
    asc = "asc"
    desc = "desc"


class TagType(Enum):
    general = 0
    artist = 1
    # 2 seems to be unused
    copyright = 3
    character = 4
    meta = 5
    depreciated = 6