
kevät = ("Tammikuu", "Helmikuu", "Maaliskuu")
kesä = ("Huhtikuu", "Toukokuu", "Kesäkuu")
syksy = ("Heinäkuu", "Elokuu", "Syyskuu")
talvi = ("Lokakuu", "Marraskuu", "Joulukuu")

kuukausi = int(input("Valitse jokin kuukauden numero: "))-1

if kuukausi >= 0 and kuukausi < 12:
    if kuukausi < 9:
        if kuukausi < 6:
            if kuukausi < 3:
                print("Kyseessä on kevät!")
            else:
                print("Kyseessä on kesä!")
        else:
            print("Kyseessä on syksy!")
    else:
        print("Kyseessä on talvi!")
else:
    print("Virheellinen luku!")