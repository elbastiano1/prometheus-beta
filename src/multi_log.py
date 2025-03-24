import logging

def log_multiple_values(*values, level='info', logger=None):
    """
    Log multiple values in a single statement with flexible logging options.

    Args:
        *values: Variable number of values to log
        level (str, optional): Logging level. Defaults to 'info'.
            Supported levels: 'debug', 'info', 'warning', 'error', 'critical'
        logger (logging.Logger, optional): Custom logger. 
            If None, uses the root logger.

    Raises:
        ValueError: If an invalid logging level is provided
        TypeError: If logger is not a valid logging.Logger instance

    Returns:
        None
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Validate logger type
    if not isinstance(logger, logging.Logger):
        raise TypeError("Logger must be an instance of logging.Logger")

    # Normalize level to lowercase
    level = level.lower()

    # Map of supported logging levels
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    # Validate logging level
    if level not in log_levels:
        raise ValueError(f"Invalid logging level. Supported levels are: {', '.join(log_levels.keys())}")

    # Convert values to strings and join
    log_message = ' '.join(str(value) for value in values)

    # Log the message using the specified level
    log_levels[level](log_message)