from __future__ import annotations

import logging
import os

import platformdirs

LOGGER_FORMAT = logging.Formatter("%(asctime)s - %(message)s")


class Logger:
    instances: dict[str, Logger] = {}

    def __new__(cls, logger_name: str) -> Logger:
        if logger_name not in cls.instances:
            cls.instances[logger_name] = super(Logger, cls).__new__(cls)
        return cls.instances[logger_name]

    def __init__(self, logger_name: str) -> None:
        self.logger_name = logger_name
        log_dir = platformdirs.user_log_dir("fastapi-template")
        os.makedirs(log_dir, exist_ok=True)

        self.logger_path = os.path.join(log_dir,
                                        f"{logger_name}.log")

        handler = logging.FileHandler(self.logger_path,
                                      encoding="utf-8")

        handler.setFormatter(LOGGER_FORMAT)
        self.logger = logging.getLogger(logger_name)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log info message

        Args:
            message (str): logging message
        """
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log warning message

        Args:
            message (str): logging message
        """
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log error message

        Args:
            message (str): logging message object
        """
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message, exc_info=True)