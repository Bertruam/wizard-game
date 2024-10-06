import random

creature = ["Goblin", "Skeleton", "Merman", "Brigand" , "Slime", "Ghoul", "Vampire", "Gnome", "Orc", "Mummy", "Elf", "Serpent", "Werewolf", "Ogre", "Cultist", "Wraith", "Troll", "Scarab", "Zombie", "Demon", "Lizardman"]
mon_adjective = ["Fearsome ", "Coniving ", "Horrendous ", "Nightmarish ", "Sultry ", "Obnoxious ", "Vicious ", "Deadly ", "Weird ",
                  "Fangorious ", "Grotesque ", "Diabolical ", "Drippy ", "Whimsical ", "Drunken ", "Stinky ", "Poorly Drawn ", "Flatulent ", "Raging ", "Bellowing ","Cunning "]

class Wizard:
    def __init__(self, name, title, job, school):
        self.name = name
        self.title = title
        self.job = job
        self.school = school
        self.true_name = f"{title} {name}, {job} of {school}"

class Monster:
    def __init__(self, threat):
        self.name = mon_adjective[random.randrange(0,len(mon_adjective))] + creature[random.randrange(0,len(creature))]
        self.threat = threat

class Game_Status:
    def __init__(self, z, y, x):
        self.health = z
        self.maxhealth = z
        self.score = y
        self.power = x
        self.r = 0