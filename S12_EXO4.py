with open("message.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
    nombre_lignes = len(lignes)
print(f"Le fichier contient {nombre_lignes} ligne(s).")

