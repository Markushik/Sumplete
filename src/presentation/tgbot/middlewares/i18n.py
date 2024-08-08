from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from fluent.runtime import FluentLocalization

from src.infrastructure.redis.gateways.user import UserCacheGateway


class I18nMiddleware(BaseMiddleware):
    def __init__(
        self,
        l10ns: Dict[str, FluentLocalization],
        default_lang: str,
    ):
        super().__init__()
        self.l10ns = l10ns
        self.default_lang = default_lang

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
        cache: UserCacheGateway = await dishka.get(UserCacheGateway)

        language = await cache.get_lang(event.from_user.id)

        l10n: FluentLocalization = self.l10ns[language or "en_GB"]

        data["l10ns"] = self.l10ns
        data["l10n"] = l10n
        data["aiogd_i18n_format"] = l10n.format_value

        return await handler(event, data)
