# preTraining.py

def parse_chkrootkit(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if "INFECTED" in line:
                data['chkrootkit_infected'] = data.get('chkrootkit_infected', 0) + 1
            # Ajoutez plus de conditions de parsing selon les besoins
    return data

def parse_lynis(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if "Warning" in line:
                data['lynis_warning'] = data.get('lynis_warning', 0) + 1
            # Ajoutez plus de conditions de parsing selon les besoins
    return data

def parse_rkhunter(filepath):
    data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if "Warning" in line:
                data['rkhunter_warning'] = data.get('rkhunter_warning', 0) + 1
            # Ajoutez plus de conditions de parsing selon les besoins
    return data
