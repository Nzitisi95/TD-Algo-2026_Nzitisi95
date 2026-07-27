annuaire = {
    "Alice": "0601020304",
    "Bob": "0655443322",
    "Charlie": "0699887766"
}
nom = input("Entrez le nom du contact à rechercher : ")
if nom in annuaire:
    print(f"Numéro de {nom} : {annuaire[nom]}")
else:
    print("Contact introuvable dans l'annuaire.")
  
