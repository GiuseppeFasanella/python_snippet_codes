def from_string_to_list(string):
    string = string.replace(' ', ',')
    string = string.replace('[', '')
    string = string.replace(']', '')
    return list(map(int,string.split(',')))

a='[-1 -3 4 2]'
a=from_string_to_list(a)

