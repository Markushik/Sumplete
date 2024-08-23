from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Jinja

from .getters import getter
from .handlers import on_main
from .states import RankingMenu
from ..extras.i18n.format import I18nFormat


def ranking_menu() -> Dialog:
    return Dialog(
        Window(
            Jinja(
                "<pre>"
                "{{ l10n.format_value('leaderboard-msg') }}:\n"
                "{% for rank in ranks %}"
                "{{ loop.index }}. | {{ '%-12s' | format(rank.user_id) }} | {{ '%-3s' | format(rank.score) }} points\n"
                "{% endfor %}"
                "</pre>"
            ),
            Button(
                I18nFormat("back-to-main-btn"),
                id="to_main",
                on_click=on_main,
            ),
            getter=getter,
            state=RankingMenu.RANKS,
        )
    )
