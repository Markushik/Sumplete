from attrs import define, field


@define(slots=True, kw_only=True)
class UserDTO:
    user_id: int
    user_name: str = field(default=None)
    locale: str = field(default="en")
    anncmt: str = field(default="off")
    style: str = field(default="emoji")
