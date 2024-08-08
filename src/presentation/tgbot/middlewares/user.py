from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from src.domain.constants import DEFAULT_LOCALE
from src.domain.dto.user import UserDTO
from src.domain.usecases.user import CreateUser
from src.infrastructure.redis.gateways.user import UserCacheGateway


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[
            [Union[Message, CallbackQuery], Dict[str, Any]],
            Awaitable[Any],
        ],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        dishka = data["dishka_container"]

        cache = await dishka.get(UserCacheGateway)
        create_user = await dishka.get(CreateUser)

        user = await cache.get(event.from_user.id)

        if user is None:
            await create_user(
                UserDTO(
                    tg_id=event.from_user.id,
                    first_name=event.from_user.first_name,
                    last_name=event.from_user.last_name,
                    username=event.from_user.username,
                    language=DEFAULT_LOCALE,
                    notify=False,
                    style="emoji",
                )
            )

        return await handler(event, data)
