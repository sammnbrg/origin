# Données météo journalières
météo_semaine = [(12, 25, 0), (15, 28, 10), (14, 27, 5), (13, 24, 15), (11, 22, 8), (10, 20, 20), (12, 23, 0)]

# a)
amplitude_thermique = lambda météo: météo[1] - météo[0]

# b)
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

amplitudes = {jours_semaine[i]: amplitude_thermique(météo_semaine[i]) for i in range(len(météo_semaine))}

print(amplitudes)

# c)
jours_pluie = [jours_semaine[i] for i in range(len(météo_semaine)) if météo_semaine[i][2] > 0]

print(jours_pluie)

# d)
jours_chauds = list(filter(lambda jour: météo_semaine[jours_semaine.index(jour)][1] > 25, jours_semaine))

print(jours_chauds)