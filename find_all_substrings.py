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
