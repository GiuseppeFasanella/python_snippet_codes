
# Python3 program to find  minimum number  
# of swaps required to sort an array 
Numero di swap = somma sui cicli di (taglia del ciclo -1)
taglia del ciclo = numero di nodi nel ciclo

Soluzione trovata qui:
https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


# Function returns the minimum  
# number of swaps required to sort the array 
def minSwaps(arr): 
    n = len(arr) 
      
    ##e.g arr = [1, 5, 4, 3, 2] 
    arrpos = [*enumerate(arr)] 
    ## arrpos=[(0, 1), (1, 5), (2, 4), (3, 3), (4, 2)]
      
    # Sort arrpos so that:
    # (position in arr, element)
    arrpos.sort(key = lambda it:it[1]) 
    # [(0, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
      
    # To keep track of visited elements.  
    # Initialize all elements as not  
    # visited or false. 
    vis = {k:False for k in range(n)} 
      
    # Initialize result 
    ans = 0 #ans stands for answer
    for i in range(n): 
          
        # already swapped or  
        # already present at  
        # correct position 
        if vis[i] or arrpos[i][0] == i: 
            continue
              
        # find number of nodes  
        # in this cycle and 
        # add it to ans 
        cycle_size = 0
        j = i 
        while not vis[j]: 
              
            # mark node as visited 
            vis[j] = True
              
            # move to next node 
            j = arrpos[j][0] 
            cycle_size += 1
              
        # update answer by adding 
        # current cycle 
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    # return answer 
    return ans 
  
# Driver Code      
arr = [1, 5, 4, 3, 2] 
print(minSwaps(arr)) 
