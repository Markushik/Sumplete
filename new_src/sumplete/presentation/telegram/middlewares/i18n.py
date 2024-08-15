from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from aiogram.types import TelegramObject
from fluent.runtime import FluentLocalization

from new_src.sumplete.adapters.redis.adapter.implement import RedisAdapter
from new_src.sumplete.domain.user.usecase import UserDTO


class I18nMiddleware(BaseMiddleware):
    def __init__(
        self,
        l10ns: Dict[str, FluentLocalization],
    ):
        super().__init__()
        self.l10ns = l10ns

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: dict[str, Any],
    ) -> Any:
        dishka = data["dishka_container"]

        cache = await dishka.get(RedisAdapter)
        locale = await cache.get_locale(event.from_user.id)

        # if locale is None:
        #     create_user = await dishka.get(...)  # create user usecase
        #     await create_user(
        #         UserDTO(
        #             user_id=event.from_user.id,
        #             first_name=event.from_user.first_name,
        #             last_name=event.from_user.last_name,
        #             username=event.from_user.username,
        #         )
        #     )

        l10n: FluentLocalization = self.l10ns[locale or "en"]

        data["l10ns"] = self.l10ns
        data["l10n"] = l10n
        data["aiogd_i18n_format"] = l10n.format_value

        return await handler(event, data)
