with open("message.txt", "r", encoding="utf-8") as source, open("copie_message.txt", "w", encoding="utf-8") as cible:
    for ligne in source:
        cible.write(ligne)
print("La copie du fichier a été effectuée avec succès.")
