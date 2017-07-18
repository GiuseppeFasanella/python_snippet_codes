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
