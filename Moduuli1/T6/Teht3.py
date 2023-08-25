litra = 3.785
gallon = 0


def laskeMuutos(g):
    muutos = g*litra
    return muutos

while (gallon >= 0):
    gallon = int(input("Kuinka monta gallonaa sinulla on? "))
    litroissa = laskeMuutos(gallon)
    print(f"Se on {litroissa:0.1f} litroissa.")