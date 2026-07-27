def saluer(nom, langue="fr"):
    if langue.lower() == "fr":
        return f"Bonjour, {nom} !"
    else:
        return f"Hello, {nom} !"

print(saluer("Alice"))
print(saluer("Bob", "en"))
