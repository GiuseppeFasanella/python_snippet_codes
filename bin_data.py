import numpy

data = [0.1, 2.2, 3.4] #those are my data                                                                                                                                               
bin_edges = numpy.linspace(0, 10, 11) ##Those are my bin edges                                                                                                                          
bin_index = numpy.digitize(data, bin_edges) ##associate my data to a bin index                                                                                                          
                                            ##(integers), starting from 1                                                                                                               

##                                                                                                                                                                                      
#for i in range(0,len(data)): #i is the data index                                                                                                                                      
#    print(data[i], bin_index[i], bin_edges[bin_index[i]-1])                                                                                                                            

data_binned = [bin_edges[bin_index[i]-1] for i in range(0,len(data))]
print(data_binned)

