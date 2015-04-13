file_mass=ROOT.TFile('root_path','READ')


#####WRITE A FILE##################
file_res_BB = open(str('path_'+path2),'w+')
hist   = file_mass.Get('h')
file_res_BB.write("%lf %lf\n"%(h.GetMean(),hist.GetRMS()))


#####READ A FILE###################
for regions in Regions:
    with open(str('path1_'+path2+'.txt')) as file_res:
        for line in file_res:  #Line is a string 
            # split the string on whitespace, return a list of numbers as strings
            numbers_str = line.split()  
            #convert numbers to floats                                                     
            numbers_float = map(float, line.split())
            ##numbers_float = [float(x) for x in numbers_str]  #map(float,numbers_str) works too
            mass[regions].append(numbers_float[0])

