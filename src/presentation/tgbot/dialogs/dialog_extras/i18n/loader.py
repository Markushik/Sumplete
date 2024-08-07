from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

from src.domain.constants import LocalesEnum, DEFAULT_LOCALE
from src.presentation.tgbot.middlewares import I18nMiddleware


def locales_loader() -> I18nMiddleware:
    loader = FluentResourceLoader(
        Path.cwd().parent.joinpath("locales", "{locale}").__str__(),
    )
    l10ns = {
        locale: FluentLocalization(
            locales=[locale],
            resource_ids=[
                "main.ftl",
            ],
            resource_loader=loader,
            use_isolating=False,
        )
        for locale in [item.value for item in LocalesEnum]
    }

    return I18nMiddleware(l10ns, DEFAULT_LOCALE)
