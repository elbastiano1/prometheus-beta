import pytest
import time
from src.process_progress_logger import ProcessProgressLogger


def test_basic_progress_logging():
    """Test basic progress logging functionality."""
    log_messages = []
    def capture_log(msg):
        log_messages.append(msg)
    
    with ProcessProgressLogger(10, update_interval=0, log_callback=capture_log) as logger:
        logger.update(3)
        # Explicitly check the last update
        assert log_messages[-1] == "Progress: 3/10 steps (30.00%)"
        logger.update(4)
    
    # Verify final completion
    assert log_messages[-1] == "Progress: 10/10 steps (100.00%)"


def test_invalid_total_steps():
    """Test initialization with invalid total steps."""
    with pytest.raises(ValueError, match="total_steps must be a positive integer"):
        ProcessProgressLogger(0)
    
    with pytest.raises(ValueError, match="total_steps must be a positive integer"):
        ProcessProgressLogger(-5)


def test_update_with_invalid_steps():
    """Test updating with invalid number of steps."""
    logger = ProcessProgressLogger(10)
    
    with pytest.raises(ValueError, match="Steps completed cannot be negative"):
        logger.update(-1)


def test_update_interval():
    """Test update interval functionality."""
    log_messages = []
    def capture_log(msg):
        log_messages.append(msg)
    
    logger = ProcessProgressLogger(5, update_interval=0.1, log_callback=capture_log)
    
    logger.update()  # First update should log
    time.sleep(0.05)
    logger.update()  # Should not log due to interval
    time.sleep(0.1)
    logger.update()  # Should log again
    
    assert len(log_messages) >= 2


def test_complete_method():
    """Test the complete method."""
    log_messages = []
    def capture_log(msg):
        log_messages.append(msg)
    
    logger = ProcessProgressLogger(5, log_callback=capture_log)
    logger.update(3)
    logger.complete()
    
    assert log_messages[-1] == "Progress: 5/5 steps (100.00%)"


def test_context_manager():
    """Test usage as a context manager."""
    log_messages = []
    def capture_log(msg):
        log_messages.append(msg)
    
    with ProcessProgressLogger(3, log_callback=capture_log) as logger:
        logger.update(2)
    
    assert log_messages[-2] == "Progress: 2/3 steps (66.67%)"
    assert log_messages[-1] == "Progress: 3/3 steps (100.00%)"


def test_over_update():
    """Test updating beyond total steps."""
    log_messages = []
    def capture_log(msg):
        log_messages.append(msg)
    
    logger = ProcessProgressLogger(5, log_callback=capture_log)
    logger.update(10)  # More than total steps
    
    assert log_messages[-1] == "Progress: 5/5 steps (100.00%)"