from aiogram_dialog import DialogManager

from src.domain.entities.menu import COMPLEXITIES, Complexity, Size, SIZES


async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        SIZES: [
            Size("3x3_id", "3×3"),
            Size("4x4_id", "4×4"),
            Size("5x5_id", "5×5"),
            Size("6x6_id", "6×6"),
        ],
        COMPLEXITIES: [
            Complexity("easy_id", "Easy"),
            Complexity("advanced_id", "Advanced"),
            Complexity("expert_id", "Expert"),
        ],
    }


async def get_pincode_data(dialog_manager: DialogManager, **kwargs):
    pincode = dialog_manager.current_context().dialog_data.get("pin", "")
    return {"text": pincode}
