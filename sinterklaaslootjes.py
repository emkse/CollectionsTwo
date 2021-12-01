import random

name = {}
Lootjes = []

while True:
    Names = input("Welke namen wilt u toevoegen\n")
    Lootjes.append(Names)
    Lootjes.sort()
    name[Names] = random.choices(Lootjes)
    feature = input("Wilt u meer namen toevoegen? (J/N) als je klaar bent type je (done)\n")
    if feature == 'N' or feature == 'N':
        print('De getrokken lootjes\n' + str(name))
        break
    elif feature == 'J' or feature == 'j':
        if len(Names) >= 0:
            print(name)
        else:   
            name[Names] = Lootjes
            print(name)