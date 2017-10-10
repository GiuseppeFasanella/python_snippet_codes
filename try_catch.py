Supponiamo che questa operazione:
df_input.loc[:,(met_model,model_params['variables'],slice(None))]
puo' dare un errore con messaggio 'KeyError'

Fai cosi':

try:
  df_input = df_input.loc[:,(met_model,model_params['variables'],slice(None))]
except KeyError as e:
  logger.warning(met_model+' not available : skipping it')
  continue
