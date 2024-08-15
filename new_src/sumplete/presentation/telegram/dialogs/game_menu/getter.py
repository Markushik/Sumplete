from adaptix import Retort
from aiogram_dialog import DialogManager
from pendulum import now

from new_src.sumplete.domain.game.usecase import check_intersection

retort = Retort()


def get_started_at(locale: str) -> str:  # todo: rewrite
    return now("Europe/Moscow").format("D MMMM Y, HH:mm", locale=locale)


async def getter(dialog_manager: DialogManager, **kwargs):
    if play := dialog_manager.dialog_data.get("play"):
        size = dialog_manager.dialog_data["size"]
        score = dialog_manager.dialog_data["score"]
        puzzle_id = dialog_manager.dialog_data["puzzle_id"]
        complexity = dialog_manager.dialog_data["complexity"]
        started_at = dialog_manager.dialog_data["started_at"]
        cells = dialog_manager.dialog_data["field"]["cells"]
        solved = dialog_manager.dialog_data["field"]["solved"]
        unsolved = dialog_manager.dialog_data["field"]["unsolved"]

        if check_intersection(
            cells=cells,
            solved=solved,
            unsolved=unsolved,
            finder=dialog_manager.find("lst_grp"),
        ):
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
    started_at = get_started_at(meta["locale"])

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
