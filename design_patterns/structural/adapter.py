import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Type
from xml.dom import minidom

DATE_FORMAT = '%d/%m/%Y, %H:%M'


@dataclass
class MediaClass:
    """Abstract Media Class"""

    created: str = datetime.now().strftime(DATE_FORMAT)
    text: str = "<empty>"

    @property
    def __dict__(self):
        return asdict(self)

    @abstractmethod
    def __str__(self) -> str:
        ...


@dataclass
class NewsArticle(MediaClass):
    """News Article Data Class"""

    title: str = "untitled"
    published: str = datetime.now().strftime(DATE_FORMAT)

    def __str__(self) -> str:
        return f'News Article "{self.title}" ({self.published})'


@dataclass
class Tweet(MediaClass):
    """Tweet Data Class"""

    def __str__(self) -> str:
        return f'Tweet "{self.text}" ({self.created})'


class MediaParser(ABC):
    """Abstract Media Parser Class"""

    @abstractmethod
    def parse(self, cls_type: Type[MediaClass], string: str) -> MediaClass:
        ...

    @abstractmethod
    def to_text(self, cls: MediaClass) -> str:
        ...


class JSONMediaParser(MediaParser):
    """XML Media Parser class"""

    @classmethod
    def parse(self, cls_type: Type[MediaClass], string: str) -> MediaClass:
        return cls_type(**json.loads(string))

    @classmethod
    def to_text(self, cls: MediaClass) -> str:
        return json.dumps(cls.__dict__)


class XMLMediaParser(MediaParser):
    """XML Media Parser class"""

    @classmethod
    def parse(self, cls_type: Type[MediaClass], string: str) -> MediaClass:
        root_name = type(cls_type()).__name__
        parsed_xml = minidom.parseString(string)
        if len(parsed_xml.childNodes) != 1:
            raise Exception('XML must have only one root node')

        root = parsed_xml.childNodes[0]
        if root.nodeName != root_name:
            raise ValueError(f'XML Root "{root.nodeName}" is not equal to media type "{root_name}"')

        keys = {}
        for key in asdict(cls_type()):
            for node in root.childNodes:
                if node.nodeName == key:
                    keys[key] = node.childNodes[0].data

        return cls_type(**keys)

    @classmethod
    def to_text(self, cls: MediaClass) -> str:
        root = ET.Element(type(cls).__name__)
        for key in asdict(cls):
            field = ET.SubElement(root, key)
            field.text = getattr(cls, key)
            print(key, getattr(cls, key))
        xml = ET.tostring(root, encoding='unicode')
        return xml


class Adapter:
    """Adapter class"""

    xml_parser = XMLMediaParser()
    json_parser = JSONMediaParser()

    @classmethod
    def json_to_xml(self, cls_type: Type[MediaClass], json: str) -> str:
        parsed_obj = self.json_parser.parse(cls_type, json)
        result = self.xml_parser.to_text(parsed_obj)
        return result

    @classmethod
    def xml_to_json(self, cls_type: Type[MediaClass], xml: str) -> str:
        parsed_obj = self.xml_parser.parse(cls_type, xml)
        result = self.json_parser.to_text(parsed_obj)
        return result

    @classmethod
    def xml_to_obj(self, cls_type: Type[MediaClass], xml: str) -> MediaClass:
        parsed_obj = self.xml_parser.parse(cls_type, xml)
        return parsed_obj

    @classmethod
    def json_to_obj(self, cls_type: Type[MediaClass], json: str) -> MediaClass:
        parsed_obj = self.json_parser.parse(cls_type, json)
        return parsed_obj
