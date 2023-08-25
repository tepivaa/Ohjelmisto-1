import random

heitot = int(input("Montako kertaa noppaa heitetään? "))
vastaus = 0

numerot = []

while heitot != 0:
    randomNumero = random.randint(1, 6)
    numerot.append(randomNumero)
    heitot = heitot-1

print(numerot)

for n in numerot:
    vastaus = vastaus+n

print(f"Noppien summa oli: {vastaus}")