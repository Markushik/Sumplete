from itertools import chain
from typing import Dict

from aiogram_dialog import DialogManager
from aiogram_dialog.api.internal import RawKeyboard
from aiogram_dialog.widgets.kbd import Group


class CustomGroup(Group):  # a temporary solution
    async def _render_keyboard(
        self,
        data: Dict,
        manager: DialogManager,
    ) -> RawKeyboard:
        self.width = int(manager.dialog_data.get("width"))
        self.width = self.width + 1
        kbd: RawKeyboard = []
        for b in self.buttons:
            b_kbd = await b.render_keyboard(data, manager)
            if self.width is None:
                kbd += b_kbd
            else:
                if not kbd:
                    kbd.append([])
                kbd[0].extend(chain.from_iterable(b_kbd))
        if self.width and kbd:
            kbd = self._wrap_kbd(kbd[0])
        return kbd
