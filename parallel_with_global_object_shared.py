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
