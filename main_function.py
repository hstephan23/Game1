import json


def first_choice(gold):
    print("Choose left or right.")
    print("[1] Left")
    print("[2] Right")
    choice_1 = input()
    while True:
        if choice_1 == "1":
            print("You run into an orc on your journey, who seems much stronger and bigger than you.")
            print("Do you fight or run?")
            print("[1] Fight")
            print("[2] Run")
            choice_1a = input()
            while True:
                if choice_1a == "1":
                    print("You valiantly try to fight the orc, but ultimately you end up dying a sad and meaningless "
                          "life.")
                    print("Game over. Total gold: " + str(gold))
                    return 1
                elif choice_1a == "2":
                    print("You trip as you run away, falling down a hill and into a forest.")
                    break
                else:
                    choice_1a = input("Try again! 1 or 2? ").lower()
            break
        elif choice_1 == "2":
            print("You begin your journey in the forest.")
            break
        else:
            choice_1 = input("Try again! 1 or 2? ")


def weapon(character_name):
    print("Which weapon do you find? ")
    print("[1] Sword")
    print("[2] Spear")
    print("[3] Bow")
    c_class = input()
    while True:
        if c_class == "1":
            print("Congratulations " + character_name + "! You are a swordsman!")
            print("You are strong, but slow.")
            character_class = "sword"
            return character_class
        if c_class == "2":
            print("Congratulations " + character_name + "! You are a spearman!")
            print("You are medium strength, and medium speed")
            character_class = "spear"
            return character_class
        if c_class == "3":
            print("Congratulations " + character_name + "! You are a bowman!")
            print("You are weak, but fast.")
            character_class = "bow"
            return character_class
        else:
            c_class = input("Try again! 1, 2, or 3? ")


def goblin(character_class, gold):
    print("You come across a weak goblin, do you fight or hide? ")
    print("[1] fight")
    print("[2] hide")
    choice_2 = input()
    # You have name and class stowed now, gold should = 0
    while True:
        if character_class == "sword" and choice_2 == "1":
            print("Congrats! You defeated the goblin. You now have 25 gold.")
            gold += 25
            return 25
        elif character_class == "spear" and choice_2 == "1":
            print("Congrats! You defeated the goblin. You now have 25 gold.")
            gold += 25
            return 25
        elif character_class == "bow" and choice_2 == "2":
            print("You hide from the goblin, but see an opening as it walks by. "
                  "You slay the goblin and find 25 gold.")
            gold += 25
            return 25
        elif character_class == "sword" and choice_2 == "2":
            print("You hide from the goblin, but make noise in your escape. "
                  "The goblin pulls out its bow and kills you.")
            print("Game over. Total gold: " + str(gold))
            return 0
        elif character_class == "spear" and choice_2 == "2":
            print("You hide from the goblin, waiting for an opportunity to strike. "
                  "It never comes, but they do drop their money pouch. You now have 25 gold.")
            gold += 25
            return 25
        elif character_class == "bow" and choice_2 == "1":
            print("You forget that you are weak. You cry out before attacking and miss the shot."
                  " The Goblin knives you in the gut and lets you die slowly.")
            print("Game over. Total gold: " + str(gold))
            return 0
        else:
            choice_2 = input("Try again! 1 or 2? ")


def traveler(gold):
    print("You come across a fellow traveller. "
          "Do you speak or keep walking? ")
    print("[1] Speak")
    print("[2] Keep Walking")
    choice_3 = input()
    while True:
        if choice_3 == "2":
            print("Good choice, he looked scary.")
            return 0
        elif choice_3 == "1":
            print("After listening to him speak for three hours, you pull out your knife and "
                  "kill him. Taking his 2 gold from his corpse.")
            gold += 2
            return 2
        else:
            choice_3 = input("Try again! 1 or 2? ").lower()


def sleep():
    print("You are feeling sleepy. Do you make a fire or not?")
    print("[1] Yes")
    print("[2] No")
    choice_4 = input()
    while True:
        if choice_4 == "1":
            print("You sleep warm through the night and wake up feeling refreshed.")
            return
        elif choice_4 == "2":
            print("You sleep safe through the night, but wake up wishing you were warmer.")
            return
        else:
            choice_4 = input("Try again! 1 or 2? ")


def group_of_goblins(character_class, gold):
    print("You see a group of goblins from afar, what do you do?")
    print("[1] Run")
    print("[2] Fight")
    print("[3] Hide")
    choice_5 = input()
    while True:
        if choice_5 == "1" and (character_class == "sword" or character_class == "spear"):
            print("You trip on your weapon and fall into a hole. Losing all your money.")
            return 0
        elif choice_5 == "1" and character_class == "bow":
            print("You probably made the right choice, you are weak...")
            return 2
        elif choice_5 == "2" and (character_class == "sword" or character_class == "spear"):
            print("You are stronger than you think and kill the three goblins. You find 100 gold!")
            return 100
        elif choice_5 == "2" and character_class == "bow":
            print("You die... You are weak, remember?")
            print("Game over. Total gold: " + str(gold) + ".")
            return 1
        elif choice_5 == "3" and (character_class == "sword" or character_class == "spear"):
            print("You regret your decision right away, and think about your life choices "
                  "leading up to now. "
                  "You decide to retire from the adventuring life. ")
            print("You give up.")
            print("You retire happy and with " + str(gold) + " gold. With this you life a semi satisfied life.")
            return 1
        elif choice_5 == "3" and character_class == "bow":
            print("You successful hide, finding a patch of strawberries to eat."
                  " You are kind of satisfied, but not richer.")
            return
        else:
            choice_5 = input("Try again! 1, 2, or 3? ")


def town(gold, weapons):
    store = ["[1] Sword--25 gold", "[2] Food--1 gold", "[3] Shield--30 gold", "[4] Nothing--0 gold"]
    print("You come across a town, do you enter?")
    print("[1] Yes")
    print("[2] No")
    choice_6 = input()
    while True:
        if choice_6 == "2":
            print("You have no social skills, but keep all your money.")
            break
        elif choice_6 == "1":
            print("Nice! Do you want to make a purchase? Or gamble? Or nothing? ")
            print("[1] Make a purchase")
            print("[2] Gamble")
            print("[3] Nothing")
            choice_6a = input()
            while True:
                if choice_6a == "1":
                    while True:
                        print("What do you want to buy? You have: " + str(gold) + " gold")
                        print(*store, sep="\n")
                        purchase = input("")
                        if purchase == "1" and gold >= 25:
                            character_secondary = "sword"
                            weapons.append(character_secondary)
                            gold = gold - 25
                            store.remove("[1] Sword--25 gold")
                        elif purchase == "1" and gold < 25:
                            print("Not enough gold")
                        elif purchase == "2" and gold >= 1:
                            character_secondary = "food"
                            weapons.append(character_secondary)
                            gold = gold - 1
                            store.remove("[2] Food--1 gold")
                        elif purchase == "2" and gold < 1:
                            print("Not enough gold!")
                        elif purchase == "3" and gold >= 30:
                            character_secondary = "shield"
                            weapons.append(character_secondary)
                            gold = gold - 30
                            store.remove("[3] Shield--30 gold")
                        elif purchase == "3" and gold < 30:
                            print("Not enough gold!")
                        elif purchase == "4":
                            return
                        else:
                            print("Try again! 1, 2, 3, or 4. ")
                            purchase = input()
                elif choice_6a == "2":
                    print("You see an inn. You enter the inn. There is a game of what looks like black jack.")
                    amount = input("How much money do you want to gamble? You have " + str(gold) + " gold.")
                    if 10 <= int(amount) < 20 and int(amount) <= gold:
                        print("You are balanced, luckily your gamble pays off. Plus " + amount + " gold!")
                        gold = gold + int(amount)
                        return gold
                    elif 20 <= int(amount) <= gold:
                        print("You are very ambitious... It doesn't pay off. You lose that gold...")
                        gold = gold - int(amount)
                        return gold
                    elif int(amount) < 10 and int(amount) <= gold:
                        print("You are very conservative, it doesn't pay off though. You lose your money.")
                        gold = gold - int(amount)
                        return gold
                    else:
                        print("Try again! Please input value. ")
                        amount = input()
                elif choice_6a == "3":
                    print("You decide against spending any gold and continue on your way.")
                    break
                else:
                    choice_6a = input("Try again! Make a 1, 2, or 3. ").lower()
            break
        else:
            print("Try again! 1 or 2? ")
            choice_6 = input()


def fire(gold, weapons):
    print("After passing through town, you see what looks like a fire in the distance.")
    print("Do you go towards it or keep following the path? ")
    print("[1] Towards the fire")
    print("[2] Keep following the path")
    choice_7 = input()
    while True:
        if choice_7 == "1":
            print("You are adventurous and seek the fun in things. You continue towards the fire.")
            print("As you get closer, you see that there are orcs around the fire. "
                  "Do you engage them head on?")
            print("[1] Yes")
            print("[2] No")
            choice_7a = input()
            while True:
                if choice_7a == "1" and ("shield" in weapons) and ("sword" in weapons):
                    print("You courageously fight the orcs.")
                    print("Your shield protecting your back while your extra sword slays the enemies before you.")
                    print("You are able to find 300 gold in the corpses of your slain enemies.")
                    return 300
                elif choice_7a == "1" and ("sword" in weapons):
                    print("Your extra blade serves you well. You are able to slay the orcs and obtain 300 gold "
                          "from the corpses.")
                    gold = gold + 300
                    return 300
                elif choice_7a == "1" and ("shield" in weapons):
                    print("You fight for your life, your shield protects you from any killing blows.")
                    print("Ultimately you "
                          "survive,"
                          "but can no longer adventure. ")
                    print("You collect the 300 gold from the orcs' corpse and retire.")
                    gold = gold + 300
                    print("Your total gold was: " + str(gold) + ".")
                    return 0
                elif choice_7a == "1" and weapons == "none":
                    print("You fight to the valiant end, but it isn't enough. You die a meaningless life...")
                    print("Game over. Total gold: " + str(gold))
                    return 0
                elif choice_7a == "2":
                    print("Smart choice, best not to attract the attention of them. "
                          "You wait it out until the orcs are clear and you go to loot. You find 25 gold.")
                    return 25
                else:
                    print("Try again! 1 or 2? ")
                    choice_7a = input()
        elif choice_7 == "2":
            print("You are boring and don't seek the adventures that mysterious things can bring.")
            break
        else:
            choice_7 = input("Try again! 1 or 2? ")


def cave():
    print("You resume your journey on the path, going through winding and treacherous pathways. ")
    print("You see a cave, enter?")
    print("[1] Yes")
    print("[2] No")
    choice_8 = input()
    while True:
        if choice_8 == "1":
            print("The cave is dark and scary, do you light a torch?")
            print("[1] Yes")
            print("[2] No")
            choice_8a = input()
            if choice_8a == "1":
                print("The cave is not that scary, it actually is a dead end! You turn around.")
                return 0
            if choice_8a == "2":
                print("You run into the end of the cave, hitting your head. You drop some of your gold in the dark. "
                      "Afraid that you are going lose more gold you turn around. You lose 2 gold.")
                return -2
        elif choice_8 == "2":
            print("You don't find any treasures, but you didn't die or lose gold. You continue on your way.")
            return 0


def turn_around(gold):
    print("You are getting tired, continue the journey? Or turn back home?")
    print("[1] Continue")
    print("[2] Return")
    choice_9 = input()
    while True:
        if choice_9 == "1":
            print("You decide that you aren't one to turn around so easily. You continue to trek onwards.")
            return
        elif choice_9 == "2":
            print("You return home, now richer than before. You are pleased with yourself and your journey."
                  "You had " + str(gold) + " gold.")
            return 0
        else:
            choice_9 = input("Try again! 1 or 2? ").lower()


def elves(party, gold):
    print("You see a party of elves in the distance. Do you approach them or not? ")
    print("[1] Yes")
    print("[2] No")
    choice_10 = input()
    while True:
        if choice_10 == "1":
            print("You approach the elves and begin speaking to them. "
                  "One of them is quite friendly and asks to join your party.")
            print("Do you let him join you on your adventure?")
            print("[1] Yes")
            print("[2] No")
            choice_10a = input()
            while True:
                if choice_10a == "1":
                    print("You now have a partner in crime. His name is Elderod.")
                    party.append("Elderod")
                    return
                # party[0] = Elderod
                elif choice_10a == "2":
                    print("The elves are disgusted by your arrogance. They kill you.")
                    print("Game over. Total gold: " + str(gold) + ".")
                    return 0
                else:
                    choice_10a = input("Try again! 1 or 2? ").lower()
        elif choice_10 == "2":
            print("You remember that you are anti-social, and decide against talking to the elves.")
            return
        else:
            choice_10 = input("Try again! 1 or 2 ").lower()


def ravine(party, gold):
    print("You decide to continue on with your journey. You party size is: " + (str(len(party)))
          + ".")
    print("Your journey brings you to a large ravine, do you use the scary bridge or attempt to "
          "go around it?")
    print("[1] Use bridge")
    print("[2] Attempt to go around")
    choice_11 = input()
    while True:
        if choice_11 == "1" and len(party) > 1:
            print("You successfully make it across the bridge. It was close by your full party survives.")
            return
        elif choice_11 == "1" and len(party) <= 1:
            print("You successfully make it across the bridge. You save yourself time and energy.")
            return
        elif choice_11 == "2":
            print("You can't seem to find a way around. Disheartened by the walking, "
                  "you decide to turn around and end your journey.")
            print("You retire happily, you had " + str(gold) + "!")
            return 0
        else:
            choice_11 = input("Try again! 1 or 2? ").lower()


def dog(weapons, party):
    print("Now safely across the ravine, you begin searching for your next adventure.")
    print("You see a dog, do you attempt to befriend it?")
    print("[1] Yes")
    print("[2] No")
    choice_12 = input()
    while True:
        if choice_12 == "1" and ("food" in weapons):
            print("You offer your food to the dog and you befriend the dog. What is it's name?")
            dog_name = input()
            party.append(dog_name)
            return
        elif choice_12 == "1":
            print("Nice try! The dog runs away.")
            break
        elif choice_12 == "2":
            print("The dog looks sad that you didn't try to befriend him. "
                  "You continue onwards, realizing your mistake.")
            break
        else:
            choice_12 = input("Try again! 1 or 2? ")
    if len(party) > 1:
        print("You and your party decide to keep moving forward.")
    else:
        print("You decide to continue moving forward.")


def turn_back(party, gold):
    print("The way ahead looks scary. This is your last chance to turn back. Turn back?")
    print("[1] Continue")
    print("[2] Turn back")
    choice_13 = input()
    while True:
        if choice_13 == "1":
            print("You take the first step forward, risking your life in the process.")
            return
        elif choice_13 == "2":
            print("You decide that you treasure your life more than adventure. You turn back.")
            print("You survived with " + str(gold) + ".")
            print("Your party members: ")
            print(*party, sep=', ')
            return 0
        else:
            choice_13 = input("Try again! 1 or 2? ")


def skeletons(party, weapons, gold):
    print("You see what looks like a tower in the distance. There doesn't appear to be any lights on.")
    print("You approach cautiously, taking care to not make any excess noise.")
    print("You think you see skeleton warriors. Do you draw your weapon?")
    print("[1] Yes")
    print("[2] No")
    choice_14 = input()
    while True:
        if choice_14 == "1" and (len(party) > 1 or ("sword" in weapons)):
            print("You decide to be aggressive and draw your weapons.")
            print("Your party does the same. The noise draws in the skeletons.")
            print("Luckily you are prepared and dispatch of them easily.")
            print("You search the tower and find 2 small rubies worth 50 gold.")
            gold = gold + 50
            return 50
        elif choice_14 == "1" and len(party) < 1:
            print("You decide to be aggressive and draw your weapons.")
            print("The noise draws in the skeletons. Unfortunately they are too much of a match for you.")
            print("You die, slain by the skeletons.")
            print("Game over. Total gold: " + str(gold) + ".")
            return 0
        elif choice_14 == "2" and len(party) == 2:
            print("You decide that you would draw too much attention.")
            print("The skeletons find you anyways. You fight, but " + str(party[1]) + " is badly injured.")
            print(str(party[1]) + " dies...")
            print("You continue onward, knowing that is what they would want.")
            party.pop(1)
            return
        elif choice_14 == "2" and len(party) == 3:
            print("You decide that you would draw too much attention.")
            print("The skeletons find you anyways. You fight, but " + str(party[2]) + " is hurt.")
            print(str(party[1]) + " departs the group and decides to seek medical attention.")
            party.pop(1)
            return
        elif choice_14 == "2" and len(party) <= 1:
            print("You decide that you would draw too much attention.")
            print("The skeletons walk directly by you, but you avoid their detection.")
            print("You carefully search the tower and find 2 rubies worth 50 gold.")
            gold = gold + 50
            return 50
        else:
            choice_14 = input("Try again! 1 or 2?")


def add_to_scoreboard(party, gold):
    score_board = open("Score_board.json", "a")
    score_board.write(", ".join(party) + ": " + str(gold) + " gold" + "\n")
    score_board.close()


def sort_scoreboard():
    previous_character = 0
    score_board = []
    value = []
    values = [0]
    with open("Score_board.json", "r") as file:
        for line in file:
            score_board.append(line)
    for line in score_board:
        for item in line.split():
            if item.isdigit() is True:
                if int(item) >= previous_character:
                    previous_character = int(item)
                    value.insert(0, line)
                    values.insert(0, item)
                else:
                    count = 0
                    for piece in values:
                        if int(item) >= int(piece):
                            value.insert(count, line)
                            values.insert(count, item)
                            break
                        else:
                            count += 1
                            continue
    real_score_board = open("Score_board_real.json", "w")
    for item in value:
        real_score_board.write(item)
    real_score_board.close()
    line_number = []
    counter = 0
    with open("Score_board_real.json", "r") as json_file:
        for line_2 in json_file:
            counter += 1
            if counter <= 10:
                line_number.append(str(counter) + " " + line_2)
            else:
                continue
    score_board_update = open("Score_board_final.json", "w")
    for line_3 in line_number:
        score_board_update.write(line_3)
    score_board_update.close()


def print_scoreboard():
    score_board = []
    with open("Score_board_final.json", "r") as json_file:
        for line in json_file:
            score_board.append(line)
    print(*score_board)


def main_adventure():
    gold = 0
    party = []
    weapons = []
    print("No spaces at the end or beginning of the answers please.")
    character_name = input("Insert your name: ")
    print("Hello " + character_name + "! Today we embark on a journey!")
    party.append(character_name)
    death_1 = first_choice(gold)
    if death_1 == 1:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    character_class = weapon(character_name)
    goblin_gold = goblin(character_class, gold)
    if goblin_gold == 0:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    test_goblin = isinstance(goblin_gold, int)
    if test_goblin is True:
        gold = gold + goblin_gold
    traveler_gold = traveler(gold)
    gold = gold + traveler_gold
    sleep()
    gold_group_of_goblins = group_of_goblins(character_class, gold)
    if gold_group_of_goblins == 1:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    elif gold_group_of_goblins == 0:
        gold = gold_group_of_goblins
    elif gold_group_of_goblins == 100:
        gold = gold + gold_group_of_goblins
    town_gold = town(gold, weapons)
    test_town = isinstance(town_gold, int)
    if test_town is True:
        gold = town_gold
    else:
        if "sword" in weapons and "shield" in weapons and "food" in weapons:
            gold = gold - 56
        elif "sword" in weapons and "shield" in weapons:
            gold = gold - 55
        elif "sword" in weapons and "food" in weapons:
            gold = gold - 31
        elif "sword" in weapons:
            gold = gold - 25
        elif "shield" in weapons:
            gold = gold - 30
        elif "food" in weapons:
            gold = gold - 1
        else:
            gold = gold
    gold_from_orcs = fire(gold, weapons)
    if gold_from_orcs == 0:
        return
    test_orcs = isinstance(gold_from_orcs, int)
    if test_orcs is True:
        gold = gold + gold_from_orcs
    gold_from_cave = cave()
    gold = gold + gold_from_cave
    end_1 = turn_around(gold)
    if end_1 == 0:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    elf_party = elves(party, gold)
    test_elf = isinstance(elf_party, int)
    if test_elf is True:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    test_ravine = ravine(party, gold)
    if test_ravine == 0:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    dog(weapons, party)
    decision = turn_back(party, gold)
    if decision == 0:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    skeleton = skeletons(party, weapons, gold)
    if skeleton == 0:
        add_to_scoreboard(party, gold)
        sort_scoreboard()
        print_scoreboard()
        return
    test_skeleton = isinstance(skeleton, int)
    if test_skeleton is True:
        gold = gold + skeleton
    print("Thank you for playing " + character_name + "! You had a total of " + str(gold) + " gold!")
    print("You're party consisted of:")
    print(*party, sep=', ')
    print(character_class)
    print(gold)
    print(*weapons, sep= ", ")
    add_to_scoreboard(party, gold)
    sort_scoreboard()
    print_scoreboard()

main_adventure()
