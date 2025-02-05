# 1
def racines_communes(ensemble1,ensemble2):
    # Racines qui ne sont pas communes
    racines_non_communes = ensemble1 ^ ensemble2

    # Ensemble deux ensembles de racines
    racines_totales = ensemble1 | ensemble2

    # Racines paires communes aux deux ensembles
    racines_paires_communes = {racine for racine in ensemble1 & ensemble2 if racine % 2 == 0}

    return racines_non_communes, racines_totales, racines_paires_communes

# 2
# Données météo journalières
données_météo = [(12, 25, 0), (15, 28, 10), (14, 27, 5), (13, 24, 15), (11, 22, 8), (10, 20, 20), (12, 23, 0)]

# a
amplitude_thermique = lambda météo: météo[1] - météo[0]

