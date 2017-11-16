#Allora hai un dizionario che usi sempre ed e' condiviso da piu' file per mille cose

Lo definisco una volta e per sempre in un file: zone_dictionary.py
def load():
    zone_dict={}
    zone_dict['ITA'] ={74 : 'ITA',
                       1 : 'NORD',
                       2 : 'CNORD',
                       3 : 'CSOUTH',
                       4 : 'SOUTH',
                       5 : 'SARD',
                       6 : 'SICI',
                       61 : 'FRA',
                       62 : 'GER',
                       206 : 'TENNET',
    }
    return zone_dict

#oh, a questo punto, ogni file che usa sto dizionario fara'

import zone_dictionary as zone_dictionary
zone_dict=zone_dictionary.load()

E hai il dizionario!
