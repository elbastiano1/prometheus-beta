import logging
import pytest
from src.multi_log import log_multiple_values

# Create a custom logger and handler to capture log messages
class LogCapture:
    def __init__(self):
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.logger.addHandler(self.handler)
        self.captured_logs = []

    def capture_logs(self):
        self.handler.stream.seek(0)
        self.captured_logs = self.handler.stream.read().strip().split('\n')
        return self.captured_logs

def test_log_multiple_values_default():
    log_capture = LogCapture()
    
    # Log multiple values with default settings
    log_multiple_values("Hello", 42, 3.14, logger=log_capture.logger)
    
    logs = log_capture.capture_logs()
    assert len(logs) == 1
    assert "Hello 42 3.14" in logs[0]
    assert "INFO" in logs[0]

def test_log_multiple_values_different_levels():
    log_capture = LogCapture()
    
    # Test different logging levels
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        log_multiple_values("Test", level, logger=log_capture.logger, level=level)
        logs = log_capture.capture_logs()
        assert len(logs) == 1
        assert "Test" in logs[0]
        assert level.upper() in logs[0]

def test_log_multiple_values_mixed_types():
    log_capture = LogCapture()
    
    # Test logging with mixed types
    log_multiple_values(1, "string", [1, 2, 3], {"key": "value"}, logger=log_capture.logger)
    
    logs = log_capture.capture_logs()
    assert len(logs) == 1
    assert "1 string [1, 2, 3] {'key': 'value'}" in logs[0]

def test_invalid_logging_level():
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multiple_values("Test", level="invalid")

def test_invalid_logger():
    with pytest.raises(TypeError, match="Logger must be an instance of logging.Logger"):
        log_multiple_values("Test", logger="not_a_logger")

def test_no_values():
    log_capture = LogCapture()
    
    # Logging no values should result in an empty string
    log_multiple_values(logger=log_capture.logger)
    
    logs = log_capture.capture_logs()
    assert len(logs) == 1
    assert "" in logs[0]