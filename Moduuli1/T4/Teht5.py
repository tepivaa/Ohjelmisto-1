käyttäjätunnus = "python"
salasana = "rules"
yritykset = 0



while (yritykset != 5):
    käyttis = input("Kirjoita käyttäjätunnuksesi: ")
    salis = input("Kirjoita salasanasi: ")
    if käyttis == käyttäjätunnus and salis == salasana:
        print(f"Tervetuloa {käyttis}!")
        break
    else:
        yritykset = yritykset+1
        print(str(5-yritykset) + " yritystä jäljellä!")

if (yritykset == 5):
    print("Käyttäjätili suljettu!")