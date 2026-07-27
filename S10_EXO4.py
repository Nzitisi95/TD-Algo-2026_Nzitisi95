entree1 = input("Entrez des nombres (liste 1) : ")
entree2 = input("Entrez des nombres (liste 2) : ")

set1 = {int(x) for x in entree1.split()}
set2 = {int(x) for x in entree2.split()}

communs = set1.intersection(set2)
print(f"Éléments communs : {communs}")
