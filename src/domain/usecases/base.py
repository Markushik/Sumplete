from typing import Generic

from src.domain.dto.base import InputDTO, OutputDTO


class Usecase(Generic[InputDTO, OutputDTO]):
    async def __call__(self, data: InputDTO) -> OutputDTO:
        pass
