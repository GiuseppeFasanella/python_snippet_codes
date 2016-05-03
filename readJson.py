#!/bin/env python

import json
json.encoder.FLOAT_REPR = lambda o: format(o, '.3f')

# -----------------------------------------------------------------------------------------------------------
def loadSettings():
    
	cf = open("pdfsct14_13TeV.json")
        cont = cf.read()
        settings = json.loads(cont)
        xsecs={} #dictionary
	#k is the "label", v is what is inside the label k. It happens that v is a dictionary
        for k,v in settings.iteritems():
		if(k=="ct14_0_13TeV"):
			for mass in sorted(v["001"].keys()):
				print k, mass, v["001"][mass] 
				   
        cf.close()
        

loadSettings()
