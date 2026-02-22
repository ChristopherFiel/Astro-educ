# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# Idk what to name Alice or Dawn
define a = Character("Dawn", image="sprites/Dawn", color="#e6cc90")

# Transforms/transitions for expressions/blinks
define config.say_attribute_transition = Dissolve(0.1)
# Randomize blinking time
transform blinkwait:
    choice:
        6.0
    choice:
        5.0
    choice:
        4.0
    choice:
        2.0

#Blinking Character Images
image Dawn normal:
    zoom 1.5
    "sprites/Dawn/Dawn_normal.png"
    blinkwait
    "sprites/Dawn/Dawn_normal_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_normal.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn normal2:
    zoom 1.5
    "sprites/Dawn/Dawn_normal2.png"
    blinkwait
    "sprites/Dawn/Dawn_normal2_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_normal2.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn lookaway:
    zoom 1.5
    "sprites/Dawn/Dawn_lookaway.png"
    blinkwait
    "sprites/Dawn/Dawn_lookaway_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_lookaway.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn surprised:
    zoom 1.5
    "sprites/Dawn/Dawn_surprised.png"
    blinkwait
    "sprites/Dawn/Dawn_surprised_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_surprised.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn pout:
    zoom 1.5
    "sprites/Dawn/Dawn_pout.png"
    blinkwait
    "sprites/Dawn/Dawn_pout_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_pout.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn smile:
    zoom 1.5
    "sprites/Dawn/Dawn_smile.png"
    blinkwait
    "sprites/Dawn/Dawn_smile_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_smile.png" with Dissolve(0.1)
    0.1
    repeat


# Splashscreen to show before main menu

label splashscreen:
    scene black
    with Pause(1)

    show text "{size=40}Fiel & Sarmiento presents...{/size}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# The game starts here.

label start:
    $ quick_menu = False
    window hide

    scene black with dissolve
    with Pause(1)

    show text "{font=HowdyLemon.otf}{size=60}Somewhere in the northern hemisphere{/size}{/font}" with dissolve
    pause 

    hide text with dissolve
    with Pause(1)

    $ quick_menu = True 
    window show

    # Change the bg mountain top to a stylize real life image when you have time
    scene bg mountain top with dissolve

    # The scenario is the player is talking to himself admiring the view at the
    # mountain top, after that he needs to go down now
    # it's sunset at the mountain summit

    "Idk what to write here"

    "What a great view!!!"

    "Well it's time to go home now!"

    jump lost_in_forest

# Chapter 1: Dawn at Sunset

label lost_in_forest:
    $ renpy.block_rollback()

    scene bg forest 1 with dissolve

    # Write dialogue that shows that the player is lost in the forest for hours
    # Indicate that the player don't bring that much of a supply
    # Indicate that the player seems to be going in circles
    # Indicate that the player notice something strange in the forest
    "Idk what to write here as well"
    "I'm lost"

    # Dawn appears mysteriously 
    show Dawn normal 
    "???" "Are you lost?"
    "???" "Oppss, sorry didn't mean to startle you hehe"
    "???" "By the way my name is Dawn"
    a "How about you what's your name?"

    $ player_name = renpy.input("Type your name")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="#1 Netanyahu Hater"
    $ renpy.block_rollback()

    a "Nice to meet you %(player_name)s"
    a "Don't worry I am a hiker too"
    a "Eh?? so I guess you're indeed lost"
    a "Don't worry I know a way to navigate the forest without a compass or map"
    a "Just... Look Up"

    hide Dawn

    # Cinema, magnum opus, imdb 10/10, rotten tomato 100%, cannes film festival film of the year
    # Game of the year 2026, Oscars best cinematography, MMFF best film,
    # 2026 NBA Champions & finals MVP, 2026 Anime of the year, 
    # MAMA Song of the year, Peak fiction, kino has been served

    $ quick_menu = False
    window hide

    scene black with dissolve
    with Pause(1)

    show text "{font=HowdyLemon.otf}{size=60}Chapter 1: Dawn at Sunset{/size}{/font}" with dissolve
    pause 

    hide text with dissolve
    with Pause(1)

    $ quick_menu = True
    window show

    jump star_map

label star_map:
    # $ renpy.block_rollback()

    scene bg map with dissolve

    a "Let me show you"

    jump lost_in_forest_2

label lost_in_forest_2:
    # $ renpy.block_rollback()

    scene bg forest 1 with dissolve

    show screen gameUI
    "The game UI is apprearing."
    "test2"

    show Dawn pout
    a "Lets go"
    a "test"

    menu:
        a "Where shall we go?"
        "Straight ahead":
            a "Ok"
            return
        "Let's stay":
            a "aight"
            return

label lost_in_forest_3:

# Chapter 2: Midnight Challenge

# Chapter 3: Star trail, and Shooting Stars

# Chapter 4: At Dawn