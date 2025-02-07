# Données matrice
matrice = {(0,0): -1, (0,2): 3, (1,1): -2, (2,0): 4, (2,2): 5}

# a)
matrice_neg = {k: v for k, v in matrice.items() if v < 0}

print(matrice_neg)

# b)
lignes_non_nulles = {i for i, _ in matrice.keys()}

print(lignes_non_nulles)

# c)
positions_impaires = list(filter(lambda k: matrice[k] % 2 != 0, matrice.keys()))

print(positions_impaires)