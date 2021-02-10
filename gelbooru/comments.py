from gelbooru.base import XMLClass
from datetime import datetime, timezone


class Comment(XMLClass):

    BASE_URL = "http://gelbooru.com/index.php?page=dapi&s=comment&q=index"

    def __init__(self, **kwargs):
        self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
        self.post_id = int(kwargs["post_id"])
        self.body = kwargs["body"]
        self.creator = kwargs["creator"]
        self.id = int(kwargs["id"])
        self.creator_id = int(kwargs["creator_id"])

    def __str__(self):
        return self.body