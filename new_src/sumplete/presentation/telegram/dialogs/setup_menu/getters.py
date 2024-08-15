from aiogram_dialog import DialogManager

from src.domain.entities.menu import COMPLEXITIES, Complexity, Size, SIZES


async def get_pincode_data(dialog_manager: DialogManager, **kwargs):
    return {"text": dialog_manager.dialog_data.get("puzzle_id", "")}


async def get_setups(dialog_manager: DialogManager, **kwargs):
    return {
        SIZES: [
            Size("3x3", "3×3"),
            Size("4x4", "4×4"),
            Size("5x5", "5×5"),
            Size("6x6", "6×6"),
        ],
        COMPLEXITIES: [
            Complexity("easy", "Easy"),
            Complexity("advanced", "Advanced"),
            Complexity("expert", "Expert"),
        ],
    }
