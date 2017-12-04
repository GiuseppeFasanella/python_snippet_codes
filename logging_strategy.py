import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

logger.info('writing some info')

############################DUF UTILS
Nel main:
import LogLib
logger = LogLib.Initiate(FConfig['LOG_PATH'], __file__, '_models', FConfig)


In tutti gli altri file:
import logging
logger = logging.getLogger(__name__)
