import pickle

##Salva la lista                                                                                                                                                      
numbers = [1,2,3,4]
filename='numbers.list'
pickle.dump(numbers, open(filename,'wb'))


##Accedi alla lista salvata                                                                                                                                           
loaded_list = pickle.load(open(filename,'rb'))
print('printing the loaded list')
print(loaded_list)
