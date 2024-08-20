from .user import setup


def get_handlers() -> list:
    return [setup()]
