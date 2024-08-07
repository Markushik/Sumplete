from functools import cache

from adaptix import Retort
from dynaconf import Dynaconf

from src.main.config.models import Config


@cache
def get_config() -> Config:
    dynaconf = Dynaconf(
        settings_file=[
            "settings/.secrets.toml",
            "settings/settings.toml",
        ],
        core_loaders=[
            "toml",
        ],
        validators=...,  # todo: write validators
        environments=True,
        lowercase_read=True,
    )
    retort: Retort = Retort()

    return retort.load(dynaconf, Config)
