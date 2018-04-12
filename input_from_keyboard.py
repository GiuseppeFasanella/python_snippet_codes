try:
  nation = sys.argv[1]
except IndexError:
  nation = raw_input("Nation is a mandatory argument....please insert it: ")

##Se non passi l'argomaneto, si ferma, aspetta che tu lo immetta da tastiera e poi presegue senza crashare
