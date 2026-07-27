try:
    age = int(input("Entrez votre âge : "))
    if age < 0 or age > 120:
        raise ValueError("L'âge doit être compris entre 0 et 120 ans.")
    print(f"Âge valide enregistré : {age} ans.")
except ValueError as e:
    print(f"Erreur détectée : {e}")
  
