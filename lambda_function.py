df['99th_percentile'] = df[cols].apply(lambda x: numpy.percentile(x, 99), axis=1)

#I'm assuming here that the variable 'cols' contains a list of the columns you want to include in the percentile 
#(You obviously can't use the Description in your calculation, for example).
#What this code does is loops over rows in the dataframe, and for each row, computes the numpy.percentile to get the 99th percentile. 
#You'll need to import numpy.

###########Esempio 2 (piu' complesso, ancora non lo capisco)
sum2=reduce(lambda x,y: x+y, map(lambda z,z*z, list))
# Questa e' l'idea per fare le somme in quadratura
# Ovviamente le parentesi, le virgole ecc, sono tutte sbagliate: questa e' solo l'idea
