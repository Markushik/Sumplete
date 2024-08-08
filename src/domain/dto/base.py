from typing import TypeVar

InputDTO = TypeVar("InputDTO", covariant=True)
OutputDTO = TypeVar("OutputDTO", contravariant=True)
