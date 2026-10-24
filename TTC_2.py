
prixHT = float(input("entre le prix HT:"))
print(f"{prixHT}DH")

print("TVA est 20%")

TVA = prixHT * 0.20

TTC = prixHT + TVA
print(f"votre prix est: {TTC}DH")

