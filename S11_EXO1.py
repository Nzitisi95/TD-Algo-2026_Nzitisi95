def calculer_perimetre(longueur, largeur):
    return 2 * (longueur + largeur)

l = float(input("Entrez la longueur : "))
w = float(input("Entrez la largeur : "))
print(f"Le périmètre est : {calculer_perimetre(l, w)}")
