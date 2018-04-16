Nota preliminare:

in ogni sottodirectory ci deve essere un file __init__.py
```
Se hai una struttua in sottocartelle, e molte librerie sono altrove rispetto 
alla cartella da dove lanci il codice, puoi fare cosi'

tu sei in una directory 
supponiamo esiste un python MeteoLib/MyFunctions.py
export PYTHONPATH=$PYTHONPATH:/home/gfasanella/workspace/MeteoLib

e nel codice puoi fare
import MyFunctions (anche se MyFunctions non e' nel path dove tu lanci il codice)

```

```
supponiamo ora invece che sta nella cartella parente a dove c'e' il main
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))                                                    
parentdir = os.path.dirname(currentdir)                                                                                                 
sys.path.insert(0,parentdir)   
E ora puoi fare
import file_che_si_trova_nella_parentdir
```

```
Supponiamo infine che la cartella da cui vuoi importare si trova molte posizioni sopra la cartella in cui sei
Senza perder tempo, aggiungi il path e via
import sys
sys.path.insert(0,'/home/gfasanella/workspace/Zonal_prod/')

import file_che_si_trova_in_Zonal_prod
print(sys.path)
```
