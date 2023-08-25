import math

vuosi = int(input("Mikä on vuosi? "))

vastaus = vuosi/4

if (vastaus.is_integer()):
    vastaus2 = vuosi/100
    if (vastaus2.is_integer()):
        vastaus3 = vuosi/400
        if (vastaus3.is_integer()):
            print("Kyseessä on karkausvuosi!")
        else:
            print("Kyseessä ei ole karkausvuosi!")
    else:
        print("Kyseessä on karkausvuosi!")
else:
    print("Kyseessä ei ole karkausvuosi!")



