import sys

##supponiamo che bla.py sia nel path "M:/Dufenergy/Meteo/POWERANALYSIS/power_model/"
sys.path.append("M:/Dufenergy/Meteo/POWERANALYSIS/power_model/") 
from bla import bla bla

# Puoi anche salire di un livello cosi'
sys.path.append("..")
# E ora hai "visibili" tutti i .py della cartella parent

