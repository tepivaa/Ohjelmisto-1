import random


numero = random.randint(1, 10)


print("Valitsin luvun 1-10 väliltä, mitä lukua ajattelen? ")
arvaus = int(input())
yritykset = 1

while arvaus != numero:
    yritykset = yritykset+1
    if arvaus < numero:
        print("Arvaus on liian pieni. ")
        arvaus = int(input())
    elif arvaus > numero:
        print("Arvaus on liian suuri. ")
        arvaus = int(input())

if (arvaus == numero):
    if (yritykset==0):
        print("Onneksi olkoon! Arvasit oikein ensimmäisellä yrityksellä! ")
    else:
        print(f"Onneksi olkoon! Arvasit oikein {yritykset} yrityksellä! ")