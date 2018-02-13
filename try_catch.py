Supponiamo che questa operazione:
df_input.loc[:,(met_model,model_params['variables'],slice(None))]
puo' dare un errore con messaggio 'KeyError'

Fai cosi':

try:
  df_input = df_input.loc[:,(met_model,model_params['variables'],slice(None))]
except KeyError as e:
  logger.warning(met_model+' not available : skipping it')
  continue

########## TRY-CATCH in PARALLEL ###################
#Tu hai un programma parallelizzato su tanti core
#In principio ogni thread puo' dare un suo errore diverso, di cui vuoi tener traccia.
#La versione semplice sarebbe
#try:                                                                                                                                                                                   
#    for i in pool_result:                                                                                                                                                              
#        result = i.get()                                                                                                                                                                                                                                                                                 
#except Exception as err:                                                                     
#    logger.error(err) ##Ma cosi' ogni errore ti manda una mail e fa spam

###per ogni thread catcha l'errore e nel caso appendilo in una lista di messaggi, inviati solo alla fine
error_messages=[]
try:
    for i in pool_result:                                                                                                                                                      
        try:
            result = i.get()
        except Exception as err:
            error_messages+=(err)
except Exception as outer_err:
    error_messages+=(outer_err)


if len(error_messages)==0:
    logger.info('**************************************** ')
    logger.info('*         Succesfully finished         * ')
    logger.info('**************************************** ')
else:
    logger.error(error_messages)

