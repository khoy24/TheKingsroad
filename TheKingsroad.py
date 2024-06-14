#Kaitlyn Hoyme   12-9-2022
#Assignment 7    

#The game functions similarly to an oregon trail type game, but themed around game of thrones. You create a
#team of 4 people and try to survive the 8 day long journey. There are functions that have chances of being 
#applied and killing members of the team. I used a lot of random.randint() for this. There is also a shop 
#function that you can buy supplies at to help you along your journey. If at least one character makes it 
#to the end, you win. I also added another file that when called prints a map of Westeros (the road they travel).
#Team members can be killed instantly, or can starve. Depending on the choices you make at the beginning you will
#have certain abilities that will change your gameplay experience and help you survive. 
#I used dictionaries to keep track of the characters stats as they change throughout the game. The day function runs 
#8 times for how many days there are, and inside of that is where all of the functions that have randomized chances of 
#effecting your team are called. 

import random 
import pyTextColor

pytext = pyTextColor.pyTextColor()  # Create an object of the pyTextColor class
# Format the text with the color/bgcolor of your choice

def houseChoice():
        print("Your team must represent one of the famous houses of Westeros")
        choice1 = input("[c]hoose house or [l]earn advantages of the houses: ") 
        house = False
        while house == False: 
            if choice1 == "C" or choice1 == "c":
                print("Which house would you like to choose")
                housechoice = input("[S]tark, [L]annister, [B]aratheon, [T]argaryen: ")
                if housechoice == "S" or housechoice =="s":
                    house = "Stark"
                elif housechoice == "L" or housechoice == "l":
                    house = "Lannister"
                elif housechoice == "B" or housechoice == "b":
                    house = "Baratheon"   
                elif housechoice == "T" or housechoice == "t":
                    house = "Targaryen"
                else: 
                    print("Invalid input. Try again.")
                    
            elif choice1 == "l" or choice1 == "L": 
                print("The advantages and disadvantages to these houses are as follows: ")
                print("HOUSE LANNISTER")
                print("A lannister always pays their debts...")
                print("Greater starting amount of 350 silver coins, allowing you to purchase more supplies and services")
                print("")
                print("HOUSE STARK")
                print("A greater sense of loyalty and honor amongst your team. In the event of an unexpected death, allows one team member to sacrifice themselves and save the otherwise effected player.")
                print("(can be useful if your strongest teammate is suddenly killed, and you would rather have another die in their place)")
                print("")
                print("HOUSE BARATHEON")
                print("Your house is known for strength. Each players HP increases by 5 points immediately.")
                print("")
                print("HOUSE TARGARYEN")
                print("\"Fire cannot kill a dragon.\" Exactly what it sounds like.")
                print("")
                choice1 = "C"
                continue
            else: 
                print("Invalid input. Try again.")
                choice1 = input("[c]hoose house or [l]earn advantages of the houses: ") 
                continue
        return house
#need to have it stop when startingmoney hits 0
#how do i stop them buying horses

def shop(startingmoney, horses, foodAmount, clothingamount, spareparts, food, clothes, spares): #if want to use in future could just use currentmoney as startingmoney by calling it with the currentmoney as an argument, but would have to change location of varaible initializes (like horses = 0)
    print("")
    print("Welcome to the shop! Before you continue on your journey you must purchase the supplies necessary to survive.")
    print("Choose carefully, you never know when you'll have another opportunity to get supplies, and winter is coming.")
    print("")
    print("You have", startingmoney, "silver coins to spend.")
    print("What would you like to purchase?")
    replay = True
    # horses = 0
    while replay == True and startingmoney > 0:
        x = input(" [H]orses (1 team of horses = 50 silver coins) \n [F]ood (1 lbs of food = 1 silver coins) \n [C]lothing (pair of outfits (summer&winter) = 10 silver coins) \n [S]pare parts (30 silver coins each) \n [Q]uit ")
        if x == "H" or x == "h":
            try:
                if horses < 3:
                    numHorse = int(input("How many teams of horses would you like? (Max 3): "))
                    if numHorse <= 3 and numHorse >= 0:
                        if startingmoney >= 50 * numHorse:
                            for i in range(0, numHorse):
                                startingmoney -= 50
                                horses += 1
                        else: 
                            print("You don't have enough coins for that.")
                    else: 
                        print("Invalid input. Try again.")
                else: 
                    print("You cannot buy anymore horses.")
            except: 
                print("Invalid input. Try again.")
                pass
            # print("You have", startingmoney, "silver coins left.")
        elif x == "F" or x == "f":
            try:
                foodAmount = int(input("How many pounds of food would you like?"))
                if startingmoney >= foodAmount * 1:
                    for i in range(0, foodAmount):
                        startingmoney -= 1
                    food += foodAmount
                    startingmoney = int(startingmoney)
                else: 
                    print("You don't have enough coins for that.")
            except:
                print("Invalid input. Try again.")
        elif x == "C" or x == "c":
            try:
                clothingamount = int(input("How many pairs of clothing would you like to buy? "))
                if startingmoney >= clothingamount * 10:
                    for i in range(0,clothingamount):
                        startingmoney -= 10
                    clothes += clothingamount
                else: 
                    print("You don't have enough coins for that.")
            except:
                print("Invalid input. Try again.") 
            
        elif x == "S" or x == "s":
            try:
                spareparts = int(input("How many spare parts would you like to purchase?"))
                if startingmoney >= spareparts * 30:
                    for i in range(0, spareparts):
                        startingmoney -= 30
                    spares += spareparts
                else:
                    print("You don't have enough coins for that.")
            except:
                print("Invalid input. Try again.")

        elif x == "Q" or x == "q":
            print("Okay goodbye, and good luck!")
            replay = False
        else: 
            print("Invalid input. Try again.")
        print("You have", startingmoney, "silver coins left. You have", horses, "horses,", food, "pounds of food,", spares, "spare parts, and", clothes, "pairs of clothing." )

    return startingmoney, horses, food, clothes, spares

def starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath):

    if sacrifice == True and (char1["HP"]>0 or char2["HP"]>0 or char3["HP"]>0 or char4["HP"]>0 ):
        
        if wolfbite == True:
                print(fchar["Name"], "has been attacked by a wolf.")
                listchar = [char1["Name"], char2["Name"], char3["Name"], char4["Name"]]
                if char1["HP"] <=0:
                    listchar.remove(char1["Name"])
                if char2["HP"] <= 0:
                    listchar.remove(char2["Name"])
                if char3["HP"] <= 0:
                    listchar.remove(char3["Name"])
                if char4["HP"] <= 0:
                    listchar.remove(char4["Name"])
                replay2 = True
                while replay2 == True:
                    sac = input("Would you like another character to take their place? [y]es or [n]o: ")
                    if sac == "y" or sac == "Y":
                        #print("(1)",char1["Name"],"(2)", char2["Name"], "(3)", char3["Name"],"(4)", char4["Name"])
                        print("Teammates that are available to take", fchar["Name"],"'s place.")
                        # print(listchar)
                        counter = 1
                        dict1 = {}
                        for i in listchar:
                            print("(" + str(counter) + ")", i)
                            dict1[counter] = i
                            counter+=1
                        while True:
                            try:
                                ouch = int(input("Which character will take their place? (Enter number): "))
                            except:
                                print("Invalid input. Must be an integer. Try again.")
                                continue
                            if ouch not in dict1.keys():
                                print("Invalid input. Input must be one of the numbers above:")
                            else:
                                break

                        replay = True
                        while replay == True:
                            if ouch == 1 and char1["HP"]>0:
                                print(char1["Name"], "jumps in front of", fchar["Name"], "at the last minute and saves them, but in doing so, dies.")
                                char1["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 2 and char2["HP"]>0: 
                                print(char2["Name"], "jumps in front of", fchar["Name"], "at the last minute and saves them, but in doing so, dies.")
                                char2["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 3 and char3["HP"]>0:
                                print(char3["Name"], "jumps in front of", fchar["Name"], "at the last minute and saves them, but in doing so, dies.")
                                char3["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 4 and char4["HP"]>0:
                                print(char4["Name"], "jumps in front of", fchar["Name"], "at the last minute and saves them, but in doing so, dies.")
                                char4["HP"] = 0
                                safe = True
                                replay = False
                            else: 
                                print("Invalid input. Try again.")
                        replay2 = False
                    elif sac == "n" or sac == "N":
                        print("You leave", fchar["Name"], "to the wolves.")
                        safe = False
                        replay2 = False
                    else:
                        print("Invalid input. Try again.")
        elif riverdeath == True: 
                print(fchar["Name"], "is about to die!")
                listchar = [char1["Name"], char2["Name"], char3["Name"], char4["Name"]]
                if char1["HP"] <=0:
                    listchar.remove(char1["Name"])
                if char2["HP"] <= 0:
                    listchar.remove(char2["Name"])
                if char3["HP"] <= 0:
                    listchar.remove(char3["Name"])
                if char4["HP"] <= 0:
                    listchar.remove(char4["Name"])
                replay2 = True
                while replay2 == True:
                    sac = input("Would you like another character to take their place? [y]es or [n]o: ")
                    if sac == "y" or sac == "Y":
                        #print("(1)",char1["Name"],"(2)", char2["Name"], "(3)", char3["Name"],"(4)", char4["Name"])
                        print("Teammates that are available to take", fchar["Name"],"'s place.")
                        # print(listchar)
                        counter = 1
                        dict1 = {}
                        for i in listchar:
                            print("(" + str(counter) + ")", i)
                            dict1[counter] = i
                            counter+=1
                        while True:
                            try:
                                ouch = int(input("Which character will take their place? (Enter number): "))
                            except:
                                print("Invalid input. Must be an integer. Try again.")
                                continue
                            if ouch not in dict1.keys():
                                print("Invalid input. Input must be one of the numbers above:")
                            else:
                                break

                        replay = True
                        while replay == True:
                            if ouch == 1 and char1["HP"]>0:
                                print(char1["Name"], "jumps in front of", fchar["Name"], "and takes the arrow in their own heart, saving them, but in doing so, dies.")
                                char1["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 2 and char2["HP"]>0: 
                                print(char2["Name"], "jumps in front of", fchar["Name"], "and takes the arrow in their own heart, saving them, but in doing so, dies.")
                                char2["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 3 and char3["HP"]>0:
                                print(char3["Name"], "jumps in front of", fchar["Name"], "and takes the arrow in their own heart, saving them, but in doing so, dies.")
                                char3["HP"] = 0
                                safe = True
                                replay = False
                            elif ouch == 4 and char4["HP"]>0:
                                print(char4["Name"], "jumps in front of", fchar["Name"], "and takes the arrow in their own heart, saving them, but in doing so, dies.")
                                char4["HP"] = 0
                                safe = True
                                replay = False
                            else: 
                                print("Invalid input. Try again.")
                        replay2 = False
                    elif sac == "n" or sac == "N":
                        print("You leave", fchar["Name"], "to bleed out.")
                        if fchar == char4:
                            char4["HP"] = 0
                        if fchar == char3:
                            char3["HP"] = 0
                        if fchar == char2:
                            char2["HP"] = 0
                        if fchar == char1:
                            char1["HP"] = 0
                        safe = False
                        replay2 = False
                    else:
                        print("Invalid input. Try again.")
    elif sacrifice == False and wolfbite == True:
        print(fchar["Name"], "has died from a wolf attack. No one was able to save them.")
        if fchar == char4:
            char4["HP"] = 0
        if fchar == char3:
            char3["HP"] = 0
        if fchar == char2:
            char2["HP"] = 0
        if fchar == char1:
            char1["HP"] = 0
        safe = False
    elif sacrifice == False and riverdeath == True:
        print(fchar["Name"], "bled out. No one was able to save them.")
        if fchar == char4:
            char4["HP"] = 0
        if fchar == char3:
            char3["HP"] = 0
        if fchar == char2:
            char2["HP"] = 0
        if fchar == char1:
            char1["HP"] = 0
        safe = False

    return safe

def rivercrossing(horses, char1, char2, char3, char4, food, spares, clothes, sacrifice, fchar, wolfbite):
    x = random.randint(0,2)
    riverdeath = True
    if x == 2:
        print("A large river lies in front of you. How do you cross?")
        replay = True
        while replay == True:
            choice = input("[h]orseback [c]onvince the local lord to let you use his bridge or [s]wim: ")
            if choice == "H" or choice == "h":
                if horses > 0:
                    d = random.randint(0,1)
                    if d == 0 and horses >0 :
                        print("Your horses can't swim. They drown.")
                        f = random.randint(0,3)
                        if f == 1:
                            print("")
                            alive = False
                            while alive == False:
                                x = random.randint(0,3)
                                if x == 0:
                                    if char1["HP"]>0:
                                        print(char1["Name"], "fell into the river along with the horses and drowned.")
                                        char1["HP"] = 0
                                        alive = True
                                    else:
                                        continue
                                if x == 1:
                                    if char2["HP"]>0:
                                        print(char2["Name"], "fell into the river along with the horses and drowned.")
                                        char2["HP"] = 0
                                        alive = True
                                    else:
                                        continue
                                if x == 2:
                                    if char3["HP"]>0:
                                        print(char3["Name"], "fell into the river along with the horses and drowned.")
                                        char3["HP"] = 0
                                        alive = True
                                    else:
                                        continue
                                if x == 3:
                                    if char4["HP"]>0:
                                        print(char4["Name"], "fell into the river along with the horses and drowned.")
                                        char4["HP"] = 0
                                        alive = True
                                    else:
                                        continue
                            
                                # safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar)
                                ## could add in the starksacrifice piece of code here by making another series of if statements inside of starksac to account for what kind of death it is.

                            else:
                                pass
                        else:
                            print("Luckily, your teammates all made it across the river, despite the death of one of your teams of horses")
                        horses -= 1
                    elif d == 1 and horses >1:
                        print("Your team safely crosses the river thanks to your horses.")

                    replay = False
                elif horses <= 0:
                    print("You don't have any horses to help you cross. Choose another option.")
            elif choice == "C" or choice == "c":
                x = random.randint(0,1)
                if x == 1:
                    print("You walk up to the local lord confidently.")
                    print("Knowing you all come from a great house, the lord lets you cross safely, afraid of retribution.")
                    replay = False
                elif x ==0:
                    print("You timidly approach the local lord.")
                    print("The local lord listens to your proposition, but he can sense your fear and takes advantage of your situation.")
                    print("He demands something in return.")
                    replay = True
                    while replay == True:
                        if horses < 1 and food < 100 and spares < 2 and clothes < 2:
                            print("You don't have anything that the local lord wants. He chases your team out of his castle.")
                            alive = False
                            while alive == False:
                                x = random.randint(0,3)
                                if x == 0:
                                    if char1["HP"]>0:
                                        print("One of his archers land a hit on", char1["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char1
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 1:
                                    if char2["HP"]>0:
                                        print("One of his archers land a hit on", char2["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char2
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 2:
                                    if char3["HP"]>0:
                                        print("One of his archers land a hit on", char3["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char3
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 3:
                                    if char4["HP"]>0:
                                        print("One of his archers land a hit on", char4["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char4
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                            replay = False
                        else:
                            choice = input("Choose what to trade for safe crossing. [h]orse(1) [f]ood(100 lbs) [c]lothing(2 pairs) [s]pare parts(2) [m]ake a break for it and run: ")
                        if horses >= 1 and (choice == "h" or choice =="H"):
                            horses -= 1
                            print("You now have", horses, "horses.")
                            print("You trade one of your horse teams for safe crossing.")
                            replay = False
                        elif choice == "H" or choice == "h":
                            print("You don't have enough horses.")
                        elif choice == "M" or choice == "m":
                            print("Your team tries to hold onto their belongings. You all make a break for it and run towards the bridge!")
                            alive = False
                            while alive == False:
                                x = random.randint(0,3)
                                if x == 0:
                                    if char1["HP"]>0:
                                        print("One of his archers land a hit on", char1["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char1
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 1:
                                    if char2["HP"]>0:
                                        print("One of his archers land a hit on", char2["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char2
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 2:
                                    if char3["HP"]>0:
                                        print("One of his archers land a hit on", char3["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char3
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                                if x == 3:
                                    if char4["HP"]>0:
                                        print("One of his archers land a hit on", char4["Name"])
                                        print("The arrow goes straight through their heart.")
                                        fchar = char4
                                        safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                                        print("In the chaos, the rest of your team manages to quickly cross the river over the lord's bridge, despite his wishes.")
                                        alive = True
                                    else:
                                        continue
                            replay = False
                        elif (choice == "s" or choice == "S") and spares >= 2:
                            print("You trade 2 spare parts for safe crossing.")
                            spares-=2
                            print("You now have", spares, "spare parts left.")
                            replay = False
                        elif choice == "s" or choice == "S":
                            print("You don't have enough spares to trade.")
                        elif (choice == "f" or choice == "F") and food >= 100:
                            print("You trade 100lbs of food for safe crossing.")
                            food -= 100
                            replay = False
                        elif choice == "f" or choice == "F":
                            print("You don't have enough food to trade")
                        elif (choice == "C" or choice == "c") and clothes >=2:
                            print("You trade 2 clothes.")
                            clothes -= 2
                            print("You now have",clothes,"clothes left.")
                            replay = False
                        elif choice == "C" or choice == "c":
                            print("You don't have enough clothes to trade.")
                        else:
                            print("")
                        
                    replay = False
                
                replay = False
            elif choice == "S" or choice == "s":
                x = random.randint(0,1)
                if x == 0:
                    print("You thought you could all swim across the river? Cute.")
                    replay = True
                    while replay == True:
                        y = random.randint(0,3)
                        if y == 0:
                            if char1["HP"]>0:
                                fchar = char1
                                print(fchar["Name"], "drowned")
                                char1["HP"]=0
                                replay = False
                        elif y == 1:
                            if char2["HP"]>0:
                                fchar = char2
                                print(fchar["Name"], "drowned")
                                char2["HP"]=0
                                replay = False
                        elif y == 2:
                            if char3["HP"]>0:
                                fchar = char3
                                print(fchar["Name"], "drowned")
                                char3["HP"]=0
                                replay = False
                        elif y == 3:
                            if char4["HP"]>0:
                                fchar = char4
                                print(fchar["Name"], "drowned")
                                char4["HP"]=0
                                replay = False
                    print("The team carries on across the river.")
                elif x == 1:
                    print("Somehow, the 7 gods blessed your team and you all made it across the river.")
                replay = False
            else:
                print("invalid input. Try again.")
        replay = False
    return horses, spares, clothes, food, riverdeath, fchar #do i need to return these? What must i return 

def fire(char1, char2, char3, char4, fireimmunity, horses, food, spares, clothes):
    g = random.randint(0,50)
    if g == 1 and fireimmunity == False:
        char1["HP"] = 0
        char2["HP"] = 0
        char3["HP"] = 0
        char4["HP"] = 0
        print("Your wagon got set on fire, and burns everything and everyone!")
        horses = 0
        food = 0
        spares = 0
        clothes = 0
        print(char1["Name"],",", char2["Name"],",", char3["Name"],", and", char4["Name"]," have all perished.")
    elif g == 1 and fireimmunity == True: 
        print("Your wagon got set on fire, and burns everything! Luckily, since fire cannot kill a dragon and you are house Targaryen, your team is safe.")
        horses = 0
        food = 0
        spares = 0
        clothes = 0
    else:
        print("")

    pass
    return char1, char2, char3, char4, horses, food, spares, clothes

#14 days 
def day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity):
    while char1["HP"]>0 or char2["HP"]>0 or char3["HP"]>0 or char4["HP"]>0:
        if char1["HP"]>0 or char2["HP"]>0 or char3["HP"]>0 or char4["HP"]>0:
            print("It is day", str(daynum), "of your journey.")
            daysleft = 8 - daynum
            print("You have", str(daysleft), "days left and", miles,"miles left to go until you reach King's Landing.")
            print("")
            ## WOLFBITE
            x = random.randint(0,10)
            if x == 1:
                wolfbite = True
                y = random.randint(0,4)
                if y == 0 and char1["HP"]>0:
                    fchar = char1
                    safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                    if safe == False:
                        char1["HP"] = 0
                elif y == 1 and char2["HP"]>0:
                    fchar = char2
                    safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                    if safe == False:
                        char2["HP"] = 0
                elif y == 2 and char3["HP"]>0:
                    fchar = char3
                    safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                    if safe == False:
                        char3["HP"] = 0
                elif y == 3 and char4["HP"]>0:
                    fchar = char4
                    safe = starksacrifice(sacrifice, char1, char2, char3, char4, fchar, wolfbite, riverdeath)
                    if safe == False:
                        char4["HP"] = 0
            
            else:
                pass
        else:
            break
        horses, spares, clothes, food, riverdeath, fchar = rivercrossing(horses, char1, char2, char3, char4, food, spares, clothes, sacrifice, fchar, wolfbite)

        char1, char2, char3, char4, horses, food, spares, clothes = fire(char1, char2, char3, char4, fireimmunity, horses, food, spares, clothes)

        listchar = [char1["Name"], char2["Name"], char3["Name"], char4["Name"]]
        if char1["HP"] <=0:
            listchar.remove(char1["Name"])
        if char2["HP"] <= 0:
            listchar.remove(char2["Name"])
        if char3["HP"] <= 0:
            listchar.remove(char3["Name"])
        if char4["HP"] <= 0:
            listchar.remove(char4["Name"])
        for i in listchar:
            food -= 15
        if food < 0:
            food = 0
            if char1["HP"]>0:
                char1["HP"] -= 5
                if char1["HP"]<=0:
                    print(char1["Name"], "has starved.")
                char1["Hunger"] += 5
            if char2["HP"]>0:
                char2["HP"] -= 5
                if char2["HP"]<=0:
                    print(char2["Name"], "has starved.")
                char2["Hunger"] += 5
            if char3["HP"]>0:
                char3["HP"] -=5
                if char3["HP"]<=0:
                    print(char3["Name"], "has starved.")
                char3["Hunger"] += 5
            if char4["HP"] > 0 :
                char4["HP"] -= 5
                if char4["HP"]<=0:
                    print(char4["Name"], "has starved.")
                char4["Hunger"] +=5

        

        miles -= 200
        
        print("You have", money, "silver coins left. You have", horses, "horses,", food, "pounds of food,", spares, "spare parts, and", clothes, "pairs of clothing." )
        print("How the squad is doing: ")
        if char1["HP"]>0:
            print(char1)
        if char2["HP"]>0:
            print(char2) 
        if char3["HP"]>0:
            print(char3)
        if char4["HP"] > 0 :
            print(char4)
        if char1["HP"]<=0 and char2["HP"]<=0 and char3["HP"]<=0 and char4["HP"]<=0:
            print("Really bad. Everyone died.")
        
        input("Press enter to continue:")
        break
    return miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar

def main():
    gameOver = False
    horses = 0
    spareparts = 0
    foodAmount = 0 
    clothingamount = 0
    food = 0
    clothes = 0
    spares = 0
    fchar = {}
    riverdeath = False
    wolfbite = False
    miles = 1600
        # Print the text
    while gameOver == False:
        
        choice = input("What would you like to do? [p]lay, [i]nstructions, [s]ee map of Westeros [q]uit: ")
        if choice == "p" or choice == "P": 
            print("You have entered The Kingsroad")
            char1 = {"Name": "", "HP": "", "Hunger": 0, "Items": "none"}
            char2 = {"Name": "", "HP": "", "Hunger": 0, "Items": "none"}
            char3 = {"Name": "", "HP": "", "Hunger": 0, "Items": "none"}
            char4 = {"Name": "", "HP": "", "Hunger": 0, "Items": "none"}

            print("Choose your team to travel along the kingsroad with.")

            

            # 10 levels
            # instant deaths: 
            # cons: wolf pack, bandits, wildlings, assassin (randomize who they target) , hand cut off? things like that., fall asleep on watch, horse dies, run out of food - each level your food goes down 
            #more cons: 
            #pros: find tavern, sleep, steal horse,

            print("Who will Character 1 be? ")
            char1name = input("Enter name: ")
            char1["HP"] = random.randint(30,50)
            char1["Name"] = char1name
            print("Who will character 2 be?")
            char2name = input("Enter name: ")
            char2["HP"] = random.randint(30,50)
            char2["Name"] = char2name
            print("Who will character 3 be? ")
            char3name = input("Enter name: ")
            char3["HP"] = random.randint(30,50)
            char3["Name"] = char3name
            print("Who will character 4 be? ")
            char4name = input("Enter name: ")
            char4["HP"] = random.randint(30,50)
            char4["Name"] = char4name
            print("Your team is", char1name, ",", char2name, ",", char3name, ", and ", char4name)
            
            team = [char1name, char2name, char3name, char4name]
            
            print("Character stats: ")
            print(char1)
            print(char2)
            print(char3)
            print(char4)

            house = houseChoice()
            print("You have chosen House", house +"!")

            # apply all the effects of the chosen houses
            if house == "Stark":
                startingmoney = 300
                sacrifice = True
                fireimmunity = False
            if house == "Lannister":
                startingmoney = 350
                sacrifice = False
                fireimmunity = False
            if house == "Baratheon":
                startingmoney = 300
                char1["HP"] += 5
                char2["HP"] += 5
                char3["HP"] += 5
                char4["HP"] += 5
                sacrifice = False
                fireimmunity = False
            if house == "Targaryen":
                startingmoney = 300
                fireimmunity = True
                sacrifice = False
            money, horses, food, clothes, spares = shop(startingmoney, horses, foodAmount, clothingamount, spareparts, food, clothes, spares)
            #money is new variable assigned to how many silver coins you have 
            print("Now that you have bought your supplies, it is time to begin your journey to King's Landing.")
            miles = 1600
            #200 miles per day
            daynum = 0
            
            while daynum < 9 and (char1["HP"]>0 or char2["HP"]>0 or char3["HP"]>0 or char4["HP"]>0):
                
                daynum = 1
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                daynum = 2
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                daynum = 3
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                daynum = 4
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                daynum = 5
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                
                daynum = 6
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                
                daynum = 7
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
            
                daynum = 8
                miles, food, horses, spares, clothes, char1, char2, char3, char4, fchar = day(daynum, char1, char2, char3, char4, sacrifice, miles, horses, spares, clothes, food, fchar, wolfbite, riverdeath, money, fireimmunity)
                daynum = 9
            survivingcharacters = []
            if char1["HP"]<=0 and char2["HP"]<=0 and char3["HP"]<=0 and char4["HP"]<=0:
                print("You did not make it to King's Landing.")
                print("All members of your team died.")
            elif char1["HP"]>0 or char2["HP"]>0 or char3["HP"]>0 or char4["HP"]>0:
                print("You have made it to King's Landing")
                if char1["HP"]>0:
                    survivingcharacters.append(char1["Name"])
                if char2["HP"]>0:
                    survivingcharacters.append(char2["Name"])
                if char3["HP"]>0 :
                    survivingcharacters.append(char3["Name"])
                if char4["HP"]>0:
                    survivingcharacters.append(char4["Name"])
                print("Surviving teammates: ")
                for i in survivingcharacters:
                    print(i)
            else: 
                print("Something went wrong on the way to King's Landing.")

            #RESET VARIABLES FOR REPLAYABILITY
            horses = 0
            spareparts = 0
            foodAmount = 0 
            clothingamount = 0
            food = 0
            clothes = 0
            spares = 0
            wolfbite = False
            riverdeath = False
            miles = 1600
        elif choice == "s" or choice == "S":
            with open("westeros.txt", "r") as f:
                map = f.readlines()

            #RWBY team instead? 
            #could have team name function, combat functions easier? 

            def printmap(map):
                #Args:
                    #board (list of lists): Contains all of the data of a specific board.

                    #boardWidth (int): This is how many spaces wide the board is.

                    #boardHeight (int): This is how many spaces high the board is
                for i in range(0, 14):
                    row = str(i)
                    for j in range(0, 8):
                        print(map[i][j], end="")
                return
            print("Map of Westeros:")
            printmap(map)

            #print(map[0][2]) #This is Winterfell's coordinate
            level = 1
            print(pytext.format_text(text="W = Winterfell (Starting Point)" + map[0], color="red", bgcolor="black"))
            text = pytext.format_text(text="K = King's Landing (Destination)"+ map[13], color="red",
                                    bgcolor="black")
            print(text)
        elif choice == "i" or choice == "I":
            #instructions???
            print("")
            print("You must travel from Winterfell to King's Landing by the Kingsroad to avenge a friend's wrongful execution.")
            print("Along with yourself, 3 others will journey with you. But proceed with caution, the night is dark and full of terrors. Choose your teammates carefully..")
            print("")
        elif choice == "q" or choice == "Q":
            print("Okay, bye!")
            gameOver = True
        else: 
                print("Invalid input. Try again. ")

if __name__ == "__main__":
    main()

