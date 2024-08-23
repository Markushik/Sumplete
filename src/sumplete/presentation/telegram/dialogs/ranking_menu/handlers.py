from aiogram_dialog import DialogManager, StartMode

from ..main_menu.states import MainMenu


async def on_main(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)
