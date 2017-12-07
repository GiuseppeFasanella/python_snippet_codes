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

###case 1: function takes 1 argument
pool_result = [pool.apply_async(Looper, args=(farm,)) for farm in farms_ids]
for i in pool_result:
    result = i.get()

#func takes 2 arguments
pool_result = [pool.apply_async(func, args=(arg1, arg2)) for arg1 in args_loop_list]
for i in pool_result:
    result = i.get()
