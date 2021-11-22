a = 0
boodschappenlijst = []
boodschappenlijst2 = []
def ja():
    print("\nWat wilt u toevoegen op uw boodschappenlijst?")
    product = input(": ")
    hoeveelheid = input("Hoeveel wil er van dit product?\n: ")
    voegtoe = input("wilt u nog meer producten?\n: ")
    if voegtoe == 'ja':
        boodschappenlijst2 = (product, hoeveelheid)
        boodschappenlijst.append(boodschappenlijst2)
        ja()
    else:
        boodschappenlijst2 = (product,hoeveelheid )
        boodschappenlijst.append(boodschappenlijst2)
        print(boodschappenlijst)

ja()
        
        