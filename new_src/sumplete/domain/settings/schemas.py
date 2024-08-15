from attrs import define

from ..base.schema import BaseSchema


@define(slots=True)
class Locale(BaseSchema):
    id: str
    locale: str


@define(slots=True)
class Style(BaseSchema):
    id: str
    style: str


@define(slots=True)
class Announcement(BaseSchema):
    id: str
    switch: str
