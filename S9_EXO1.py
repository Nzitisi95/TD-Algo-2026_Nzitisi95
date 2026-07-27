texte = input("Entrez un texte: ")
# Nettoyage
texte = texte.strip().lower().replace(".", "!")
print(f"Texte nettoyé : {texte}")
