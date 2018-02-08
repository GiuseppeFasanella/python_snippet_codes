import random
import itertools

def get_all_random_pairs(input_list):
    # Generate all possible non-repeating pairs                                                                                                                                         
    pairs = list(itertools.combinations(input_list, 2))

    # Randomly shuffle these pairs                                                                                                                                                      
    random.shuffle(pairs)
    return pairs

def get_m_random_n_tuplets(input_list, n, m):
    # Generate all possible non-repeating ntuplets                                                                                                                                      
    n_tuplets = list(itertools.combinations(input_list, n))

    # Randomly grep m ntupltes                                                                                                                                                          
    return random.sample(n_tuplets, m)


#############################################################                                                                                                                           
numbers=[1,2,3,5,6]
print(random.sample(numbers, 3)) #give me three random numbers from the list                                                                                                            
print(get_all_random_pairs(numbers)) #give me all possible pairs (in random order)                                                                                                      
print(get_m_random_n_tuplets(numbers,2,5)) #give me 5 possible pairs                                                                                                                    

