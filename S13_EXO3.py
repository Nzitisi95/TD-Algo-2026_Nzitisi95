try:
    nombre = int(input("Entrez un nombre : "))
except ValueError:
    print("Saisie invalide.")
else:
    print(f"Saisie réussie : {nombre}")
finally:
    print("Fin du traitement de la saisie.")
  
