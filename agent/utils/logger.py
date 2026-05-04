
# https://www.aemonge.com/articles/python/debug/logging.html
from loguru import logger as loguru_logger
import json

def safe(obj):
    """Recursively convert non-JSON-serializable objects."""
    if isinstance(obj, dict):
        return {k: safe(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [safe(v) for v in obj]
    if hasattr(obj, "__dict__"):
        return safe(obj.__dict__)
    return obj

def json_sink(message):
    r = message.record
    log = {
        "timestamp": r["time"].timestamp(),
        "level": r["level"].name,
        "message": r["message"],
        **r["extra"],
    }
    log = safe(log)
    with open("agent_debug.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")

loguru_logger.remove()
loguru_logger.add(json_sink, level="INFO")


class CustomLogger:

    def __init__(self):
        self.logger = loguru_logger

    def info(self, message: str, **context):
        self.logger.bind(**context).info(message)

    def trace(self, message: str, **context):
        self.logger.bind(**context).trace(message)

    def warning(self, message: str, **context):
        self.logger.bind(**context).warning(message)

    def error(self, message: str, **context):
        self.logger.bind(**context).error(message)


        