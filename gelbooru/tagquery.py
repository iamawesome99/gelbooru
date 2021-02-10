from __future__ import annotations

from gelbooru.tag import Tag
from typing import Union, TypeVar, Optional
from gelbooru.enums import InvRating, PostRating, SortTypes, SortOrder

# i both hate this amd love it
# statically typed python let's go

AllowedTerms = TypeVar("AllowedTerms", str, Tag)


class Term:
    def __init__(self, term: AllowedTerms):
        self.query = term

    def __str__(self):
        return str(self.query)


class Query:
    def __init__(self, *args: Union[AllowedTerms, Term, Query]):
        self.query = args

    def __str__(self):
        return " ".join([str(x) for x in self.query])


class Or(Query):
    def __str__(self):
        return "{" + " ~ ".join([str(x) for x in self.query]) + "}"


class Not(Term):
    def __str__(self):
        return "-" + str(self.query)


class Fuzzy(Term):
    def __str__(self):
        return str(self.query) + "~"


class Greater:
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return ">" + str(self.number)


class Lesser:
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return "<" + str(self.number)


class Options:
    def __init__(self, *query: Union[AllowedTerms, Term, Query], user: Optional[str] = None, md5: Optional[str] = None,
                 rating: Optional[Union[InvRating, PostRating]] = None, width: Optional[Union[Greater, Lesser]] = None,
                 height: Optional[Union[Greater, Lesser]] = None, score: Optional[Union[Greater, Lesser]] = None,
                 fav: Optional[int] = None, pool: Optional[int] = None, sort: Optional[SortTypes] = None,
                 sort_order: Optional[SortOrder] = None, random_seed: Optional[int] = None):
        self.random_seed = random_seed
        self.sort_order = sort_order
        self.sort = sort
        self.pool = pool
        self.fav = fav
        self.score = score
        self.height = height
        self.width = width
        self.rating = rating
        self.md5 = md5
        self.user = user
        self.query = Query(*query)

    def __str__(self):
        out = str(self.query)

        if self.user:
            out += " user:" + self.user
        if self.md5:
            out += " user:" + self.md5
        if self.rating:
            if type(self.rating) == PostRating:
                out += " rating:" + self.rating.name
            else:
                out += " -rating:" + self.rating.name
        if self.width:
            out += " width:" + str(self.width)
        if self.height:
            out += " height:" + str(self.height)
        if self.score:
            out += " score:" + str(self.score)
        if self.fav:
            out += " fav:" + str(self.fav)
        if self.pool:
            out += " pool:" + str(self.pool)
        if self.sort:
            if self.sort == SortTypes.random:
                if self.random_seed:
                    out += " sort:random:" + str(self.random_seed)
                else:
                    out += " sort:random"
            else:
                if self.sort_order:
                    out += " sort:" + self.sort.value + ":" + self.sort_order.value
                else:
                    out += " sort:" + self.sort.value

        return out
