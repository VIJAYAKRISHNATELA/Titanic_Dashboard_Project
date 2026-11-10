import logging

from app.logging_config import setup_logging, LOG_FILE


def test_logging_creates_log_file():

    setup_logging()

    logger = logging.getLogger("test_logger")

    logger.info("Titanic logging test successful")

    assert LOG_FILE.exists()

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    assert "Titanic logging test successful" in content