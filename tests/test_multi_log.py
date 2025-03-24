import logging
import pytest
from io import StringIO
from src.multi_log import log_multiple_values

# Create a custom logger and handler to capture log messages
class LogCapture:
    def __init__(self):
        # Create a StringIO to capture log output
        self.log_capture = StringIO()
        
        # Create a logger and handler
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        
        # Clear any existing handlers
        self.logger.handlers.clear()
        
        # Create a StreamHandler using StringIO
        self.handler = logging.StreamHandler(self.log_capture)
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def get_logs(self):
        # Get the log output and reset the StringIO
        log_contents = self.log_capture.getvalue().strip().split('\n')
        self.log_capture.seek(0)
        self.log_capture.truncate(0)
        return log_contents

def test_log_multiple_values_default():
    log_capture = LogCapture()
    
    # Log multiple values with default settings
    log_multiple_values("Hello", 42, 3.14, logger=log_capture.logger)
    
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "INFO: Hello 42 3.14" in logs[0]

def test_log_multiple_values_different_levels():
    log_capture = LogCapture()
    
    # Test different logging levels
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        log_capture = LogCapture()  # Create a new capture for each test
        log_multiple_values("Test", logger=log_capture.logger, level=level)
        
        logs = log_capture.get_logs()
        assert len(logs) == 1
        assert f"{level.upper()}: Test" in logs[0]

def test_log_multiple_values_mixed_types():
    log_capture = LogCapture()
    
    # Test logging with mixed types
    log_multiple_values(1, "string", [1, 2, 3], {"key": "value"}, logger=log_capture.logger)
    
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "INFO: 1 string [1, 2, 3] {'key': 'value'}" in logs[0]

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
    
    logs = log_capture.get_logs()
    assert len(logs) == 1
    assert "INFO: " in logs[0]