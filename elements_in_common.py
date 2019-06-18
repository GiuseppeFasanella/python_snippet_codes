##elements in common
list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]

inter = set(list1).intersection(list2)
print(inter)# set e' necessario perche': 'list' object has no attribute 'intersection'
inter = list(inter) #cast a lista

##Percio', mettendo tutto insieme in sintesi:
inter = list(set(list1).intersection(list2))

