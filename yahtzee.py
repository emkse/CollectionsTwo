import random
i = 0
counter = {}
whatreroll = ("")
hasendedearly = False
allRollsc = {}
position1 = []
position2 = []
position3 = []
position4 = []
position5 = []
position6 = []
positiontoak = []
positionfoak = []
positionfh = []
positionss = []
positionls = []
positiony = []
positionc = []
extracounter = ""
yahtzeecounter = 0
extrayahtzeepoints = 0
endscore = 0



def makeDictionary():
    global i, allRolls
    for x in range(0,5):
        if allRolls[i] in allRollsc:
            allRollsc[allRolls[i]] += 1
            i = int(i) + 1
        else:
            allRollsc.update({allRolls[i] : 1})
            i = int(i) + 1
        if x == 5:
            return allRollsc



def rollTheDice():
    global whatreroll, hasendedearly
    print("Cijfers gerolled: "+ str(roll1) +", "+ str(roll2) +", "+ str(roll3) +", "+ str(roll4) + " en "+ str(roll5))
    print("Welke postities wilt u rollen? (Voorbeeld: 1, 2, 5) | 'Geen: Om niet meer te rollen' | 'Quit: Stoppen met spelen'")
    whatreroll = input("")
    if whatreroll.lower() == "geen":
        hasendedearly = True
        return False
    elif whatreroll.lower() == "quit":
        quit()
    else:
        rerollDice()

def rerollDice():
    global whatreroll, roll1, roll2, roll3, roll4, roll5
    if "1" in whatreroll:
        whatreroll = list(whatreroll)
        roll1 = random.choice(dice)
    if "2" in whatreroll:
        whatreroll = list(whatreroll)
        roll2 = random.choice(dice)
    if "3" in whatreroll:
        whatreroll = list(whatreroll)
        roll3 = random.choice(dice)
    if "4" in whatreroll:
        whatreroll = list(whatreroll)
        roll4 = random.choice(dice)
    if "5" in whatreroll:
        whatreroll = list(whatreroll)
        roll5 = random.choice(dice)
    whatreroll = str(whatreroll)
dice = [1,2,3,4,5,6]

print("Welkom bij het spel Yathzee!")
print("")

while True:
    i = 0
    counter = {}
    whatreroll = ("")
    allRollsc = {}
    hasendedearly = False
    roll1 = random.choice(dice)
    roll2 = random.choice(dice)
    roll3 = random.choice(dice)
    roll4 = random.choice(dice)
    roll5 = random.choice(dice)
    mag3ofakind = False
    mag4ofakind = False
    magchance = False
    magfullhouse = False
    maglargestraight = False
    magsmallstraight = False
    magyahtzee = False

    for x in range(0,2):
        canContinue = rollTheDice()
        if canContinue == False:
            break
        else:
            continue

    if hasendedearly == True:
        print("Je hebt de ronde beindigd, de cijfers die je over hebt zijn: "+ str(roll1) +", "+ str(roll2) +", "+ str(roll3) +", "+ str(roll4) + " en "+ str(roll5))
    else:
        print("Dat was de laatste rol, de cijfers die je over hebt zijn: "+ str(roll1) +", "+ str(roll2) +", "+ str(roll3) +", "+ str(roll4) + " en "+ str(roll5))
    
    allRolls = [roll1, roll2, roll3, roll4, roll5]
    print("Waar wil je de cijfers deze ronde zetten?")
    if 1 in allRolls and not position1:
        print("Zet "+ str(allRolls.count(1) * 1)  +" in het eerste vakje")
    elif not position1:
        print("Zet 0 in het eerste vakje")
    if 2 in allRolls and not position2:
        print("Zet "+ str(allRolls.count(2) * 2)  +" in het tweede vakje")
    elif not position2:
        print("Zet 0 in het tweede vakje")
    if 3 in allRolls and not position3:
        print("Zet "+ str(allRolls.count(3) * 3)  +" in het derde vakje")
    elif not position3:
        print("Zet 0 in het derde vakje")
    if 4 in allRolls and not position4:
        print("Zet "+ str(allRolls.count(4) * 4)  +" in het vierde vakje")
    elif not position4:
        print("Zet 0 in het vierde vakje")
    if 5 in allRolls and not position5:
        print("Zet "+ str(allRolls.count(5) * 5)  +" in het vijfde vakje")
    elif not position5:
        print("Zet 0 in het vijfde vakje")
    if 6 in allRolls and not position6:
        print("Zet "+ str(allRolls.count(6) * 6)  +" in het zesde vakje")
    elif not position6:
        print("Zet 0 in het zesde vakje")
    if allRollsc != "":
        makeDictionary()
    combined = roll1 + roll2 + roll3 + roll4 + roll5
    if 3 in allRollsc.values() and not positiontoak or 4 in allRollsc.values() and not positiontoak or 5 in allRollsc.values() and not positiontoak:
        print("Zet "+ str(combined) + " in het three of a kind vakje")
        mag3ofakind = True
    if 4 in allRollsc.values() and not positionfoak or 5 in allRollsc.values() and not positionfoak:
        print("Zet "+ str(combined) + " in het four of a kind vakje")
        mag4ofakind = True
    if 3 in allRollsc.values() and 2 in allRollsc.values() and not positionfh:
        print ("Zet 25 in het full house vakje")
        magfullhouse = True
    if 1 in allRolls and 2 in allRolls and 3 in allRolls and 4 in allRolls and not positionss or 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and not positionss or 3 in allRolls and 4 in allRolls and 5 in allRolls and 6 in allRolls and not positionss:
        print ("Zet 30 in het small straight vakje")
        magsmallstraight = True
    if 1 in allRolls and 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and not positionls or 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and 6 in allRolls and not positionls:
        print("Zet 40 in het large straight vakje")
        maglargestraight = True
    if 5 in allRollsc.values() and not positiony:
        print("Zet 50 in het yahtzee vakje")
        magyahtzee = True
    if 5 in allRollsc.values() and positiony:
        print("Krijg een extra yahtzee!")
        magyahtzee = True
    if not positionc:
        print("Zet "+ str(combined)+ " in het chance vakje")
        magchance = True

    while True:
        whatchoice = input("Vul de naam in van het vakje waar je een cijfer in wilt doen ")
        if whatchoice.lower() == "eerste" and not position1:
            position1.append(allRolls.count(1)* 1) 
            break
        elif whatchoice.lower() == "tweede" and not position2:
            position2.append(allRolls.count(2)* 2)
            break
        elif whatchoice.lower() == "derde" and not position3:
            position3.append(allRolls.count(3)* 3)
            break
        elif whatchoice.lower() == "vierde" and not position4:
            position4.append(allRolls.count(4)* 4)
            break
        elif whatchoice.lower() == "vijfde" and not position5:
            position5.append(allRolls.count(5)* 5)
            break
        elif whatchoice.lower() == "zesde" and not position6:
            position6.append(allRolls.count(6)* 6)
            break
        elif whatchoice.lower() == "three of a kind" and not positiontoak and mag3ofakind == True:
            positiontoak.append(combined)
            break
        elif whatchoice.lower() == "four of a kind" and not positionfoak and mag4ofakind == True:
            positionfoak.append(combined)
            break
        elif whatchoice.lower() == "full house" and not positionfh and magfullhouse == True:
            positionfh.append(25)
            break
        elif whatchoice.lower() == "small straight" and not positionss and magsmallstraight == True:
            positionss.append(30)
            break
        elif whatchoice.lower() == "large straight" and not positionls and maglargestraight == True:
            positionls.append(40)
            break
        elif whatchoice.lower() == "yahtzee" and magyahtzee == True:
            if not positiony:
                positiony.append(50)
                yahtzeecounter = int(yahtzeecounter) + 1
                break
            else:
                extracounter = str(extracounter) + "X "
                extrayahtzeepoints = int(extrayahtzeepoints) + 100
                print('Je hebt meer dan 1 yahtzee! Jou extra punten voor deze extra yahtzee worden op het einde bij je score geteld!')
                break
        elif whatchoice.lower() == "chance" and not positionc and magchance == True:
            positionc.append(combined)
            break
        else:
            print("oeps dat is niet een van de keuzes of je hebt dat vakje al gevult probeer het nog een keer")
            continue
    
    print("Lijst:")
    print("Een: "+str(position1))
    print("Twee: "+str(position2))
    print("Drie: "+str(position3))
    print("Vier: "+str(position4))
    print("Vijf: "+str(position5))
    print("Zes: "+str(position6))
    print("Three of a kind: "+str(positiontoak))
    print("Four of a kind: "+str(positionfoak))
    print("Full house: "+str(positionfh))
    print("Small straight: "+str(positionss))
    print("Large straight: "+str(positionls))
    print("Yahtzee: "+str(positiony))
    print("Chance: "+str(positionc))    
    if not extracounter:
        pass
    else:
        print("Hoeveelheid extra yahtzee's: "+ str(extracounter))

    
    if position1 and position2 and position3 and position4 and position5 and position6:
        if not positiontoak:
            positiontoak.append(0)
        if not positionfoak:
            positionfoak.append(0)
        if not positionfh:
            positionfh.append(0)
        if not positionss:
            positionss.append(0)
        if not positionls:
            positionls.append(0)
        if not positiony:
            positiony.append(0)
        if not positionc:
            positionc.append(0)
        
        first6combined = int(position1[0]) + int(position2[0]) + int(position3[0]) + int(position4[0]) + int(position5[0]) + int(position6[0])
        if first6combined > 63:
            endscore = int(endscore) + 35
        endscore = int(first6combined) + int(positiontoak[0]) + int(positionfoak[0]) + int(positionfh[0]) + int(positionss[0]) + int(positionls[0]) + int(positiony[0]) + int(positionc[0]) + int(extrayahtzeepoints)
        print("Dat was het einde van het spel! dit is je eindscore: ")
        print(str(endscore))
        quit()