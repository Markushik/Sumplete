from attrs import define

SIZES = "sizes"
COMPLEXITIES = "complexities"
MODES = "modes"
LANGUAGES = "languages"
STYLES = "styles"
ANNOUNCEMENTS = "announcements"


@define(slots=True)
class Language:
    id: str
    language: str


@define(slots=True)
class Style:
    id: str
    style: str


@define(slots=True)
class Announcement:
    id: str
    switch: str


@define(slots=True)
class Size:
    id: str
    size: str


@define(slots=True)
class Complexity:
    id: str
    complexity: str


@define(slots=True)
class Mode:
    id: str
    mode: str
    message: str
