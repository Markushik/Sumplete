from itertools import cycle

from adaptix import Retort
from aiogram_dialog import DialogManager
from attrs import asdict
from pendulum import now

from src.core.puzzle.generate import PuzzleGenerate, pack_to_field
from src.domain.dto.puzzle import PuzzleSetup

retort = Retort()


async def getter(dialog_manager: DialogManager, **kwargs):
    if dialog_manager.dialog_data.get("play"):
        cells = dialog_manager.dialog_data["fields"]["cells"]
        solved = dialog_manager.dialog_data["fields"]["solved"]
        unsolved = dialog_manager.dialog_data["fields"]["unsolved"]
        play = dialog_manager.dialog_data["play"]

        finder = dialog_manager.find("lst_grp")

        print(cells)
        print(solved)
        print(unsolved)


        return {
            "play": play,
            "width": dialog_manager.dialog_data["width"],
            "cells": cells,
            "time": dialog_manager.dialog_data["time"],
        }

    setup = PuzzleSetup(
        int(dialog_manager.start_data["size"]),
        dialog_manager.start_data["complexity"],
    )
    puzzle = PuzzleGenerate()
    generate = puzzle(setup)

    # setup = PuzzleSetup(4, "ADVANCED")  # maybe add style (emoji, format)
    # puzzle = PuzzleGenerate()

    fields = pack_to_field(
        style="EMOJI",
        size=generate.size,
        zeroed_array=generate.zeroed_array,
        modified_array=generate.modified_array,
        horizontal_sums=generate.horizontal_sums,
        vertical_sums=cycle(generate.vertical_sums),
    )

    play: bool = True
    width: int = dialog_manager.start_data["size"]
    size: int = dialog_manager.start_data["size"]
    complexity = dialog_manager.start_data["complexity"].title()
    time = now("Europe/Moscow").format("D MMMM Y, HH:mm", "en")

    dialog_manager.dialog_data["play"] = play
    dialog_manager.dialog_data["width"] = width
    dialog_manager.start_data["size"] = size
    dialog_manager.dialog_data["fields"] = asdict(fields)
    dialog_manager.dialog_data["time"] = time

    return {
        "play": play,
        "width": width,
        "cells": asdict(fields)["cells"],
        "generate": generate,
        "time": time,
        "size": size,
        "complexity": complexity,
        "clicks": 3,
    }
