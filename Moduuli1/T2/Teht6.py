import random

numero1 = str(random.randint(0, 9999))

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
n3 = random.randint(1, 6)

numero2 = str(n1)+str(n2)+str(n3)

print("Nelilukuinen koodi on: "+ numero1)
print("Kolmilukuinen koodi on: " + numero2)