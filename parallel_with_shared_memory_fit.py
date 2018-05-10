import itertools
import time
from multiprocessing import Process, Pipe
import pandas as pd
import time
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

#########                                                                                                                                                                               
huge_dict = pd.read_hdf('my_dataframe.hdf','table') #~roughly 1 GB                                                                                                                      
X = pd.concat([huge_dict,huge_dict,huge_dict,huge_dict],axis=0) #~roughly 4 GB                                                                                                          
y = X.iloc[:,1]
#y = np.sum(np.arange(0, X.shape[1]) * X, axis=1)                                                                                                                                       
print('global objects taken')

def main_func(X,y,i,pipe=None):
    print("worker ", i)
    y_pred = []
    #mdl = GradientBoostingRegressor(n_estimators=1)                                                                                                                                    
    mdl = MLPRegressor()
    mdl.fit(X,y)
    #y_pred = mdl.predict(X)                                                                                                                                                            
    time.sleep(100)
    if pipe:
        pipe.send(result)
    else:
        return y_pred

def run_normal_parallel(X,y):
    workers = []
    pipes = []
    for i in range(2):
        parent, child = Pipe()
        worker = Process(target=main_func, args=(X,y,i,child))
        pipes.append(parent)
        worker.start()

    result = []
    for pipe in pipes:
        result.extend(pipe.recv())
    for worker in workers:
        worker.terminate()
    print result

#### main part #####                                                                                                                                                                    
run_normal_parallel(X,y)
