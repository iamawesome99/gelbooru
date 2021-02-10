import requests
import xml.etree.ElementTree as ET
from PIL import Image


def download_image(url: str) -> Image:
    return Image.open(requests.get(url, stream=True).raw)


class XMLClass:
    BASE_URL = "http://gelbooru.com"

    def __init__(self, **kwargs):
        raise NotImplementedError

    @classmethod
    def from_id(cls, id: int):
        return cls(
            **ET.fromstring(requests.get(cls.BASE_URL + "&id=" + str(id)).text)[0].attrib
        )

    @classmethod
    def from_list(cls, xml: str, get_count=False):
        root = ET.fromstring(xml)
        if not get_count:
            return [cls(**x.attrib) for x in root]
        return [cls(**x.attrib) for x in root], root.attrib["count"]

    @classmethod
    def search(cls, **kwargs):
        return cls.from_list(requests.get(
            "&".join([cls.BASE_URL, *[key + "=" + str(value) for key, value in kwargs.items()]])
        ).text)
