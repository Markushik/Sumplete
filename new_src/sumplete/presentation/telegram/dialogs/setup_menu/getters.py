from aiogram_dialog import DialogManager

from new_src.sumplete.domain.setup.schemas import Size, Complexity


async def get_menu(dialog_manager: DialogManager, **kwargs):
    return {
        "digits": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            0,
        ],
        "puzzle_id": dialog_manager.dialog_data.get("puzzle_id", ""),
    }


async def get_setups(dialog_manager: DialogManager, **kwargs):
    return {
        "sizes": [
            Size("3x3", "3×3"),
            Size("4x4", "4×4"),
            Size("5x5", "5×5"),
            Size("6x6", "6×6"),
            Size("7x7", "7×7"),
        ],
        "complexities": [
            Complexity("easy", "Easy"),
            Complexity("advanced", "Advanced"),
            Complexity("expert", "Expert"),
        ],
    }
