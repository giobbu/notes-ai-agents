
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

def make_json_sink(filename="logs.jsonl"):
    def json_sink(message):
        r = message.record
        log = {
            "timestamp": r["time"].timestamp(),
            "level": r["level"].name,
            "message": r["message"],
            **r["extra"],
        }
        log = safe(log)
        with open(filename, mode="a", encoding="utf-8") as f:
            f.write(json.dumps(log, ensure_ascii=False) + "\n")
    return json_sink

class CustomLogger:
    
    def __init__(self, filename="logs.jsonl"):
        self.logger = loguru_logger
        self.logger.remove()
        self.logger.add(make_json_sink(filename), level="INFO")

    def info(self, message: str, **context):
        self.logger.bind(**context).info(message)

    def trace(self, message: str, **context):
        self.logger.bind(**context).trace(message)

    def warning(self, message: str, **context):
        self.logger.bind(**context).warning(message)

    def error(self, message: str, **context):
        self.logger.bind(**context).error(message)


        