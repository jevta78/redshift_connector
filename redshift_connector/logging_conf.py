import logging
import time

__all__ = ("LOGGING_CONFIG",)


class UTCFormatter(logging.Formatter):
    converted = time.gmtime


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "()": UTCFormatter,
            "format": "%(asctime)sZ %(levelname)s %(message)s"
        },
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        }
    }

}
