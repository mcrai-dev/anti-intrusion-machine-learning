def parse_chkrootkit(filepath):
    data = {}
    try:
        with open(filepath, 'r') as file:
            for line in file: 
                if "INFECTED" in line:
                    data['chkrootkit_infected'] = data.get('chkrootkit_infected', 0) + 1 
        if not data:
            print(f"Aucune donnée trouvée dans {filepath}.")
    except Exception as e:
        print(f"Erreur lors de la lecture de {filepath}: {e}")
    return data

def parse_lynis(filepath):
    data = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "Warning" in line:
                    data['lynis_warning'] = data.get('lynis_warning', 0) + 1
        if not data:
            print(f"Aucune donnée trouvée dans {filepath}.")
    except Exception as e:
        print(f"Erreur lors de la lecture de {filepath}: {e}")
    return data

def parse_rkhunter(filepath):
    data = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "Warning" in line:
                    data['rkhunter_warning'] = data.get('rkhunter_warning', 0) + 1 
        if not data:
            print(f"Aucune donnée trouvée dans {filepath}.")
    except Exception as e:
        print(f"Erreur lors de la lecture de {filepath}: {e}")
    return data
