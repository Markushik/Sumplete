from attrs import define, field


@define(slots=True)
class UserDTO:
    tg_id: int = field(default=False)
    first_name: str = field(default=False)
    last_name: str = field(default=False)
    username: str = field(default=False)
    language: str = field(default=False)
    notify: bool = field(default=bool)
    style: str = field(default=False)
