nouvelle_ligne = input("Entrez le texte à ajouter : ")
with open("message.txt", "a", encoding="utf-8") as f:
    f.write("\n" + nouvelle_ligne)
print("Ligne ajoutée avec succès.")
