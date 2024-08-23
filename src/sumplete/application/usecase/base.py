from typing import Generic, TypeVar

InputDTO = TypeVar("InputDTO", covariant=True)
OutputDTO = TypeVar("OutputDTO", contravariant=True)


class Interactor(Generic[InputDTO, OutputDTO]):
    async def __call__(self, data: InputDTO) -> OutputDTO:
        pass
