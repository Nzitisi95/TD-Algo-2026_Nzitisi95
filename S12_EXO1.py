phrase = input("Entrez une phrase à enregistrer : ")
with open("message.txt", "w", encoding="utf-8") as f:
    f.write(phrase)
print("Le fichier a été enregistré avec succès.")
