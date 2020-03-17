def load(file_name):
    file_data = []
    with open(file_name) as f:
        file_data = [line.rstrip('\n') for line in f]
    return file_data        

def getversion(the_list):
    for individual in the_list:
        if 'opam-version' in individual:
            version=individual.split('"')
            return version[1]

def getmaintainer(the_list):
    for individual in the_list:
        if 'maintainer' in individual:
            version=individual.split('"')
            return version[1]

def getsynopsis(the_list):
    for individual in the_list:
        if 'synopsis' in individual:
            version=individual.split('"')
            return version[1]
