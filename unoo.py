import random
counter = 0
global completeddeck
completeddeck = []
playerhand = []
aihand = []
pile = []
currentlyplayable = []
canPlayYellow = False
canPlayRed = False
canPlayGreen = False
canPlayBlue = False
colors = ["blauw","rood","groen","geel"]
numsandspecs = ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"]
endofthegame = False
hasNumberOrSpecialCardToPlay = False
viercounter = 0
keuzecounter = 0
nextplayerskips = 0
didyoujustdraw = False
kleurendictionary = {
    "rood" : 0,
    "blauw" : 0,
    "groen" : 0,
    "geel" : 0
}

def showDevinfo ():
        print("the list of cards currently playable: "+ ", ".join(currentlyplayable))
        print("the pile in the middle of the table: "+ ", ".join(pile))
        print("your current hand: "+ ", ".join(playerhand))
        print("the enemy's current hand: " + ", ".join(aihand))

def generateCards(deck, cardtypes):
    for currentcard in deck:
        for currenttype in cardtypes:
            completeddeck.append(currentcard + " " + currenttype)
    random.shuffle(completeddeck)
    return [completeddeck]

def playerDraws():
    global nextcard, didyoujustdraw
    if not currentlyplayable:
        didyoujustdraw = True
        nextcard = completeddeck[0]
        del completeddeck[0]
        print("Je hebt geen kaarten om te spelen dus je pakt eentje van de stapel")
        for x in colors:
            if x in nextcard and x not in pile[-1]:
                print("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", die kan je niet spelen")
                playerhand.append(nextcard)
                nextcard = ""
        for x in colors:
            if x in nextcard and x in pile[-1]:
                while True:
                    immediatelyplay = input("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", je kan die kaart meteen spelen, wil je dat doen? ")
                    if immediatelyplay.lower() == "ja":
                        pile.append(nextcard)
                        nextcard = ""
                        print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                        break
                    elif immediatelyplay.lower() == "nee":
                        playerhand.append(nextcard)
                        nextcard = ""
                        print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                        break
                    elif immediatelyplay.lower() == "quit":
                        quit()
                    elif immediatelyplay.lower() == "show":
                        showDevinfo()
                        continue
                    else:
                        print("oeps, dat snapte ik niet. de correcte inputs zijn ja en nee")
                        continue

def aiDraws():
    pass

def aiTurn():
    global nextcard, endofthegame, aihand, aiSkips, nextplayerskips
    print("De hand van je vijand bestaat uit "+ str(len(aihand)) +" kaarten")
    if len(aihand) == 0:
        endofthegame = True
    if len(pile) != 1:
        if "+2" in pile[-1]:
            print("Je vijand moet 2 kaarten pakken door jou +2 kaart")
            for x in range(0,2):
                nextcard = completeddeck[0]
                del completeddeck[0]
                aihand.append(nextcard)
        elif nextplayerskips > 0:
            print("je vijand moest zijn beurt overslaan door jou sla-beurt-over/omkeer kaart")
            nextplayerskips = int(nextplayerskips) - 1
        elif "neem vier" in pile[-1]:
            print("Je vijand moet 4 kaarten pakken door jou neem vier kaart")
            for x in range(0,4):
                nextcard = completeddeck[0]
                del completeddeck[0]
                aihand.append(nextcard)
    for x in aihand:
        if "geel" in x:
            kleurendictionary["geel"] += 1
        elif "rood" in x:
            kleurendictionary["rood"] += 1
        elif "groen" in x:
            kleurendictionary["groen"] += 1
        elif "blauw" in x:
            kleurendictionary["blauw"] += 1
      
    max_key = max(kleurendictionary, key=kleurendictionary.get)
    


    if nextplayerskips == 0:
        aiChecksForAllColors()
        aicChecksForAllNumbersAndSpecialCards()
        if canPlayBlue == True or canPlayGreen == True or canPlayYellow == True or canPlayRed == True or hasNumberOrSpecialCardToPlay == True or "Keuzekaart" in pile[-1] or "neem vier" in pile[-1] or "neem vier" in playerhand or "Keuzekaart" in playerhand and not currentlyplayable:        
            pass
    elif nextplayerskips == 1:
        print("je vijand moest zijn beurt overslaan door jou sla-beurt-over/omkeer kaart")
        nextplayerskips = int(nextplayerskips) - 1

def playerTurn():
    global nextcard, endofthegame, nextplayerskips
    if not pile:
        nextcard = completeddeck[0]
        del completeddeck[0]
        pile.append(nextcard)
    if len(playerhand) == 0:
        endofthegame = True
    
    if nextplayerskips == 0 and endofthegame == False and len(pile) != 1:
        if "+2" in pile[-1]:
            print("je moest 2 kaarten pakken door de +2 kaart die je vijand heeft gespeeld")
            for x in range(0,2):
                nextcard = completeddeck[0]
                del completeddeck[0]
                playerhand.append(nextcard)
        elif "neem vier" in pile[-1]:
            print("je moet 4 kaarten pakken door de vijand's neem vier kaart")
            for x in range (0,4):
                nextcard = completeddeck[0]
                del completeddeck[0]
                playerhand.append(nextcard)

    if nextplayerskips == 0 and endofthegame == False:
        print("Het is jouw beurt, je kaarten zijn: "+ ", ".join(playerhand))

        print("De kaart die boven aan de stapel ligt is "+ pile[-1])
        checkForAllColors()
        if didyoujustdraw == False:
            checkForAllNumbersAndSpecialCards()
            if canPlayBlue == True or canPlayGreen == True or canPlayYellow == True or canPlayRed == True or hasNumberOrSpecialCardToPlay == True or "Keuzekaart" in pile[-1] or "neem vier" in pile[-1] or "neem vier" in playerhand or "Keuzekaart" in playerhand and currentlyplayable and didyoujustdraw == False:
                print("Je hebt kaarten die je kan spelen!")

                print("De speelbare kaarten zijn "+ ", ".join(currentlyplayable) +". Geef de positie aan van de kaart die je wilt spelen (geteld van links)")
                while True:
                    whattoplay = input("")
                    if whattoplay.isnumeric() == True and int(whattoplay) > 0 and int(whattoplay) <= len(currentlyplayable):
                        pile.append(currentlyplayable[int(whattoplay) - 1])
                        for x in playerhand:
                            if currentlyplayable[int(whattoplay) - 1] ==  x:
                                playerhand.remove(x)
                                break
                        print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                        if "Keuzekaart" in pile[-1]:
                            print("Je hebt zojuist een keuzekaart gespeeld, welke kleur wil je hebben?")
                            while True:
                                chooseColor = input("")
                                if "geel" in chooseColor or "groen" in chooseColor or "rood" in chooseColor or "blauw" in chooseColor:
                                    del pile[-1]
                                    pile.append("Keuzekaart "+ str(chooseColor))
                                    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                                    break
                        if "neem vier" in pile[-1]:
                            print("Je hebt zojuist een neem vier kaart gespeeld, je vijand moet 4 kaarten pakken maar jij mag ook de kleur kiezen, welke kleur wil je hebben?")
                            while True:
                                chooseColor = input("")
                                if "geel" in chooseColor or "groen" in chooseColor or "rood" in chooseColor or "blauw" in chooseColor:
                                    del pile[-1]
                                    pile.append("neem vier "+ str(chooseColor))
                                    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                                    break
                        break
                    elif whattoplay.lower() == "quit":
                        quit()
                    elif whattoplay.lower() == "show":
                        showDevinfo()
                        continue
                    else:
                        print("Vul een geldig nummer van de positie die u heeft")
                        continue
            print("Dat was het eidne van jouw beurt, het is nu de beurt van je vijand")
            print("")
    elif endofthegame == False:
        print("je moet je beurt overslaan door je vijand's sla-beurt-over/omkeer kaart")
        nextplayerskips = int(nextplayerskips) - 1

def aiChecksForBlue():
    global canPlayBlue
    if "blauw" in pile[-1]:
        for x in aihand:
            if "blauw" in x:
                currentlyplayable.append(x)
        if currentlyplayable:
            canPlayBlue = True

def aiChecksForRed():
    global canPlayRed
    if "rood" in pile[-1]:
        for x in aihand:
            if 'blauw' in x:
                currentlyplayable.append(x)
        if currentlyplayable:
            canPlayRed = True

def aiChecksForGreen():
    global canPlayGreen
    if "groen" in pile[-1]:
        for x in aihand:
            if "groen" in x:
                currentlyplayable.append(x)
        if currentlyplayable:
            canPlayGreen = True

def aiChecksForYellow():
    global canPlayYellow
    if "yellow" in pile[-1]:
        for x in aihand:
            if "groen" in x:
                currentlyplayable.append(x)
        if currentlyplayable:
            canPlayYellow = True

def checkForBlue():
    global canPlayBlue
    if "blauw" in pile[-1]:
        for x in playerhand:
            if  "blauw" in x:
                currentlyplayable.append(x)   
        if currentlyplayable:
            canPlayBlue = True
    
def checkForRed():
    global canPlayRed
    if "rood" in pile[-1]:
        for x in playerhand:
            if  "rood" in x:
                currentlyplayable.append(x)   
        if currentlyplayable:
            canPlayRed = True

def checkForYellow():
    global canPlayYellow
    if "geel" in pile[-1]:
        for x in playerhand:
            if  "geel" in x:
                currentlyplayable.append(x)   
        if currentlyplayable:
            canPlayYellow = True

def checkForGreen():
    global canPlayGreen
    if "groen" in pile[-1]:
        for x in playerhand:
            if  "groen" in x:
                currentlyplayable.append(x)   
        if currentlyplayable:
            canPlayGreen = True

def aicChecksForAllNumbersAndSpecialCards():
    global aihand, hasNumberOrSpecialCardToPlay, viercounter, keuzecounter
    for x in aihand:
        if "sla-beurt-over" in x and "sla-beurt-over" in pile[-1] or "+2" in x and "+2" in pile[-1] or "omkeer" in x and "omkeer" in pile[-1] or "1" in x and "1" in pile[-1] or "2" in x and "2" in pile[-1] or "3" in x and "3" in pile[-1] or "4" in x and "4" in pile[-1] or "5" in x and "5" in pile[-1] or "6" in x and "6" in pile[-1] or "7" in x and "7" in pile[-1] or "8" in x and "8" in pile[-1] or "8" in x and "8" in pile[-1] or "9" in x and "9" in pile[-1] or "0" in x and "0" in pile[-1]:
            currentlyplayable.append(x)
            hasNumberOrSpecialCardToPlay = True

def checkForAllNumbersAndSpecialCards():
    global playerhand, hasNumberOrSpecialCardToPlay, viercounter, keuzecounter
    for x in playerhand:
        if "sla-beurt-over" in x and "sla-beurt-over" in pile[-1] or "+2" in x and "+2" in pile[-1] or "omkeer" in x and "omkeer" in pile[-1] or "1" in x and "1" in pile[-1] or "2" in x and "2" in pile[-1] or "3" in x and "3" in pile[-1] or "4" in x and "4" in pile[-1] or "5" in x and "5" in pile[-1] or "6" in x and "6" in pile[-1] or "7" in x and "7" in pile[-1] or "8" in x and "8" in pile[-1] or "8" in x and "8" in pile[-1] or "9" in x and "9" in pile[-1] or "0" in x and "0" in pile[-1] or "Keuzekaart" in x or "neem vier" in x:
            currentlyplayable.append(x)
            hasNumberOrSpecialCardToPlay = True 
    

def aiChecksForAllColors():
    aiChecksForBlue()
    aiChecksForGreen()
    aiChecksForYellow()
    aiChecksForRed()
    if canPlayBlue == False and canPlayRed == False and canPlayGreen == False and canPlayYellow == False and hasNumberOrSpecialCardToPlay == False:
        playerDraws()
    
def checkForAllColors():
    checkForBlue()
    checkForGreen()
    checkForRed()
    checkForYellow()
    if "Keuzekaart" in pile[-1] and len(pile) == 1:
        print("De kaart op het begin van de stapel is een keuzekaart dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in colors:
                pile.append(choosecolor)
                currentlyplayable.append("Keuzekaart")
                break
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
        print(pile[-1])        
    elif "neem vier" in pile[-1] and len(pile) == 1:
        print("De kaart op het begin van de stapel is een neem vier dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in colors:
                pile.append(choosecolor)
                currentlyplayable.append("neem vier")
                break
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
                continue
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
    elif canPlayBlue == False and canPlayRed == False and canPlayGreen == False and canPlayYellow == False and hasNumberOrSpecialCardToPlay == False:
        playerDraws()


completedeck = generateCards({"geel", "groen", "rood","blauw"}, ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])
completedeck += generateCards({"geel", "groen", "rood","blauw"}, ["1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])

playerhand = (completeddeck[0:7])
aihand = (completeddeck[7:14])
del completeddeck[:14]
while True:
    playerTurn()
    canPlayBlue = False
    canPlayGreen = False
    canPlayYellow = False
    canPlayRed = False
    currentlyplayable = []
    hasNumberOrSpecialCardToPlay = False
    didyoujustdraw = False
    aiTurn()
    didyoujustdraw = False
    canPlayBlue = False
    canPlayGreen = False
    canPlayYellow = False
    canPlayRed = False
    currentlyplayable = []
    hasNumberOrSpecialCardToPlay = False
    if endofthegame == True:
        print("Dat is het einde van het spel!")
        quit()
        