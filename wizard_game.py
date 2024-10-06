import random
import os
import time

from wizard_classes import *
from wizard_text import *

game_title = """          _    __________________ _______  _______ _________ _______            _________ _______  _______  _______  ______    _________ _______           _______  _        _______          
|\     /|( \   \__   __/\__   __/(       )(  ___  )\__   __/(  ____ \  |\     /|\__   __// ___   )(  ___  )(  ____ )(  __  \   \__    _/(  ___  )|\     /|(  ____ )( (    /|(  ____ \|\     /|
| )   ( || (      ) (      ) (   | () () || (   ) |   ) (   | (    \/  | )   ( |   ) (   \/   )  || (   ) || (    )|| (  \  )     )  (  | (   ) || )   ( || (    )||  \  ( || (    \/( \   / )
| |   | || |      | |      | |   | || || || (___) |   | |   | (__      | | _ | |   | |       /   )| (___) || (____)|| |   ) |     |  |  | |   | || |   | || (____)||   \ | || (__     \ (_) / 
| |   | || |      | |      | |   | |(_)| ||  ___  |   | |   |  __)     | |( )| |   | |      /   / |  ___  ||     __)| |   | |     |  |  | |   | || |   | ||     __)| (\ \) ||  __)     \   /  
| |   | || |      | |      | |   | |   | || (   ) |   | |   | (        | || || |   | |     /   /  | (   ) || (\ (   | |   ) |     |  |  | |   | || |   | || (\ (   | | \   || (         ) (   
| (___) || (____/\| |   ___) (___| )   ( || )   ( |   | |   | (____/\  | () () |___) (___ /   (_/\| )   ( || ) \ \__| (__/  )  |\_)  )  | (___) || (___) || ) \ \__| )  \  || (____/\   | |   
(_______)(_______/)_(   \_______/|/     \||/     \|   )_(   (_______/  (_______)\_______/(_______/|/     \||/   \__/(______/   (____/   (_______)(_______)|/   \__/|/    )_)(_______/   \_/   
                                                                                                                                                                                              
an ultimate power simulator by Kiefer Noles                                                                                                                                                                                              \n\n\n"""

pos_cond = ["yes", "y", "yes", "yse"]
neg_cond = ["no", "n", "on"]

subtle_cond = ["subtlety", "subtlet", "subtle", "subtl", "subt", "sub", "su", "s"]
bomb_cond = ["bombast", "bombas", "bomba", "bomb", "bom", "bo", "b"]

#Game Class Objects
current_wizard = Wizard
current_foe = Monster
game_stat = Game_Status
#/Game Class Object

def die_roll(power):
    global game_stat
    result = 0
    log_pass = f"R{game_stat.r}>>"
    for x in range(power):
        add = random.randrange(1,6)
        log_pass += f"[{add}]"
        result += add
    log_pass += f": {result}"
    game_stat.r += 1
    dice_log(log_pass)
    return result

def threat_gen(power):
    result = 0
    for x in range(power):
        add = random.randrange(1,6)
        result += add
    if result == 1:
        result = 2
    if result == power * 6:
        result = power * 6 - 1
    return result

def dice_log(x):
    print(x)
    log = []
    log.append(x)

def wizard_maker():
    char_finished = False
    name_check = False
    title_check = False
    job_check = False
    school_check = False

    while char_finished != True:
        while name_check != True:
            name = input("What is your Wizard Name? ")
            name_in = input(f"{name}, is this correct? (Yes) or (N)o: ")
            if name_in.lower() in pos_cond:
                name_check = True
            elif name_in.lower() in neg_cond:
                print("Reset")
            else:
                print("<<Command Not Recognised>>")
        while title_check != True:
            title = input("What is your wizardly Title? ")
            title_in = input(f"{title}, is this correct? (Yes) or (N)o: ")
            if title_in.lower() in pos_cond:
                title_check = True
            elif title_in.lower() in neg_cond:
                print("Reset")
            else:
                print("<<Command Not Recognised>>")
        while job_check != True:
            job = input("What kind of wizard are you? ")
            job_in = input(f"{job}, is this correct? (Yes) or (N)o: ")
            if job_in.lower() in pos_cond:
                job_check = True
            elif job_in.lower() in neg_cond:
                print("Reset")
            else:
                print("<<Command Not Recognised>>")
        while school_check != True:
            school = input("What is your magical school of specialty? ")
            school_in = input(f"{school}, is this correct? (Yes) or (N)o: ")
            if school_in.lower() in pos_cond:
                school_check = True
            elif school_in.lower() in neg_cond:
                print("Reset")
            else:
                print("<<Command Not Recognised>>")
        final_in = input(f"You are {title} {name}, {job} of {school}. Is this correct? ")
        if final_in.lower() in pos_cond:
            char_finished = True

        print("Your journey to arcane mastery begins!")
        
    
    return Wizard(name, title, job, school)

def main():
    os.system('clear')
    print(game_title)
    menu()

def menu():
    print("Welcome to your Ultimate Wizard Journey!\n   1) New Game\n   2) Tutorial\n   3) High Scores\n   4) Quit\n")
    menu_check = False    
    while menu_check == False:
        menu_in = input("Please enter the number of the desired command: ")
        match menu_in:
            case "1":
                menu_check = True
                new_game()
            case "2":
                menu_check = True
                print(tutorial_text)
                menu()
            case "3":
                #menu_check = True
                print("High Scores Coming Soon")
                pass
            case "4":
                end_program()
            case _:
                print("Command Not Found")

def new_game():
    #make a new wizard
    global current_wizard
    global game_stat
    current_wizard = wizard_maker()
    game_stat = Game_Status(3,0,1) # Update for difficulty later
    game_loop()

def make_monster():
    global current_foe 
    current_foe = Monster(threat_gen(game_stat.power))

def game_loop():
    print(f"\nDay {game_stat.score + 1}\n")
    time.sleep(random.randrange(1, 3))
    make_monster()
    print(f"A {current_foe.name} {combat_text[random.randrange(len(combat_text))]} Its threat is {current_foe.threat}!")
    print("What will you do?")
    battle_check = False
    while battle_check != True:
        bat_input_check = False
        while bat_input_check != True:
            battle_in = input(">> ")
            if battle_in in subtle_cond:
                bat_input_check = True
                print("Subtlety...")
                battle_system(True)
            elif battle_in in bomb_cond:
                bat_input_check = True
                print("Bombast!")
                battle_system(False)
            elif battle_in == "status":
                status_check()

# returns current health, current score, current rerolls
def status_check():
    print(f"Status: Health - {game_stat.health}/{game_stat.maxhealth} Score - {game_stat.score}")
    pass

def entomb():
    pass #add dead character to a mortuary list

def game_over():
    obituary = f"{current_wizard.true_name} {game_over_text} {current_foe.name} on the {game_stat.score + 1} day of their journey!"
    print(obituary)
    #entomb(obituary)
    #high score check goes here
    menu()

def end_program():
    print("Fare thee well!")
    quit()

def power_increses():
    game_stat.power += 1
    print(power_increase_text)
    time.sleep(2)
    game_loop()

def battle_system(tact):
    checkem  = 0
    checkem = die_roll(game_stat.power)
    #subtlety
    if (tact == True and checkem < current_foe.threat) or (tact == False and checkem > current_foe.threat):
        victory()
    elif checkem == current_foe.threat:
        print("You clash spectacularly!")
    else:
        injury()

def victory():
    print(victory_text[random.randrange(len(victory_text))])
    game_stat.score += 1
    print("Current Score: " + str(game_stat.score))
    #if (game_stat.score // 10) == 0:
    #    power_increses()
    #else:
    game_loop()

def injury():
    print("Thou are harmed!")
    game_stat.health -= 1
    if game_stat.health <= 0:
        game_over()

main()
