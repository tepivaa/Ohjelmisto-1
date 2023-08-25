luoti = 13.3
naula = luoti*32
leivaska = naula*20

luotiMäärä = int(input("Kuinka monta luotia? "))
naulaMäärä = int(input("Kuinka monta luotia? "))
leivaskaMäärä = int(input("Kuinka monta luotia? "))

kokomääärä = luotiMäärä+naulaMäärä+leivaskaMäärä
kokomäääräG = (luotiMäärä*luoti)+(naulaMäärä*naula)+(leivaskaMäärä*leivaska)


kg= int(kokomäääräG/1000)
g = int(kokomäääräG-kg*1000)

print(f"Kilogrammoja on {kg} ja grammoja {g}")