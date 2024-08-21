from aiogram_dialog import DialogManager
from attrs import define


@define(slots=True)
class Size:
    id: str
    size: str


@define(slots=True)
class Complexity:
    id: str
    complexity: str


async def get_presets(dialog_manager: DialogManager, **kwargs):
    return {
        "sizes": ["3×3", "4×4", "5×5", "6×6", "7×7"],
        "complexities": ["Easy", "Medium", "Advanced", "Expert", "Master"],
    }


async def get_menu(dialog_manager: DialogManager, **kwargs):
    return {
        "digits": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "puzzle_id": dialog_manager.dialog_data.get("puzzle_id", ""),
    }
