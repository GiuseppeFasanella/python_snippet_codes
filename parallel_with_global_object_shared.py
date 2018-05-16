### Qua la malattia e' questa: in python per parallelizzare puoi utilizzare multi_process o multithread
### Multithread sa utilizzare bene la memoria: nel senso che se esiste un oggetto globale, 
### tutti i workers lo hanno in comune e non se lo copiano. MA, per colpa del GIL (Global Interpreter Lock) 
### sara' usato un solo core (!)

### Multiprocess invece non usa bene la memoria: ogni worker si copia l'oggetto globale.
### Piu' cores vengono utilizzati, ma in memoria esistono N copie inutili di uno stesso oggetto globale
### Qui sotto riporto un modo, che mi pare funzionare, per sfruttare multiprocess con un oggetto grande e globale.

import itertools
import time
from multiprocessing import Process, Pipe
import pandas as pd
import time

huge_dict = pd.read_hdf('my_dataframe.hdf','table')
huge_dict = pd.concat([huge_dict,huge_dict,huge_dict,huge_dict],axis=0) #~roughly 4 GB                                                                                                  

def main_func(the_dict, pipe=None):
    result = []
    print('worker')
    time.sleep(100)
    if pipe:
        pipe.send(result)
    else:
        return result

def run_normal_parallel(huge_dict):
    workers = []
    pipes = []
    for i in range(4):
        parent, child = Pipe()
        worker = Process(target=main_func, args=(huge_dict, child))
        pipes.append(parent)
        worker.start()

    result = []
    for pipe in pipes:
        result.extend(pipe.recv())
    for worker in workers:
        worker.terminate()
    print result


run_normal_parallel(huge_dict)
## Then, to kill this wild beast here in shell
#kill -9 $(ps -ef | grep gfasane | grep python | grep name_of_main_program | awk '{print$2}')
