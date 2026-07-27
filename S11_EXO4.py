def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)

nombre = int(input("Entrez un nombre entier positif : "))
print(f"La factorielle de {nombre} est {factorielle(nombre)}")
