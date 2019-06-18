## 1. Get all permutations of my_list = [1, 2, 3] 

from itertools import permutations 
my_list = [1,2,3]
perm = list(permutations(my_list))

#(1, 2, 3)
#(1, 3, 2)
#(2, 1, 3)
#(2, 3, 1)
#(3, 1, 2)
#(3, 2, 1)

## 1.2 permutation of length L
from itertools import permutations 
L=2
perm = list(permutations(my_list,L))

#(1, 2)
#(1, 3)
#(2, 1)
#(2, 3)
#(3, 1)
#(3, 2)

########### Combinations
## 1.3 Combinations without replacements
from itertools import combinations 
my_list = [1,2,3]

# Get all combinations of [1, 1, 3] 
# and length L
L=2
comb = list(combinations(my_list, L)) 

#(1,2)
#(1,3)
#(2,3)

## 1.3 Combinations without replacements
from itertools import combinations_with_replacement
my_list = [1,2,3]
L=2
comb = list(combinations_with_replacement(my_list, L)) 
print(comb)
from itertools import combinations_with_replacement
my_list = [1,2,3]
L=2
comb = list(combinations_with_replacement(my_list, L)) 
print(comb)
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

