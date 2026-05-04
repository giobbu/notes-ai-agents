import json
from loguru import logger
import sys

def setup_logger(log_file="agent.log"):
    logger.remove()  # Remove default logger
    logger.add(sys.stdout, level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>")
    logger.add(log_file, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {extra} | {level} | {message}")
    return logger