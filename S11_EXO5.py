def calculer_moyenne(*notes):
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

print(f"Moyenne : {calculer_moyenne(12, 15, 18, 14)}")
