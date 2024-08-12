from adaptix import Retort
from aiogram_dialog import DialogManager
from attrs import asdict
from pendulum import now

from src.core.puzzle.packers import pack_to_field
from src.infrastructure.database.models import User
from src.infrastructure.database.uow.impl import UnitOfWork

retort = Retort()


async def getter(dialog_manager: DialogManager, **kwargs):
    if play := dialog_manager.dialog_data.get("play"):
        size = dialog_manager.start_data["size"]
        started_at = dialog_manager.dialog_data["started_at"]
        score = dialog_manager.dialog_data["score"]
        puzzle_id = dialog_manager.dialog_data["puzzle_id"]
        complexity = dialog_manager.dialog_data["complexity"]
        cells = dialog_manager.dialog_data["fields"]["cells"]
        solved = dialog_manager.dialog_data["fields"]["solved"]
        unsolved = dialog_manager.dialog_data["fields"]["unsolved"]

        finder = dialog_manager.find("lst_grp")

        local_solved: list = []
        local_unsolved: list = []

        for cell in cells:
            for unsolve in unsolved:
                if finder.find_for_item("toggle_play", cell["id"]).is_checked(unsolve):
                    local_unsolved.append(unsolve)
            for solve in solved:
                if finder.find_for_item("toggle_play", cell["id"]).is_checked(solve):
                    local_solved.append(solve)
        if not list(set(local_unsolved) & set(unsolved)):
            if sorted(local_solved) == sorted(solved):
                play = False

        return {
            "puzzle_id": puzzle_id,
            "complexity": complexity,
            "score": score,
            "started_at": started_at,
            "ended_at": "...",
            "size": size,
            "play": play,
            "width": dialog_manager.dialog_data["width"],
            "cells": cells,
        }

    action: dict = dialog_manager.start_data["action"]
    puzzle_id: int = dialog_manager.start_data["puzzle_id"]
    dishka = dialog_manager.middleware_data["dishka_container"]

    uow: UnitOfWork = await dishka.get(UnitOfWork)
    user: User = await uow.user.get(dialog_manager.event.from_user.id)

    fields = pack_to_field(
        style=user.style.upper(),
        size=action["size"],
        zeroed_array=action["zeroed_array"],
        modified_array=action["modified_array"],
        horizontal_sums=action["horizontal_sums"],
        vertical_sums=iter(action["vertical_sums"]),
    )

    play: bool = True
    width: int = action["size"]
    size: int = action["size"]
    score: int = action["score"]
    complexity: str = action["complexity"].title()
    started_at: str = now("Europe/Moscow").format("D MMMM Y, HH:mm", user.language[:2])

    dialog_manager.dialog_data["play"] = play
    dialog_manager.dialog_data["puzzle_id"] = puzzle_id
    dialog_manager.dialog_data["width"] = width
    dialog_manager.start_data["size"] = size
    dialog_manager.dialog_data["fields"] = asdict(fields)
    dialog_manager.dialog_data["started_at"] = started_at
    dialog_manager.dialog_data["score"] = score
    dialog_manager.dialog_data["complexity"] = complexity

    return {
        "puzzle_id": puzzle_id,
        "play": play,
        "width": width,
        "score": score,
        "cells": asdict(fields)["cells"],
        "action": action,
        "started_at": started_at,
        "ended_at": "...",
        "size": size,
        "complexity": complexity,
        "clicks": 3,
    }
