from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

from new_src.sumplete.presentation.telegram.middlewares.i18n import I18nMiddleware


def locales_loader() -> I18nMiddleware:
    loader = FluentResourceLoader(
        str(Path.cwd().parent.joinpath("locales", "{locale}")),
    )
    # print(loader)
    l10ns = {
        locale: FluentLocalization(
            locales=[locale],
            resource_ids=[
                "main.ftl",
            ],
            resource_loader=loader,
            use_isolating=False,
        )
        for locale in [item for item in ["en", "ru"]]
    }
    # print(l10ns)
    # print(l10ns["en"].format_value('play-btn'))

    return I18nMiddleware(l10ns)
