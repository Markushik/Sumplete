from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Jinja

from src.sumplete.presentation.telegram.dialogs.ranking_menu.states import RankingMenu
from .getters import getter


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
            getter=getter,
            state=RankingMenu.RANKS,
        )
    )
