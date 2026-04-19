"""
utils/logger.py
Centralized logger using loguru — import this in every module.
"""
from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - {message}",
    level="INFO",
    colorize=True,
)
logger.add(
    "logs/platform.log",
    rotation="10 MB",
    retention="7 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
)
