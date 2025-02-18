import logging

class LogMaker:
    @staticmethod
    def log_gen():
        log_format = '%(asctime)s:%(levelname)s:%(message)s'
        log_dateformat = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(filename=".\\logs\\nopcommerce.log",format=log_format,datefmt=log_dateformat,force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger