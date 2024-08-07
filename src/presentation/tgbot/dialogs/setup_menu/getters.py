from aiogram_dialog import DialogManager

from src.domain.entities.menu import Complexity, Dimension, SIZES, COMPLEXITIES


async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        SIZES: [
            Dimension('3x3_id', '3×3'),
            Dimension('4x4_id', '4×4'),
            Dimension('5x5_id', '5×5'),
            Dimension('6x6_id', '6×6')
        ],
        COMPLEXITIES: [
            Complexity('easy_id', 'Easy'),
            Complexity('advanced_id', 'Advanced'),
            Complexity('expert_id', 'Expert')
        ]
    }


async def get_pincode_data(dialog_manager: DialogManager, **kwargs):
    pincode = dialog_manager.current_context().dialog_data.get("pin", "")
    return {
        "text": pincode
    }
