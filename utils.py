# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""This module is for utilities functions"""

import logging


def setup_logger():
    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the logging level (choose one from DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)

    # Create a formatter to define the log message format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler to log messages to a file
    file_handler = logging.FileHandler('log_file.log')
    file_handler.setLevel(logging.DEBUG)  # Set the logging level for the file handler
    file_handler.setFormatter(formatter)

    # Create a stream handler to log messages to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)  # Set the logging level for the stream handler
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
