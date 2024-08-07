from attr import define

SIZES = 'sizes'
COMPLEXITIES = 'complexities'
MODES = 'modes'
LANGUAGES = 'langs'
STYLES = 'styles'
TOGGLES = 'toggles'
ID_LIST_SCROLL = 'list_scroll'


@define(slots=True)
class Localization:
    id: str
    language: str
    locale: str


@define(slots=True)
class Customization:
    id: str
    style: str


@define(slots=True)
class Notification:
    id: str
    toggle: str


@define(slots=True)
class Dimension:
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
