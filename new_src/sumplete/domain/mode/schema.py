from attrs import define

from ..base.schema import BaseSchema


@define(slots=True)
class Mode(BaseSchema):
    id: str
    mode: str
    message: str
