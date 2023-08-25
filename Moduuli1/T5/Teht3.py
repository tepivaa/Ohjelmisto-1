yes = 0
alkuluku = int(input("Valitse jokin luku: "))

for i in range(2, alkuluku//2+1):
    print(i)
    if (alkuluku % i == 0):
        print(f"Numero ei ole alkuluku! (Se on jaollinen numerolla {i}!)")
        yes=yes+1


if yes < 1:
    print("Luku on alkuluku!")
elif yes == 0:
    print("Luku on alkuluku!")