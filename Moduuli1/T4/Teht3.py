numerot = []
numero = 0

while numero != "":
    numero = input("Valitse numero: ")
    if (numero != ""):
        numerot.append(numero)

numerot.sort()

print("Pienin luku oli: "+ numerot[len(numerot)-1])
print("Suurin luku oli: "+ numerot[0])
