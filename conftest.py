# This conftest file is needed to write fixture that send loguru
# logs to logging library so caplog picks of logging

import logging
import pytest

# renaming caplog to _caplog to prevent nameing collision
from _pytest.logging import caplog as _caplog
from loguru import logger

@pytest.fixture
def caplog(_caplog):
    class PropagateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)
            
    handler_id = logger.add(PropagateHandler(), format="{message} {extra}")
    yield _caplog
    logger.remove(handler_id)
    