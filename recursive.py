## Simple recursive solution: works but slow (fib(3) is computed many times)
def fib(n): # O(2^n)
    if n==1 or n==2:
        result =1
    else:
        result =fib(n-1) + fib(n-2)
    return result

## Dynamic Programming solution (do not mistake with memorized sol)
def fib_dp(n, memo): # O(n)
    if memo[n]!=None: #se non e' null, l'ho gia' calcolato!
        return memo[n]
    if n==1 or n==2:
        result =1
    else:
        result =fib(n-1) + fib(n-2)
    memo[n] = result
    return result

def fib_bottom_up(n): # O(n) as well
    if n==1 or n==2:
        return 1
    bottom_up = [None]*(n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        
    return bottom_up[n]
    
    
n=5 #Voglio l'n-mo numero della serie di fibonacci
memo = [None]*(n+1)
print(fib_dp(n, memo))
print(fib(n))
print(fib_bottom_up(n))
