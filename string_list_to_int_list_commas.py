string='[5 1 2 3 7 8 6 4]'

def from_string_to_list(string):
    string = string.replace(' ', '')
    string = string.replace('[', '')
    string = string.replace(']', '')
    q_list=[0]*len(string) 
    for i in range(len(string)):
        q_list[i]=int(string[i])

    return q_list
    
    
q_list = [5,1,2,3......]
