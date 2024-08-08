from adaptix import Retort
from aiogram_dialog import DialogManager
from attrs import asdict
from pendulum import now

from src.core.puzzle.generate import PuzzleGenerate
from src.domain.dto.puzzle import GameField, PuzzleSetup

retort = Retort()


async def getter(dialog_manager: DialogManager, **kwargs):
    if dialog_manager.dialog_data.get("play"):
        generate = retort.load(dialog_manager.dialog_data["generate"], GameField)
        cells = asdict(generate)["cells"]
        return {
            "width": dialog_manager.dialog_data["width"],
            "cells": cells,
            "time": dialog_manager.dialog_data["time"],
        }

    data = PuzzleSetup(
        True,
        int(dialog_manager.start_data["size"]),
        dialog_manager.start_data["complexity"],
    )
    puzzle = PuzzleGenerate()

    play: bool = True
    width: int = dialog_manager.start_data["size"]
    size: int = dialog_manager.start_data["size"]
    complexity = dialog_manager.start_data["complexity"].title()
    generate = puzzle(data)
    time = now("Europe/Moscow").format("D MMMM Y, HH:mm", "en")

    dialog_manager.dialog_data["play"] = play
    dialog_manager.dialog_data["width"] = width
    dialog_manager.start_data["size"] = size
    dialog_manager.dialog_data["generate"] = asdict(generate)
    dialog_manager.dialog_data["time"] = time

    print(generate.cells)
    print(asdict(generate)["cells"])

    return {
        "width": width,
        "cells": asdict(generate)["cells"],
        "generate": generate,
        "time": time,
        "size": size,
        "complexity": complexity,
        "clicks": 3,
    }
