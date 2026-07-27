contacts = {"Alice": "FR", "Bob": "BE", "Charlie": "FR", "David": "CA"}
inversé = {}

for nom, pays in contacts.items():
    if pays not in inversé:
        inversé[pays] = []
    inversé[pays].append(nom)

print("Dictionnaire inversé par pays :")
print(inversé)
