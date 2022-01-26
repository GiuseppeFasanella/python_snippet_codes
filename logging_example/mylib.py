from ph_logging_utils import get_logger
logger = get_logger(name="__mylib__")


def foo():
    logger.info('Hi, foo')

class Bar(object):
    def bar(self):
        logger.info('Hi, bar')