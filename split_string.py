file="ILMIONOME.root"

name=file.split(".root")

print name[0] #--->ILMIONOME
print name[1] #--->.root
print name[-1] #---> Last element --> .root

se invece splittavi sul punto.
name=file.split(".")
name[0] #-->ILMIONOME
name[1] #--> root

