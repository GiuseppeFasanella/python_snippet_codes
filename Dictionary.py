# Those things are REALLY useful, actually I think they are THE reason why I learned python

# I see two conceptual things:
# 1) objects depending on 1 (or more) variable(s)
variables=['pt1_reco','pt2_reco']
hist={} # hist ora dipende da una variable
for variable in variables:
  hist[variable]=ROOT.TH1F(....)
  
# Vuoi che gli istogrammi dipendano da 2 variabili fai cosi'
hist={} # A questo punto dipende da 1 variabile
for variable in variables:
  hist[variable]={} # Ora dipende da 2 variabili
# E a questo punto puoi fare una cosa tipo
hist[variable][detector_region]=ROOT.TH1F(...)

# 2) Se invece vuoi associare piu' informazioni sotto un'unica "etichetta" allora io faccio cosi'
# Io la vedo come una mappa a una chiave "0_10" e piu' valori: ptmin, ptmax, 
# poi ci puoi mettere il binning, le opzioni di drawing. E insomma... e' potente
region={}
region['0_10']=dict(name='ptEE0_10',ptmin=0.,ptmax=10.) # La regione 0_10 e' definita da un ptmin=0 e un ptmax=10
region['10_20']=dict(name='ptEE10_20',ptmin=10.,ptmax=20.)

# A un certo punto ti serve sapere il ptmin associato alla region['0_10']
region['0_10']['ptmin']
