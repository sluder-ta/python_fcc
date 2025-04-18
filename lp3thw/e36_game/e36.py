from sys import exit

def treasure_room():
    print("""
                  ___
                  `. \\
                    \_)
    ____ _,..OOO......\...OOO-...._ ___
  .`    '_.-(  9``````````P  )--...)   `.
 ` ((     `  || __         ||   `     )) `
(          ) |<`  ````---__||  (          )
 `        `  ||) ,xx  xx.  //)__`        `  
  `-____-`   ,/  O`  O`   //,'_ )`-____-` 
           ,/     ,,     //  |//
          /      ((          //
         (   (._    _,)     (_) -OH YEAH!
          \    \````/        /
           \    ^--^        /
            \_   _____   __/
              | |     | |
             (   )   (   )
           ,--'~'\   /'~'--,
          (_______) (_______)dwb
    _ __ ___  ___  _        ___  _  ___
   | / /| . || . || |  ___ | . || || . \\
   |  \ | | || | || |_|___||   || || | |
   |_\_\`___'`___'|___|    |_|_||_||___/
            __ __  ___  _ _  _ 
           |  \  \| . || \ || |
           |     ||   ||   ||_/
           |_|_|_||_|_||_\_|<_>

""")

def dungeon_entrance_right():
    print("When you walk this direction you notice two things quite quickly:")
    print("1. It smells strongly of foot odor.")
    print("2. The air becomes more humid.")
    print("...\n" * 5, end = " ")
    print("You realize you're back in your middle school locker room - or at least an exact replica of it.")
    print("Standing in front of you is ol' biggus dingus, the bully that teased you relentlessly.")
    print("What do you do?")
    print("1. Finally stand up to him and tell him what you really think of him!")
    print("2. You finally fight back since you're bigger than he is now!")
    print("3. Calmly walk past this appparition.")
    choice = int(input("> "))
    
    if choice:
        choice = int(choice)
        if choice == 1:
            print("You're pathetic. You must let go of the past.")
            dungeon_entrance_right()
        elif choice == 2:
            print("You're pathetic. You want to beat up a tween-ager?")
            dungeon_entrance_right()
        elif choice == 3:
            print("This is clearly the right choice.")
            mirror_room()
        else:
            death()
    else:
        death()

def dungeon_entrance_left():
    return

def frog_wizard_lair():
    print("""
                             .-----.
                            /7  .  (
                           /   .-.  \\
                          /   /   \  \\
                         / `  )   (   )
                        / `   )   ).  \\
                      .'  _.   \_/  . |
     .--.           .' _.' )`.        |
    (    `---...._.'   `---.'_)    ..  \\
     \            `----....___    `. \  |
      `.           _ ----- _   `._  )/  |
        `.       /"  \   /"  \`.  `._   |
          `.    ((O)` ) ((O)` ) `.   `._\\
            `-- '`---'   `---' )  `.    `-.
               /                  ` \      `-.
             .'                      `.       `.
            /                     `  ` `.       `-.
     .--.   \ ===._____.======. `    `   `. .___.--`     .''''.
    ' .` `-. `.                )`. `   ` ` \          .' . '  8)
   (8  .  ` `-.`.               ( .  ` `  .`\      .'  '    ' /
    \  `. `    `-.               ) ` .   ` ` \  .'   ' .  '  /
     \ ` `.  ` . \`.    .--.     |  ` ) `   .``/   '  // .  /
      `.  ``. .   \ \   .-- `.  (  ` /_   ` . / ' .  '/   .'
        `. ` \  `  \ \  '-.   `-'  .'  `-.  `   .  .'/  .'
          \ `.`.  ` \ \    ) /`._.`       `.  ` .  .'  /
           |  `.`. . \ \  (.'               `.   .'  .'
        __/  .. \ \ ` ) \                     \.' .. \__
 .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
(_________.-====' / .' /\_)`--..__________..-- `====-. _________)
""")
    return

def mirror_room():
    print("""
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
""")

def mimic_room():
    print("""
        _____
    .-,;=_;_),-.
     \_\(),()/_/
       (,___,)
      ,-/`~`\-,___
     / /).:.('--._)
    {_[ (_,_)
        | Y |
       /  |  \\
       ... ...
""")


def start():
    print("""
WELCOME TO:

  sSSSs   d        sSSSs   d ss.  Ss   sS      d    d   sSSSs   d      d sss  
 S     S  S       S     S  S    b   S S        S    S  S     S  S      S      
S         S      S       S S    P    S         S    S S       S S      S      
S         S      S       S S sS'     S         S sSSS S       S S      S sSSs 
S    ssSb S      S       S S   S     S         S    S S       S S      S      
 S     S  S       S     S  S    S    S         S    S  S     S  S      S      
  "sss"   P sSSs   "sss"   P    P    P         P    P   "sss"   P sSSs P sSSss
""")
    
    print("Will you find glory in the hole?")
    print("What would you like to do?")
    print("1. Play the game.")
    #print("2. Add a level.")
    choice = int(input("> "))

    if choice == 1:
        play_game()
    else:
        exit(0)

def play_game():
    print("You've approached the cursed well just outside of town and notice that for the first time in recent memory the rope has been replaced.")
    print("It looks new enough and strong enough to support someone to travel down to the bottom of the well.")
    print("You begin your descent into the darkness below.")
    
    for i in range(0,4):
        print("_")
        print("__")
        print("___")
        print("__")
        print("_")
    
    print("When you reach the bottom of the well, you notice there is a path that forks.")
    print("Do you go to the right or to the left?")
    choice = input("> ")

    if "left" in choice:
        dungeon_entrance_left()
    elif "right" in choice:
        dungeon_entrance_right()
    else:
        death()


def death():
    print("You hear a snap just before you fall unconscious. Good night.")
    exit(0)

start()