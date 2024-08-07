from src.presentation.tgbot.handlers import user


def get_handlers() -> list:
    return [user.setup()]
