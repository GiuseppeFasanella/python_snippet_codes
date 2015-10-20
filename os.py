import os
os.system("command")

#useful
for file in os.listdir("my_dir"):
    if file.endswith(".root"):
        filename.append(file)
        
profiles=['0','1']
for profile in profiles:
    #fai prima una stringa con tutti gli argomenti, poi la dai in pasto a system
    command_to_run = "./script/fit.sh "+str("/outProfile_"+profile)
    os.system(command_to_run)

