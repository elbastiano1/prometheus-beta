import io
import pytest
from src.indented_logger import IndentedLogger

def test_basic_logging():
    """Test basic logging functionality."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream)
    logger.log("Hello, world!")
    assert stream.getvalue().strip() == "Hello, world!"

def test_indentation():
    """Test logging with increased indentation."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream)
    logger.log("First line")
    logger.indent()
    logger.log("Indented line")
    logger.indent()
    logger.log("More indented line")
    logger.dedent()
    logger.log("Back to previous indent")
    
    expected_output = """First line
    Indented line
        More indented line
    Back to previous indent"""
    
    assert stream.getvalue().strip() == expected_output.strip()

def test_multiple_indentations():
    """Test multiple indentation and dedentation."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream)
    logger.indent()
    logger.indent()
    logger.indent()
    logger.log("Triple indent")
    logger.dedent()
    logger.log("Double indent")
    
    expected_output = """            Triple indent
        Double indent"""
    
    assert stream.getvalue().strip() == expected_output.strip()

def test_prevent_negative_indent():
    """Ensure indentation doesn't go below zero."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream)
    logger.dedent()  # Should not cause negative indentation
    logger.log("No indent")
    
    assert stream.getvalue().strip() == "No indent"

def test_reset_indent():
    """Test resetting indentation to zero."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream)
    logger.indent()
    logger.indent()
    logger.log("Indented")
    logger.reset_indent()
    logger.log("Back to zero indent")
    
    expected_output = """        Indented
Back to zero indent"""
    
    assert stream.getvalue().strip() == expected_output.strip()

def test_custom_indent_char():
    """Test logging with a custom indent character."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream, indent_char='-', indent_width=2)
    logger.indent()
    logger.log("Custom indent")
    
    assert stream.getvalue().strip() == "--Custom indent"

def test_custom_indent_width():
    """Test logging with a custom indent width."""
    stream = io.StringIO()
    logger = IndentedLogger(output_stream=stream, indent_width=2)
    logger.indent()
    logger.log("Narrow indent")
    
    assert stream.getvalue().strip() == "Narrow indent"