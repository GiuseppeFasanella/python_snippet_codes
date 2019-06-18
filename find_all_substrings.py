## substrings sono definite come quelle sottostringhe ORDINATE che e' possibile ritagliare da una stringa piu' grande
## Ergo l'ordine delle lettere e' preservato 

def findAllSubstrings(s):
    substrings = {}
    for i in range(1, len(s) +1): #i is the substring length
        substrings[i] = []
    for i in range(0, len(s)): #Starting points
        for j in range(i, len(s)): #end points
            s_temp = s[i: j+1]
            substrings[len(s_temp)].append(s_temp)
            
    return substrings
    
s='abc'

### Trova tutte le ntuplette
def findAllNplets(arr,N):
    Nplets  = []
    for i in range(0, len(arr) - N + 1): #starting point
        j=i+N
        Nplets.append(arr[i:j])
    return Nplets


arr = [1, 2, 2, 4]

print(findAllNplets(arr,3))
Giuseppe Fasanella ran 24 lines of Python 3 (finished in 1.68s):

[[1, 2, 2], [2, 2, 4]]

>>> 

