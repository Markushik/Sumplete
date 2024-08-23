from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from fluent.runtime import FluentLocalization

from sumplete.infrastructure.redis.adapter.implement import RedisAdapter


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

        l10n: FluentLocalization = self.l10ns.get(locale, "en")

        data["l10ns"] = self.l10ns
        data["l10n"] = l10n
        data["aiogd_i18n_format"] = l10n.format_value

        return await handler(event, data)
