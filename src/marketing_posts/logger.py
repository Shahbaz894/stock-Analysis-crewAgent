import logging

def setup_logger(name: str):
    """Sets up a logger with specified logging configurations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create file handler for logging to a file
    file_handler = logging.FileHandler(f"{name}.log")
    file_handler.setLevel(logging.INFO)

    # Create console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add formatter to the handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
