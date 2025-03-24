import sys

class IndentedLogger:
    """
    A logger class that supports message logging with configurable indentation.
    
    This logger allows logging messages with variable indentation levels,
    providing flexibility in formatting log output.
    """
    
    def __init__(self, output_stream=sys.stdout, indent_char=' ', indent_width=4):
        """
        Initialize the IndentedLogger.
        
        Args:
            output_stream (file-like object, optional): Stream to write logs to. 
                                                        Defaults to sys.stdout.
            indent_char (str, optional): Character used for indentation. 
                                         Defaults to space.
            indent_width (int, optional): Number of indent characters per level. 
                                          Defaults to 4.
        """
        self._output_stream = output_stream
        self._indent_char = indent_char
        self._indent_width = indent_width
        self._current_indent = 0
    
    def log(self, message):
        """
        Log a message with the current indentation level.
        
        Args:
            message (str): The message to log.
        """
        indent = self._indent_char * (self._indent_width * self._current_indent)
        print(f"{indent}{message}", file=self._output_stream, flush=True)
    
    def indent(self):
        """
        Increase the indentation level by 1.
        
        Returns:
            IndentedLogger: The current logger instance, for method chaining.
        """
        self._current_indent += 1
        return self
    
    def dedent(self):
        """
        Decrease the indentation level by 1, ensuring it doesn't go below 0.
        
        Returns:
            IndentedLogger: The current logger instance, for method chaining.
        """
        self._current_indent = max(0, self._current_indent - 1)
        return self
    
    def reset_indent(self):
        """
        Reset the indentation level to 0.
        
        Returns:
            IndentedLogger: The current logger instance, for method chaining.
        """
        self._current_indent = 0
        return self