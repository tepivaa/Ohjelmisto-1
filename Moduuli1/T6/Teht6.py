import math


def pizza(halkaisija, hinta):

    pintaala = math.pi*(halkaisija/2)**2
    todellinenHinta = pintaala / hinta
    todellinenHinta = todellinenHinta / 10000

    return todellinenHinta

pizza1halkaisija = float(input("Mikä on ensimmäisen pizzan halkaisija? "))
pizza1hinta = float (input("Mikä on ensimmäisen pizzan hinta? "))

pizza2halkaisija = float(input("Mikä on toisen pizzan halkaisija? "))
pizza2hinta = float (input("Mikä on toisen pizzan hinta? "))

pizza1 = pizza(pizza1halkaisija, pizza1hinta)
pizza2 = pizza(pizza2halkaisija, pizza2hinta)

if pizza1 == pizza2:
    print("Pizzat ovat saman hintaisia!")

elif pizza1 < pizza2:
    print("Ensimmäinen pizza on halvempi! ")

else:
    print("Toinen pizza on halvempi! ")