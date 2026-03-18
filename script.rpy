# label splashscreen:
#     scene black
#     with Pause(1)

#     show text "{size=60}A game by \n\nFiel, Sarmiento, & Friends{/size}" with dissolve
#     with Pause(2)

#     hide text with dissolve
#     with Pause(1)

#     return

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

    $ time_of_day = 'DUSK'
    scene bg mountain top with dissolve

    # The scenario is the player is talking to himself admiring the view at the
    # mountain top, after that he needs to go down now
    # it's sunset at the mountain summit

    "Idk what to write here"

    "What a great view!!!"

    "Well it's time to go home now!"

    show Dawn surprised

    d "Hi"

    jump lost_in_forest

label mountain_climb:
    return


### Chapter 1: Dawn at Sunset ###
label lost_in_forest:
    $ time_of_day = 'DAY'
    scene black with eyeclose
    scene bg mountain top with eyeopen

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
    d "How about you what's your name?"

    $ player_name = renpy.input("Type your name")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="#1 Netanyahu Hater"
    # $ renpy.block_rollback()

    d "Nice to meet you %(player_name)s"
    d "Don't worry I am a hiker too"
    d "Eh?? so I guess you're indeed lost"
    d "Don't worry I know a way to navigate the forest without a compass or map"
    d "Just... Look Up"

    hide Dawn

    # Cinema, magnum opus, imdb 10/10, rotten tomato 100%, cannes film festival film of the year

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
    # Dawn will teach the player how to read the map
    
    scene black with eyeclose
    show star_sky with eyeopen

    d "Let me show you"

    scene black with eyeclose
    show big_dipper_tutorial with eyeopen

    d "This is how you navigate using big dipper"

    scene black with eyeclose
    show orion_tutorial with eyeopen

    d "This is how you navigate using orion"

    scene black with eyeclose
    show map with eyeopen

    d "This is how you navigate using crux"

    jump lost_in_forest_2


label lost_in_forest_2:
    $ time_of_day = "NIGHT"

    scene black with eyeclose
    scene bg park at resizer with eyeopen
    
    show screen gameUI
    "The game UI is apprearing."
    "test2"

    show Dawn pout
    d "Lets go"
    d "test"

    d "Where shall we go"
    hide Dawn with dissolve
    $ quick_menu = False
    window hide dissolve

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        d "Ok"
        return

    elif choice == "left":
        d "aight"
        scene black with eyeclose
        jump lost_in_forest_3

    elif choice == "right":
        d "Ok"
        return

    elif choice == "back":
        d "aight"
        scene black with eyeclose
        jump lost_in_forest_3


label lost_in_forest_3:
    d "Go back to menu"
    return

### Chapter 2: ###

# Chapter 3: Star trail, and Shooting Stars

### Chapter 4: At Dawn ###