texte = input("Entrez un texte : ")
frequences = {}
for char in texte:
    if char in frequences:
        frequences[char] += 1
    else:
        frequences[char] = 1

print("Fréquence des caractères :")
for char, count in frequences.items():
    print(f"'{char}' : {count}")
  
