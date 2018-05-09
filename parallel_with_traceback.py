#abbiamo una funzione (func) che usa come argomento 'loopante' il farm_id, ad esempio

#define your function.
def func(farm_id):
    ##Do whatever you want to do
    ##Se succede una certa condizione, vuoi uscire senza fare nulla

    if xxx:
        raise MissingTrainTestData('No statistical models available for farm '+str(farm_id))

##dove MissingTrainTestData e' una user defined exception
class MissingTrainTestData(Exception):
    """When a lack of data is present and you can't train/test the network"""
    pass

###A questo punto definisci una funzione di wrapping, diaframma tra il caso non parallel e il caso parallel che sappia gestire eccezioni varie e argomenti
def par_for_wrap(func, *args, **kwargs):
    """ wrapper for functions to deal with missing data when working in parrallel                                                                                                       
        and handle the traceback properly                                                                                                                                               
    func : is the function that you want to parrallise                                                                                                                                  
    args[0] : should be the farm_id (or the iterable) to allow error messages for                                                                                                       
    that specific farm/item """
    try:
        try:
            result = func(*args, **kwargs)
        except MissingTrainTestData as e:
            logger.warning(e.args[0])
            result = [None]
    except Exception, e:
        import traceback
        msg = "{}\n\nOriginal {}".format(e, traceback.format_exc()) + " ...for farm_id " + str(args[0])
        raise type(e)(msg)

    return result
    
######MAIN
pool_result = [pool.apply_async(par_for_wrap, args=(func, f_id) for f_id in farms.index]

rror_messages=[]
try:
    for i in pool_result:
        result = i.get()
        if result is not None:
            error_messages+=(result)
except Exception as outer_err:
    error_messages+=(outer_err)

if len(error_messages)==0:
    logger.info('**************************************** ')
    logger.info('*         Succesfully finished         * ')
    logger.info('**************************************** ')
else:
    logger.error(error_messages)
