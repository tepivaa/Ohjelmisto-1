
sukupuoli = str(input("Oletko mies vai nainen? "))

hemo = float(input("Mikä on hemoglobiiniarvosi? "))

if (sukupuoli == "mies" or sukupuoli == "Mies"):
    if (hemo > 134 and hemo < 195):
        print("Hemoglobiiniarvosi ovat normaalit.")
    else:
        print("Hemoglobiiniarvosi ovat huonossa kunnossa.")
elif (sukupuoli == "nainen" or sukupuoli == "Nainen"):
    if (hemo > 117 and hemo < 175):
        print("Hemoglobiiniarvosi ovat normaalit.")
    else:
        print("Hemoglobiiniarvosi ovat huonossa kunnossa.")
else:
    print("Virheellinen sukupuoli!")