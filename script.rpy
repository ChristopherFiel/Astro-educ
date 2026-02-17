# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Idk what to name Alice or Dawn
define a = Character("Alice", color="#f0f8ff")
    

transform bottom:
    xalign 0.5
    yalign 0.0

label splashscreen:
    scene black
    with Pause(1)

    show text "Fiel & Sarmiento presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# The game starts here.

label start:
    $ quick_menu = False
    window hide

    scene black
    with Pause(1)

    show text "{font=HowdyLemon.otf}{size=80}Somewhere in the southern hemisphere{/size}{/font}" with dissolve
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

label lost_in_forest:
    $ renpy.block_rollback()

    scene bg forest 1 with dissolve

    # Write dialogue that shows that the player is lost in the forest for hours
    # Indicate that the player don't bring that much of a supply
    # Indicate that the player seems to be going in circles
    # Indicate that the player notice something strange in the forest
    "Idk what to write here as well"
    "I'm lost"

    # Alice appears mysteriously 
    show Alice 
    "???" "Are you lost?"
    "???" "Oppss, sorry didn't mean to startle you hehe"
    "???" "By the way my name is Alice"
    a "How about you what's your name?"

    $ player_name = renpy.input("Input your name")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="#1 Netanyahu Hater"
    $ renpy.block_rollback()

    a "Nice to meet you %(player_name)s"
    a "Don't worry I am a hiker too"
    a "Eh?? so I guess you're indeed lost"
    a "Don't worry I know a way to navigate the forest without a compass or map"
    a "{size=80}Just...{/size}"

    hide Alice

    # Cinema, magnum opus, imdb 10/10, rotten tomato 100%, cannes film festival film of the year
    # Game of the year 2026, Oscars best cinematic, MMFF best film, 

    $ quick_menu = False
    window hide

    scene black
    with Pause(1)

    show text "{font=Midnightconstellations-YLgo.ttf}{size=160}Look Up{/size}{/font}"
    pause 

    hide text with dissolve
    with Pause(1)

    $ quick_menu = True
    window show

    jump star_map

label star_map:
    $ renpy.block_rollback()

    # Introduce the star map system

    scene bg star map

    a "Let me show you"

    return
