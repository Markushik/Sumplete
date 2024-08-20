import pendulum
from aiogram_dialog import DialogManager
from dishka.integrations.aiogram import FromDishka

from src.sumplete.adapters.database.schemas import Solve
from src.sumplete.adapters.database.uow.implement import UnitOfWork
from src.sumplete.common.di.extras import inject_getter


def check_intersection(
    cells: list[dict],
    solved: list[str],
    unsolved: list[str],
    finder,
) -> bool:
    matched_solved, matched_unsolved = set(), set()

    for cell in cells:
        cell_finder = finder.find_for_item("toggle_play", cell["id"])

        matched_unsolved.update(
            unsolve for unsolve in unsolved if cell_finder.is_checked(unsolve)
        )
        matched_solved.update(
            solve for solve in solved if cell_finder.is_checked(solve)
        )

    return not matched_unsolved and sorted(matched_solved) == sorted(solved)


def started_at_(locale: str) -> str:
    datetime = pendulum.now("Europe/Moscow")
    return datetime.format(fmt="D MMMM Y, HH:mm", locale=locale)


@inject_getter
async def getter(dialog_manager: DialogManager, uow: FromDishka[UnitOfWork], **kwargs):
    if play := dialog_manager.dialog_data.get("play"):
        size = dialog_manager.dialog_data["size"]
        score = dialog_manager.dialog_data["score"]
        puzzle_id = dialog_manager.dialog_data["puzzle_id"]
        complexity = dialog_manager.dialog_data["complexity"]
        started_at = dialog_manager.dialog_data["started_at"]
        cells = dialog_manager.dialog_data["field"]["cells"]
        solved = dialog_manager.dialog_data["field"]["solved"]
        unsolved = dialog_manager.dialog_data["field"]["unsolved"]

        finder = dialog_manager.find("lst_grp")

        if check_intersection(
            cells=cells,
            solved=solved,
            unsolved=unsolved,
            finder=finder,
        ):
            user_id = dialog_manager.event.from_user.id

            await uow.solve.add(Solve(user_id=user_id, puzzle_id=puzzle_id, size=size))
            await uow.commit()

            play = False

        return {
            "play": play,
            "size": size,
            "score": score,
            "puzzle_id": puzzle_id,
            "complexity": complexity,
            "started_at": started_at,
            "ended_at": "...",
            "clicks": "...",
            "cells": cells,
        }

    meta: dict = dialog_manager.start_data["meta"]
    field: dict = dialog_manager.start_data["field"]

    play = True
    size = meta["size"]
    width = meta["size"]
    score = meta["score"]
    puzzle_id = meta["puzzle_id"]
    complexity = meta["complexity"].title()
    started_at = started_at_(meta["locale"])

    dialog_manager.dialog_data["play"] = play
    dialog_manager.dialog_data["size"] = size
    dialog_manager.dialog_data["width"] = width
    dialog_manager.dialog_data["score"] = score
    dialog_manager.dialog_data["puzzle_id"] = puzzle_id
    dialog_manager.dialog_data["complexity"] = complexity
    dialog_manager.dialog_data["started_at"] = started_at
    dialog_manager.dialog_data["field"] = field

    return {
        "play": play,
        "size": size,
        "width": width,
        "score": score,
        "puzzle_id": puzzle_id,
        "complexity": complexity,
        "started_at": started_at,
        "ended_at": "...",
        "clicks": "...",
        "cells": field["cells"],
    }
