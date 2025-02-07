# a)
moyenne_étudiant = lambda notes: sum(notes) / len(notes)

# b)
etudiants = [
    ('Alice', 18, (17, 15, 16)),
    ('Bob', 19, (12, 14, 11)),
    ('Charlie', 18, (15, 18, 14)),
    ('David', 20, (9, 11, 10))
]

moyennes = {nom: sum(notes) / len(notes) for nom, _, notes in etudiants}

print(moyennes)

# c)
etudiants_moyenne_math = list(filter(lambda etu: etu[2][0] >= 10, etudiants))

print(etudiants_moyenne_math)