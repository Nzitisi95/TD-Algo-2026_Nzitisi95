def min_max(liste):
    return (min(liste), max(liste))

nombres = [45, 12, 89, 3, 22]
mini, maxi = min_max(nombres)
print(f"Minimum : {mini}, Maximum : {maxi}")
