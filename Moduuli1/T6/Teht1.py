import random

heitto = 0
vastaus = 0
def heitäNoppaa():
    heitto = random.randint(1, 6)
    return heitto


while (vastaus != 6):
    vastaus = heitäNoppaa()
    print(vastaus)