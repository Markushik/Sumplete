import structlog
import winloop
from aiogram import Bot, Dispatcher

from new_src.sumplete.common.di.setup import setup_dishka

logger = structlog.get_logger()


async def _main() -> None:
    # can't load locales? maybe u run how py module?
    dishka = setup_dishka()

    bot = await dishka.get(Bot)
    disp = await dishka.get(Dispatcher)

    await logger.ainfo("Bot starting. . .")

    try:
        await disp.start_polling(bot)
    finally:
        await logger.ainfo("Bot stopping. . .")
        await dishka.close()


if __name__ == "__main__":
    try:
        winloop.run(_main())
    except (KeyboardInterrupt, SystemExit):
        ...
