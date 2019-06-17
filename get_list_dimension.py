#Immagina di avere una N-dimesional list

list = [[1,2,3],
        [4,5,6],
        [7,8,9]]

#La domanda e' come fai a conoscerne le sue dimensioni.

#Versione 1: trasforma in array e usa .shape
import numpy as np

a=np.array(list)
a.shape

#Se pero', e mi e' gia' capitato in qualche interview, non riesci ad importare numpy, allora:
n_rows = len(list)
n_columns = len(list[0])
