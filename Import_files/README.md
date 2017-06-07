```
Se hai una struttua in sottocartelle, e alcune librerie sono altrove rispetto 
alla cartella da dove lanci il codice, puoi fare cosi'

tu sei in una directory 
supponiamo esiste un python MeteoLib/MyFunctions.py
export PYTHONPATH=$PYTHONPATH:/home/gfasanella/workspace/MeteoLib

e nel codice puoi fare
import MyFunctions (anche se MyFunctions non e' nel path dove tu lanci il codice)

```
