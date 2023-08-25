import random

N = int(input("Valitse likiarvon laskemisen pisteiden määrä: "))
fakeN = N
n = 0
x = 0
y = 0

while fakeN != 0:
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)
    if (x ** 2 + y ** 2 < 1):
        n = n+1
    fakeN = fakeN-1

pii = 4*n/N
print(f"Piin likiarvo on: {pii:0.6f}")