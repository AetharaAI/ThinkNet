from loguru import logger
import sys

# Configure logger
logger.remove()
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add("brain_collective.log", rotation="5 MB")

def get_logger(name: str = "brain_collective"):
    """
    Provides a ready-to-use logger instance.
    """
    return logger.bind(name=name)
