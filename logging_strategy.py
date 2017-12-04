###DUF WAY TO GO
#Nel main:
FConfig={
    'LOG_PATH' : '/home/gfasanella/workspace/Analysis/Farms_Evaluation_Giuseppe/Put_in_prod/',
    'send_mail_on_error' : 0,  
  }
import LogLib
logger = LogLib.Initiate(FConfig['LOG_PATH'], __file__, '_models', FConfig)


### in tutti gli altri file:
import logging
logger = logging.getLogger(__name__)


#############quick and dirty per 1 file solo (per usare MeteoDB ad esempio)
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

logger.info('writing some info')


