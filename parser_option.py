#!/usr/bin/env python

#parser.add_option("-short","--Long",dest="destination")
#default action is "store"
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-M","--Method",dest="Method") # python parser_option.py -M something => options.Method is now set to something
parser.add_option("-r","--doRatio",action="store_true") # python parser_option.py -r => options.doRatio is now true
parser.add_option("-p","--path",dest="path",default="",type="str") #python parser option.py -p "whatever" => options.path is "whatever"
parser.add_option("-v","--verbose",dest="verbose",action="store_true")
parser.add_option("-a","--append",dest="append",default="",help="Append string to filename")
parser.add_option("","--sideband",dest="sideband",default=False,action="store_true")
parser.add_option("","--addline",action="append",type="str",help="add lines to the plot file.root:color:linestyle:legend entry", default = [])


(options,args)=parser.parse_args()

# Standard Imports and calculators
import ROOT
import array,sys,numpy

####Examples###########
if options.Method=="MaxLikelihoodFit": 
    print "Do something!"

if options.doRatio:
    print "doRatio is true if you call parser_option.py -r"


print options.path+"/higgsCombineTest."+Method

for lineF in options.addline:

    # Parse the string, should be file.root:color:linestyle:legend entry    
    vals = lineF.split(":")
    ftmp = ROOT.TFile(vals[0])
    grext = ftmp.Get("observed")
    grext.SetLineColor(int(vals[1]))
    grext.SetLineStyle(int(vals[2]))
    grext.SetLineWidth(2)
    legend.AddEntry(grext,vals[3],"L")
    grext.Draw("same")


