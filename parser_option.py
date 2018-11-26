#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='my options parser')
parser.add_argument("-M","--Method", dest="Method") #python prog.py -M something ==> args.Method is now set to something                                              
parser.add_argument("-r","--doRatio",action="store_true") # python parser_option.py -r => options.doRatio is now true    
#Se invece vuoi poter settare una variabile true o false al run time, fai cosi'
import distutils.util
#python BDT_Model_predictor.py --roll=False (altrimenti args.roll is set to true)       
parser.add_argument("-r","--roll", dest='roll',default=True,type=distutils.util.strtobool) 
parser.add_argument("-p","--path",dest="path",default="",type="str") #python parser option.py -p "whatever" => options.path is "whatever"                             
parser.add_argument("-v","--verbose",dest="verbose",action="store_true")
parser.add_argument("-a","--append",dest="append",default="",help="Append string to filename")
parser.add_argument("","--sideband",dest="sideband",default=False,action="store_true")
parser.add_argument("","--addline",action="append",type="str",help="add lines to the plot file.root:color:linestyle:legend entry", default = [])
#pass a list 
parser.add_argument("-p","--point", dest='point',nargs='*', default=[0,1]) #'*' stands for 0 or more use 
##pass a 'datetime'
parser.add_argument("--train_st", default='',help="pass it as '20150101 00'")

    
#call it as
#python prog.py --point 1 8 9 9
#you'll have args.point as a list [1,8,9,9]


args = parser.parse_args()


####Examples###########                                                                                                                                               
if args.Method=="MaxLikelihoodFit":
    print "Do something!"

if args.doRatio:
    print "doRatio is true if you call parser_option.py -r"
