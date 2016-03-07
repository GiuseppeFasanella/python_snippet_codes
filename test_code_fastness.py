% python -mtimeit  "l=[]"
10000000 loops, best of 3: 0.0711 usec per loop

% python -mtimeit  "l=list()"
1000000 loops, best of 3: 0.297 usec per loop
