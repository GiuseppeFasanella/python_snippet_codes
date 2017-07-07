import sys
import os #forse serve anche lui (not sure)

#E il gioco e' fatto
farm_ids = [sys.argv[1]] #qui e' in una lista, forse e' leggermente migliorabile, ma insomma

for farm_id in farm_ids:
  my_fuction(farm_id) #con ovviamente my_fucntion che qualcosa fa
  
  
#sostanzialmente e' un modo molto piu' agile per parsare gli argomenti "alla bash",
#senza specificare tutto come in parser_option.py

