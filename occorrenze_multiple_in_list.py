## Trova le occorrenze multiple in una lista
my_list = ['a','b','c', 'a', 'a', 'c']

unique_el = list(set(my_list))
occurrences = {}
for key in unique_el:
    occurrences[key]=0
    
for el in my_list:
    occurrences[el]+=1
    
    
###
print(occurrences)

Giuseppe Fasanella ran 18 lines of Python 3 (finished in 2.04s):

{'a': 3, 'c': 2, 'b': 1}
