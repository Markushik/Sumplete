from types import TracebackType
from typing import Protocol


class IUoW(Protocol):
    async def __aenter__(self):
        return self

    async def __aexit__(
        self, ex_type: type[BaseException], ex_val: BaseException, ex_tb: TracebackType
    ):
        if ex_type is None:
            await self.commit()
        else:
            await self.rollback()

    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...
