import string
import random

kaarten = ['A (Harten)',"Harten 2","Harten 3", "Harten 4", 'Harten 5', "Harten 6", "Harten 7", "Harten 8", "Harten 9 ", "Harten 10", "Harten Boer", "Harten vrouw", "Harten Koning", 'A (klaver)',"klaver 2","klaver 3", "klaver 4", 'klaver 5', "klaver 6", "klaver 7", "klaver 8", "klaver 9 ", "klaver 10", "klaver Boer", "klaver vrouw", "klaver Koning",'A (Schoppen)',"Schoppen 2","Schoppen 3", "Schoppen 4", 'Schoppen 5', "Schoppen 6", "Schoppen 7", "Schoppen 8", "Schoppen 9 ", "Schoppen 10", "Schoppen Boer", "Schoppen vrouw", "Schoppen Koning",'A (ruiten)',"ruiten 2","ruiten 3", "ruiten 4", 'ruiten 5', "ruiten 6", "ruiten 7", "ruiten 8", "ruiten 9 ", "ruiten 10", "ruiten Boer", "ruiten vrouw", "ruiten Koning", "joker", "joker"]

print("kaart 1 = ", random.choice(kaarten))
print("kaart 2 = ", random.choice(kaarten))
print("kaart 3 = ", random.choice(kaarten))
print("kaart 4 = ", random.choice(kaarten))
print("kaart 5 = ", random.choice(kaarten))
print("kaart 6 = ", random.choice(kaarten))
print("kaart 7 = ", random.choice(kaarten))
print(" deck (47 kaarten): ", kaarten)