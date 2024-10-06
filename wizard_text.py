#test for the main menu tutorial
tutorial_text = """
Welcome to the Tutorial!\n

When you begin the game you will be aske to create a wizard with the following information:
    * The Name of your wizard (Tim, Baldomere, Hershel, etc.)
    * Your wizarldy Title (Lord, Master, Carney, Stinky, etc.)
    * What kind of Spellcaster you are (Wizard, Warlock, Witch, Shaman, Pyromancer, etc.)
    * What School of magic you practice (Chronomancy, Storm Magic, Yogurtomancy, etc.)

    After that, you will begin your journey to battle dangerous foes around the world.

    Each foe will have Threat that you must overcome with either of two options: Subtlety or Bombast
    You will roll an amount of dice equal to you Power Level, comparing the result to the foe's threat and your choice.

    Subtlety is the act of using you arcane might to trick, circumvent, or otherwise outhink your foe.
    For Subltety to work you must roll LOWER than the foe's Threat.

    Bombast is the act of making a grand display of your might to blast, remove, or scare off a foe.
    For Bombast to work you must roll Higher than the foe's Threat.

    If you are correct you will grow stronger and proceed on you journey.

    If you are incorrect you will be harmed by the foe and continue the battle.
    Being reduced to zero Health is the end of your wizard's journey.

    After every tenth foe, you raise in power level and regain one health up to your maximum.

    You are now ready to journey forth, powerful master of magics. Go forth and inscribe your name on the legend of this world!
"""

#text that displays when the player loses.
game_over_text = "hath been slain by"

#text that displays how a foe approaches the wizard.
combat_text = ["approaches menacingly!",
               "bounds in from the shadows!",
               "slinks seductively towards you!",
               "howls in from the night sky!",
               "wriggles eerily in your direction!",
               "is just kinda hangin' around.",
               "gesticulates in a way to indicate threats!",
               "rushes at you from the murk!",
               "jumps out of a picture book you got from your local library!",
               "appears one layer at a time as if by some three dimensional printing device!",
               "sneaks in via a cunning disguise!",
               "is the prize in your box of cereal!",
               "emerges from a nearby mirror!",
               "is summoned by some mindless flunkies!",
               "is accidentally conjured while you were trying to pronounce 'Worchestershire'!",
               "glides in like it thinks its cool or something!",
               "is playing the bongos terribly!",
               "just stole your parking spit!",
               "called your latest thesis 'Trite!'",
               "spilled its drink all over you and refused to apologize!"
               ]

victory_text = ["Thou arest mighty!",
                "Victory is yours",
                "You made them 'Splode!",
                "Your Power is overwhelming!",
                "An Wizard is you!",
                "You have fabulous secret powers!",
                "Zounds! What a display of prowess!",
                "Huzzah! This foe is bested!",
                "Aw heck, you just straight up killed that guy, my dude!",
                "Well, hot dog!",
                "Hey, why hasn't my check cleared yet?"]

power_increase_text = f"You grow even mightier!\n\nBut be warned, stronger foes will rise to meet you on the feild of battle!\n\n"