#! /usr/bin/python                                                                                                                                                              

from classes import *
#This allows you to call your objects without typing classes.myObject                                                                                                           
#On the other hand it's considered bad practice                                                                                                                                 
print "this is my test"
obj=myObject(2,3)
print obj.n1
print obj.n2
print obj.sum

#Se il .py che vuoi importare si trova in un'altra sottocartella, devi fare questo barbatrucco
configfile = 'Closure_et_files/barrel_38T_scale.py'
import os
import sys
sys.path.append(os.path.dirname(os.path.expanduser(configfile)))
from barrel_38T_scale import *


#import classes                                                                                                                                                                 
#obj=classes.myObject(2,3)                                                                                                                                                      
#print obj.n1                                                                                                                                                                   
#print obj.n2                                                                                                                                                                   
#print obj.sum  
