###############################
#Esempio master: hai uno script molto bello che chiami con python prog.py --id 678
#Ora di id ce ne sono parecchio --> parallelizza cosi'
import os
from multiprocessing import Pool

def Looper(farm_id):
    print farm_id
    os.system('python BDT_Model_predictor.py -o farms_check --create --id '+str(farm_id))

farms_ids=[247, 374, 546, 606, 626, 666, 667, 686, 740, 741, 742, 743, 744, 1044, 1045, 1147, 1186, 1187, 1252, 1254, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366,\
 1367] #1226                                                                                                                                                          

pool = Pool(processes=2)
pool_result = [pool.apply_async(Looper, args=(farm,)) for farm in farms_ids]
for i in pool_result:
    result = i.get()
##################################

from multiprocessing import Pool

def func(arg1, arg2):
    print arg1 + arg2
    return arg1 + arg2

args_loop_list=[1,2]
# Only create pool once                                                                                                                                               
pool = Pool(processes=2)

#func takes 2 arguments
pool_result = [pool.apply_async(func, args=(arg1, 2)) for arg1 in args_loop_list]

#func takes 1 argument: se non scrivi args=(arg1,) non capira' mai
pool_result = [pool.apply_async(func, args=(arg1,)) for arg1 in args_loop_list]

for i in pool_result:
    result = i.get()
