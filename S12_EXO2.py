try:
    with open("message.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print("Le fichier n'existe pas.")
  
