numerot = []
numero = 0

while numero != "":
        numero = str(input("Valitse numero: "))

        if numero != "":
            oikeaNumero = int(numero)
            numerot.append(oikeaNumero)
        else:
            break

numerot.sort(reverse=True)

if len(numerot) < 4:
    print("Virhe, ilmoita vähintään 5 lukua!")
else:
    for n in range(5):
        print(numerot[n])
