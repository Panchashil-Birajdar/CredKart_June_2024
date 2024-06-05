import logging

class   LoggingClass:
    @staticmethod
    def log_generator():
        logger = logging.getLogger()
        logfile = logging.FileHandler(".\\logs\\logfile.log")
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logfile.setLevel(logging.INFO)
        return logger

# debug
# Info
# Warnings
# error
# critical
