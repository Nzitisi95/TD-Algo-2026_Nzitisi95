try:
    a = float(input("Entrez le numérateur : "))
    b = float(input("Entrez le dénominateur : "))
    resultat = a / b
    print(f"Le résultat est : {resultat}")
except ZeroDivisionError:
    print("Erreur : Impossible de diviser par zéro !")
  
