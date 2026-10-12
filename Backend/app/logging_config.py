import json
import logging
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from flask.logging import default_handler


HANDLER_NAME = "app-json-stdout"
MAX_STACK_FRAMES = 20
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


class JsonFormatter(logging.Formatter):
    def format(self, record):
        timestamp = datetime.fromtimestamp(record.created, timezone.utc)
        timestamp = timestamp.isoformat(timespec="milliseconds")
        timestamp = timestamp.replace("+00:00", "Z")
        event = getattr(record, "event", None)
        if not isinstance(event, str):
            event = "application.log"

        entry = {
            "timestamp": timestamp,
            "level": record.levelname,
            "message": record.getMessage(),
            "service.name": "web",
            "event": event,
        }

        if record.exc_info and record.exc_info[0]:
            error_type, _, error_traceback = record.exc_info
            frames = list(traceback.walk_tb(error_traceback))
            stacktrace = []
            for frame, line in frames[-MAX_STACK_FRAMES:]:
                code = frame.f_code
                location = f"{Path(code.co_filename).name}:{line}"
                stacktrace.append(f"{location} in {code.co_name}")
            entry["error.type"] = error_type.__name__
            entry["error.stacktrace"] = "\n".join(stacktrace)

        return json.dumps(entry, ensure_ascii=False)


def configure_logging(app):
    level = app.config.get("LOG_LEVEL", "INFO")
    if isinstance(level, str):
        level = LOG_LEVELS.get(level.strip().upper())
    if not isinstance(level, int) or level not in LOG_LEVELS.values():
        raise ValueError(
            "LOG_LEVEL must be DEBUG, INFO, WARNING, ERROR or CRITICAL"
        )

    logger = app.logger
    for handler in list(logger.handlers):
        if handler is default_handler or handler.name == HANDLER_NAME:
            logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.set_name(HANDLER_NAME)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
