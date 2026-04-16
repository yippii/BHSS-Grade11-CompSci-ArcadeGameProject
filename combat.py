import random as r
import constants as c

#This function controls the basic combat, allowing the user to choose their actions
def found_monster_actions():
    global battle_action
    while battle == True:
        try:
            print(c.blocker)
            print("You stumble upon a " + monster + "!")
            print(" 1 - Attack\n 2 - Inventory\n 3 - Flee")
            battle_action = int(input(c.wyd))
            return
        except:
            print(c.blocker)
            print(c.tno)

#This function controls which attack function is called based on the user's choice
def battle_attack_action():
    global battle
    while battle == True:
        try:
            print(c.blocker)
            print("Attack")
            print(c.blocker)
            print(" 1 - " + weapon1 + "\n 2 - " + weapon2 + "\n 3 - " + weapon3 + "\n 5 - Back")
            battle_attack = int(input(c.wyd))
            if battle_attack == 1:
                sword_fighting()
            elif battle_attack == 2:
                bow_fighting()
            elif battle_attack == 5:
                return
            else:
                print(c.blocker)
                print(c.tno)
        except:
            print(c.blocker)
            print(c.tno)

#This weapon checks if weapons have been discovered. If discovered, it shares their name 
def weapon_checker():
    if have_sword == True:
        weapon1 = "Sword"
    else:
        weapon1 = "???"
    if have_bow == True:
        weapon2 = "Bow"
    else:
        weapon2 = "???"
    if have_crossbow == True:
        weapon3 = "Crossbow"
    else:
        weapon3 = "???"

#This function controls the sword fighting process, using swords and stamina
def sword_fighting():
    global sword_amount
    if sword_amount >= 1:
        while battle == True:
            global stamina
            print(c.blocker)
            print("You use your sword!")
            sword_battle_roll = r.randint(1,6)
            if sword_battle_roll <= 2:
                print(c.m)
                miss_stamina_loss = r.randint(1,2)
                if miss_stamina_loss == 1:
                    print(c.s1)
                    print(c.no_sw)
                    stamina = stamina - 1
                else:
                    print(c.no_s)
                    print(c.no_sw)
                return
            elif sword_battle_roll <= 4:
                print(c.h)
                print(c.s1)
                print(c.sw1)
                stamina = stamina - 1
                sword_amount = sword_amount - 1
                return
            else:                    
                print(c.ph)
                print(c.no_s)
                print(c.sw1)
                sword_amount = sword_amount - 1
                return
    else:
        print(c.blocker)
        print(c.nowe)
        return

#This function controls the bow fighting process, using arrows and stamina
def bow_fighting():
    global arrow_amount
    global have_bow
    if have_bow == True:
        if arrow_amount >= 1:
            while battle == True:
                global stamina
                print(c.blocker)
                print("You use your bow!")
                bow_battle_roll = r.randint(1,6)
                if bow_battle_roll <= 3:
                    print(c.m)
                    print(c.s2)
                    print(c.a1)
                    stamina = stamina - 2
                    arrow_amount = arrow_amount - 1
                    return
                else:
                    print(c.ph)
                    print(c.no_s)
                    print(c.a1)
                    arrow_amount = arrow_amount - 1
                    return
            else:
                print(c.nowe)
                return
        else:
            print(c.blocker)
            print("You do not have any more arrows!")
    else:
        print(c.blocker)
        print(c.nowe)

#This function controls which function and process is called based ont he user's choice
def battle_inventory_action():
    global sword_amount
    global arrow_amount
    while battle == True:
        try:
            print(c.blocker)
            print("Inventory: ")
            print(c.blocker)
            print(" 1 - Stamina Potion\n 2 - Swords\n 3 - Arrows\n 4 - Special Items\n 5 - Back")
            battle_inv = int(input(c.wyd))
            if battle_inv == 1:
                s_pot_inv()
            elif battle_inv == 2:
                print(c.blocker)
                print("You have " + str(sword_amount) + " swords.")
            elif battle_inv == 3:
                print(c.blocker)
                print("You have " + str(arrow_amount) + " arrows.")
            elif battle_inv == 4:
                print(c.blocker)
                print("You have " + str(keys_amount) + " keys")
            elif battle_inv == 5:
                return
            else:
                print(c.blocker)
                print(c.tno)
        except:
            print(c.blocker)
            print(c.tno)
    
#This function controls the usage of stamina potions
def s_pot_inv():
    global stamina
    global s_pot_num
    while battle == True:
        try:
            print(c.blocker)
            print("You have " + str(s_pot_num) + " Stamina Potions")
            print(" 1 - Yes\n 2 - No")
            s_pot_use = int(input("Would you like to use a stamina potion?\n: "))
            if s_pot_use == 1:
                if s_pot_num >= 1:
                    print(c.blocker)
                    print("You used a stamina potion!")
                    s_pot_num = s_pot_num - 1
                    stamina = stamina + 25
                else:
                    print(c.blocker)
                    print("You do not have a stamina potion!")
            elif s_pot_use == 2:
                return
            else:
                print(c.blocker)
                print(c.tno)
        except:
            print(c.blocker)
            print(c.tno)

#This function allows the user to flee the battle, ending it prematurely
def battle_flee_action():
    global stamina
    global battle
    print(c.blocker)
    print("You have fled the battle.")
    print("-5 stamina")
    stamina = stamina - 5
    battle = False

stamina = 100
battle = True  
monster = "Goblin"
battle_attack = 0

have_sword = True
have_bow = True
have_crossbow = False

sword_amount = 5
arrow_amount = 5

keys_amount = 2
s_pot_num = 3


while battle == True:
    weapon_checker()
    found_monster_actions()
    if battle_action == 1:
        battle_attack_action()
    elif battle_action == 2:
        battle_inventory_action()
    elif battle_action == 3:
        battle_flee_action()
