try:
    valeur = int(input("Entrez un nombre entier : "))
    calcul = 100 / valeur
    print(f"100 divisé par {valeur} vaut {calcul}")
except ValueError:
    print("Erreur : Vous devez entrer un nombre entier valide.")
except ZeroDivisionError:
    print("Erreur : La division par zéro est interdite.")
  
