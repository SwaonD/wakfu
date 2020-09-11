aptPdv = int(input("Points d'intellingence en '% Points de vie' : "))
aptRes = int(input("Points d'intelligence en 'Resistance Elementaire' : "))
totalRes = float(input("Resistance elementaire : "))
totalPdv = int(input("Points de vie : "))

# Calcul des PDV de base (sans l'intelligence)
basePdv = totalPdv/(1 + (aptPdv*4/100))

# Enlever 10 points d'intelligence, priorite a la resi
x = 10 - aptRes
aptPdv -= x
begintest = 0

# Pour savoir si le test est fait avec moins de 10 points d'intelligence
if aptPdv < 0 :
    begintest =  aptPdv * (-1)
    aptPdv = 0
totalRes -= aptRes * 10

# Boucle pour tester les differentes combinaisons entre les points d'intelligence en vie et en resi
i = 0
pdvPoint = 10 - begintest
resPoint = 0
while i <= 10 - begintest:
    pourcentRes = int((1-0.8**((totalRes + resPoint * 10)/100)) * 100)
    PDV = basePdv * (1 + ((aptPdv + pdvPoint)*4/100))
    REALPDV = PDV/((100 - pourcentRes)/100)
    print("\nPDV", PDV, sep=" : ")
    print("\nRES(%)", pourcentRes, sep=" : ")
    print("\nREALPDV",REALPDV, sep=" : ")
    print("\npdvPoint", pdvPoint, sep=" : ")
    print("\nresPoint", resPoint, sep=" : ")
    print("\n-------------------------------")
    pdvPoint -= 1
    resPoint += 1
    i += 1
