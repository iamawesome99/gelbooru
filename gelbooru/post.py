from typing import Union
from datetime import datetime, timezone
from gelbooru.enums import PostRating
from gelbooru.tagquery import Options, Query, Term, AllowedTerms
from gelbooru.base import XMLClass, download_image
from PIL import Image


class Post(XMLClass):
    BASE_URL = "http://gelbooru.com/index.php?page=dapi&s=post&q=index"

    def __init__(self, **kwargs):
        self.height = int(kwargs["height"])
        self.score = int(kwargs["score"])
        self.file_url = kwargs["file_url"]
        self.parent_id = int(kwargs["parent_id"]) if kwargs["parent_id"] else None
        self.sample_url = kwargs["sample_url"]
        self.sample_width = int(kwargs["sample_width"])
        self.sample_height = int(kwargs["sample_height"])
        self.preview_url = kwargs["preview_url"]
        self.rating = PostRating(kwargs["rating"])
        self.list_tags = kwargs["tags"].strip().split(" ")
        self.id = int(kwargs["id"])
        self.width = int(kwargs["width"])
        self.change = datetime.utcfromtimestamp(int(kwargs["change"]))
        self.md5 = kwargs["md5"]
        self.creator_id = int(kwargs["creator_id"])
        self.has_children = bool(kwargs["has_children"])
        self.created_at = datetime.strptime(kwargs["created_at"], "%a %b %d %H:%M:%S %z %Y").replace(
            tzinfo=timezone.utc)
        self.status = kwargs["status"]  # TODO: Make this into an enum once I figure out the possible values.
        self.source = kwargs["source"]
        self.has_notes = bool(kwargs["has_notes"])
        self.has_comments = bool(kwargs["has_comments"])
        self.preview_width = int(kwargs["preview_width"])
        self.preview_height = int(kwargs["preview_height"])

    def get_image(self) -> Image:
        return download_image(self.file_url)

    def get_sample(self) -> Image:
        return download_image(self.sample_url)

    def get_preview(self) -> Image:
        return download_image(self.preview_url)

    @classmethod
    def search_tags(cls, query: Union[Options, Query, Term, AllowedTerms, str], **kwargs):
        print(str(query))
        return cls.search(tags=str(query), **kwargs)
