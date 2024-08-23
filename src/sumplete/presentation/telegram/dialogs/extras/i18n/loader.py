from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

from ....middlewares.i18n import I18nMiddleware


def locales_loader() -> I18nMiddleware:
    path = Path.cwd().joinpath("locales", "{locale}")
    loader = FluentResourceLoader(str(path))

    l10ns = {
        locale: FluentLocalization(
            locales=[locale],
            resource_ids=["main.ftl"],
            resource_loader=loader,
            use_isolating=False,
        )
        for locale in [item for item in ("en", "ru")]
    }

    return I18nMiddleware(l10ns)
