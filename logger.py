import os
import logging
from datetime import datetime

# Create the format
FORMAT = "%(asctime)-10s | %(levelname)-8s | %(lineno)-4d | %(module)-10s | %(message)s"


class Logger():

    def __init__(self, loglevel=20):
        """
        Description:
        Constructor for Logger

        Mandatory Args:
        None

        Optional Args:
        loglevel(int)   : 20 (default) - INFO
                          10 - DEBUG
                          30 - WARNING
                          40 - ERROR
                          50 - CRITICAL

        Use:
        >>> from logger import Logger ; log = Logger()
        """

        # Log level
        self.loglevel = loglevel

        # Initialize logger
        self.logger = logging.getLogger("root")

        # Log on console
        console_handler = logging.StreamHandler()

        # Set the format
        console_handler.setFormatter(logging.Formatter(fmt=FORMAT, datefmt='%m/%d/%y %H:%M:%S'))

        # Create handler
        self.logger.root.addHandler(console_handler)

        # Create the log directory if it does not exists
        if not os.path.exists("log/"):
            os.makedirs("log/")

    def log_to_file(self, name):
        """
        Description:
        File logger for printing on the conosle and the file

        Mandatory Args:
        name(str)       -       Name to be given to the log line

        Optional Args:
        None

        Use:
        >>> from logger import Logger ; log = Logger().log_to_file("A")
        """

        self.logger= logging.getLogger(name).getChild("root.module.{}".format(name))

        # Set level
        self.logger.setLevel(self.loglevel)

        # Create File name and Handler
        file_handle = logging.FileHandler("log/{}_{}.log".format(name, datetime.now().strftime('%b_%d_%y_%H_%M_%S')))

        # Set formatter for the file
        file_handle.setFormatter(logging.Formatter(fmt=FORMAT, datefmt='%m/%d/%y %H:%M:%S'))

        # Add the file handler
        self.logger.root.addHandler(file_handle)

        return self.logger
