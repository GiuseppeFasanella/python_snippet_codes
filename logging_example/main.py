import mylib
from ph_logging_utils import get_logger
logger = get_logger(is_main=True,name="__main__")

logger.info('Hello baby')
mylib.foo()
bar = mylib.Bar()
bar.bar()





