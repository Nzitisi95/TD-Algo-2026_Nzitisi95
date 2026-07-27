liste1 = input("Entrez des mots pour la première liste : ").split()
liste2 = input("Entrez des mots pour la seconde liste : ").split()

set1 = set(liste1)
set2 = set(liste2)
union_sets = set1.union(set2)

print(f"Tous les mots uniques combinés : {union_sets}")
