note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))

moyenne = (note1 + note2 + note3) / 3

if moyenne >= 10:
    print(f"Moyenne : {moyenne:.2f} → Reçu(e)")
else:
    print(f"Moyenne : {moyenne:.2f} → Non reçu(e)")
