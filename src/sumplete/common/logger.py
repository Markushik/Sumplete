import logging.config
from functools import cache


@cache
def configure_logger():  # todo output with rich
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "json": {
                    "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "format": """
                asctime: %(asctime)s
                created: %(created)f
                filename: %(filename)s
                funcName: %(funcName)s
                levelname: %(levelname)s
                levelno: %(levelno)s
                lineno: %(lineno)d
                message: %(message)s
                module: %(module)s
                msec: %(msecs)d
                name: %(name)s
                pathname: %(pathname)s
                process: %(process)d
                processName: %(processName)s
                relativeCreated: %(relativeCreated)d
                thread: %(thread)d
                threadName: %(threadName)s
                exc_info: %(exc_info)s
            """,
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "stderr": {
                    "class": "logging.StreamHandler",
                    "level": "WARNING",
                    "formatter": "json",
                    "stream": "ext://sys.stderr",
                },
                "stdout": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "json",
                    "stream": "ext://sys.stderr",
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "json",
                    "filename": "../../../../logs/bot.log",
                    "maxBytes": 10_485_760,
                    "backupCount": 3,
                },
            },
            "loggers": {
                "root": {"level": "DEBUG", "handlers": ["stdout", "file"]},
                "sqlalchemy.engine": {
                    "level": "INFO",
                    "handlers": ["stdout"],
                    "propagate": False,
                },
            },
        }
    )
