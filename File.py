file_mass=ROOT.TFile('root_path','READ')


#####WRITE A FILE##################
file_res_BB = open(str('path_'+path2),'w+')
hist   = file_mass.Get('h')
file_res_BB.write("%lf %lf\n"%(h.GetMean(),hist.GetRMS()))


#####READ A FILE###################
# Si aprono due casi: 
#1) E' un file di soli numeri e tutte le righe hanno la stessa struttura
#Esempio: [0] -> x [y] -> sempre
for regions in Regions:
    with open(str('path1_'+path2+'.txt')) as file_res:
        for line in file_res:  #Line is a string 
            # split the string on whitespace, return a list of numbers as strings
            numbers_str = line.split()  
            #convert numbers to floats                                                     
            numbers_float = map(float, line.split())
            ##numbers_float = [float(x) for x in numbers_str]  #map(float,numbers_str) works too
            mass[regions].append(numbers_float[0])
            

#2) E' un file di numeri e di stringhe, nel quale ogni riga ha un significato diverso
#Esempio: 
#constTerm EB 1
#constTerm EE 2
#scale EB 3
#scale EE 4
with open('test2.dat') as file_res:
    for line in file_res:  #Line is a string #split the string on whitespace, return a list                                                                                     
        numbers_str = line.split() #At this point everything is a string                                                                                                        
        #In base alla struttura del file, ti regoli.                                                                                                                            
        #In questo caso (test2.dat):                                                                                                                                            
        #[0] -> scale/constTerm                                                                                                                                                 
        #[1] -> barrel/endcap                                                                                                                                                   
        #[2] -> fit value                                                                                                                                                       
        if numbers_str[0] in ['constTerm'] and numbers_str[1] in ['EB']:
            result_constTerm_barrel=float(numbers_str[2])
        elif numbers_str[0] in ['constTerm'] and numbers_str[1] in ['EE']:
            result_constTerm_endcap=float(numbers_str[2])
        elif numbers_str[0] in ['scale'] and numbers_str[1] in ['EB']:
            result_scale_barrel=float(numbers_str[2])
        elif numbers_str[0] in ['scale'] and numbers_str[1] in ['EE']:
            result_scale_endcap=float(numbers_str[2])

print result_constTerm_barrel, result_constTerm_endcap, result_scale_barrel, result_scale_endcap


