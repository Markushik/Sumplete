import logging

import winloop
from aiogram import Bot, Dispatcher

from sumplete.shared.di.setup import setup_dishka

logger = logging.getLogger(__name__)


async def main() -> None:
    # configure_logger()
    dishka = setup_dishka()

    bot = await dishka.get(Bot)
    disp = await dishka.get(Dispatcher)

    try:
        logger.info("Bot starting. . .")
        await disp.start_polling(bot)
    finally:
        await dishka.close()
        logger.info("Bot stopping. . .")


if __name__ == "__main__":
    try:
        winloop.run(main())
    except (KeyboardInterrupt, SystemExit):
        ...
