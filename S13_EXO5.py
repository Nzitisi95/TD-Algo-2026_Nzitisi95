while True:
    try:
        nombre = int(input("Veuillez entrer un entier valide : "))
        print(f"Merci ! Vous avez entré : {nombre}")
        break
    except ValueError:
        print("Erreur : Ce n'est pas un entier valide. Réessayez.")
      
