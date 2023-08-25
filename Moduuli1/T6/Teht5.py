alkuluku = int(input("Mihin lukuun asti alkulukuja lasketaan? "))
alMäärä = 0
alkuluvut = []


def laskeAlkuluvut(n):

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            alkuluvut.append(i)
    return alkuluvut


def poistaParittomat(lista):
    for i in lista:
        vastaus = i / 2

        if not vastaus.is_integer():
            alkuluvut.remove(i)


laskeAlkuluvut(alkuluku)

print(f"Ennen muutosta: {alkuluvut}")

poistaParittomat(alkuluvut)

print(f"Muutoksen jälkeen: {alkuluvut}")
