
alkuluku = int(input("Mihin lukuun asti alkulukuja lasketaan? "))
alMäärä = 0
alkuluvut = []





def laskeAlkuluvut(m):
    for i in range(2, m // 2 + 1):

        if (alkuluku % i == 0):
            alkuluvut.append(i)

laskeAlkuluvut(alkuluku)

def yhteenLaske(n):
    vastaus = 0
    for m in n:
        vastaus = vastaus+m
    return vastaus

print(yhteenLaske(alkuluvut))