#NOTA: non ho capito bene la differenza tra apply e map
#This works fine if you work on a series df_DET['forecastdate']
df_DET['forecastdate']=df_DET['forecastdate'].map(lambda t: t.replace(hour=0))
#map e' molto piu' veloce di apply quindi secondo me map e' correttamente vettorializzato

##########Esempio 0
The apply method accepts a python function which should have a single parameter.
df["YourColumns"].apply(someFunction)

If you have more than 1 argument, use lambda function inside apply
my_series.apply((lambda x: your_func(a,b,c,d,...,x))) 

##########Esempio 1 (che ho messo in opera)
# cols e' una lista, percio' df[cols] e' un dataframe!
df['99th_percentile'] = df[cols].apply(lambda x: numpy.percentile(x, 99), axis=1)
#I'm assuming here that the variable 'cols' contains a list of the columns you want to include in the percentile 
#(You obviously can't use the Description in your calculation, for example).
#What this code does is loops over rows in the dataframe, and for each row, computes the numpy.percentile to get the 99th percentile. 
#You'll need to import numpy.


##########Esempio master: vuoi fare un'operazione complessa, x e' una serie/lista
def decision(x,model_params):
                keep_date=0
                if x[0] >model_params['min_odd_capacity']:
                    #to prevent taking decisions on few farms                                                                                                                           
                    if x[1] > model_params['min_odd_ratio']:
                        keep_date=1
                else:
                    #if the capacity of the farms where we know the odds is too small,                                                                                                  
                    #do not take any decision and discard nothing                                                                                                                       
                    keep_date=1
                return keep_date

df_keep=df_odd[['total_power','odd_ratio']].apply(lambda x : decision(x,model_params),axis=1).index


###########Esempio 2 (piu' complesso, ancora non lo capisco)
sum2=reduce(lambda x,y: x+y, map(lambda z,z*z, list))
# Questa e' l'idea per fare le somme in quadratura
# Ovviamente le parentesi, le virgole ecc, sono tutte sbagliate: questa e' solo l'idea
