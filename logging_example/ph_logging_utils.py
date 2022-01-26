import logging.config
import os

def get_logger(filename="output.log",is_main=False,name="__main__"):
    filename=filename
    if is_main:
        logging.config.fileConfig("logging.ini",disable_existing_loggers=False)
    logger = logging.getLogger(name)
    if is_main:
        should_roll_over = os.path.isfile(filename)
        handler = logging.handlers.RotatingFileHandler(filename, mode='w') #, backupCount=5)
        if should_roll_over:  # log already exists, roll over!
            handler.doRollover()

    output_file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    output_file_handler.setFormatter(formatter)
    logger.addHandler(output_file_handler)
    return logger