import random

heitto = 0
vastaus = 0

heittomäärä = int(input("Kuinka monta sivuista noppaa käytetään? "))

def heitäNoppaa():
    heitto = random.randint(1, heittomäärä)
    return heitto


while (vastaus != heittomäärä):
    vastaus = heitäNoppaa()
    print(vastaus)