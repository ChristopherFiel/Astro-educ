# label splashscreen:
#     scene black
#     with Pause(1)

#     show text "{size=60}A game by \n\nChristopher, & Elyze" with dissolve
#     with Pause(2)

#     hide text with dissolve
#     with Pause(1)

#     return

# The game starts here.


label start:
    $ quick_menu = False
    window hide

    scene black with dissolve
    show screen disclaimer_screen with dissolve
    pause 5
    show screen press_to_continue with dissolve
    pause
    hide screen disclaimer_screen
    hide screen press_to_continue
    with dissolve

    show text "{font=cmunorm.ttf}{size=60}April 21, 2022\nMt. Mayumi Philippines{/size}{/font}" with dissolve
    pause (3.0)

    hide text with dissolve

    $ quick_menu = True
    window show

    scene bg mountain background with dissolve
    "Mt. Mayumi, it's so beautiful"
    "This will be my first time climbing a mountain"
    "It looks bigger than the pictures"
    "Take a deep breathe"
    "This is going to be hard but..."
    $ quick_menu = False
    window hide

    show text "{font=HowdyLemon.otf}{size=80}You can do this{/size}{/font}" with Dissolve(1.0)
    pause

    jump mountain_basecamp

label mountain_basecamp:
    scene bg mountain basecamp with dissolve
    $ renpy.notify("Mt. Mayumi Basecamp")
    $ quick_menu = True
    window show

    "The journey of a thousand miles begin wit a single step"
    "It seems like I'll be the only one climbing up this mountain today"
    "I hope I won't get lost"
    # A worn out poster of a missing girl suddenly get swept by the wind to you
    "Hmm... what's this?"
    # Add a menu as well to pick it and read it
    "A missing poster..."
    "It's barely holding on but some text are still readable"
    "Age 17, wearing uniform, name: Da..."
    "Da- whattt?"
    "Whatever her name was, I hope she's already found"
    "It's almost time, I need to leave soon"
    "Otherwise, I'll get down the mountain after sunset"

    menu start_trail:
        "What to do?"
        "Start trail":
            "Everything's now ready"
            "It's time to go"
            jump mountain_climb_rainforest
        "Stay for a while":
            "I still have time, no need to rush"
            "I'll rest for a while"
            $ quick_menu = False
            window hide
            pause
            $ quick_menu = True
            window show
            jump start_trail


label mountain_climb_rainforest:
    scene bg mountain climb rainforest with dissolve
    ""

label mountain_climb_rockyside:
    scene bg mountain climb rockyside with dissolve

label mountain_climb_grassyside:
    scene bg mountain climb grassyside with dissolve

label mountain_summit:
    scene bg mountain summit with dissolve



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
        $ player_name="Clementine"
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

    show Dawn pout
    d "Lets go"
    d "test"

    d "Where shall we go"
    hide Dawn with dissolve
    $ quick_menu = False
    window hide dissolve

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        d "Lets gooo!!!"
        scene black with eyeclose
        jump forest_north

    elif choice == "left":
        d "Lets gooo!!!"
        scene black with eyeclose
        jump forest_west

    elif choice == "right":
        d "Lets gooo!!!"
        scene black with eyeclose
        jump forest_east

    elif choice == "back":
        d "Lets gooo!!!"
        scene black with eyeclose
        jump forest_south


label forest_north:
    scene black with eyeclose
    show star_sky with eyeopen

    d "lets use the map"
    return

label forest_south:
    scene black with eyeclose
    show star_sky with eyeopen

    d "Lets use the map"
    return

label forest_east:
    scene black with eyeclose
    show star_sky with eyeopen

    d "lets use the map"
    return

label forest_west:
    scene black with eyeclose
    show star_sky with eyeopen

    d "Lets use the map"
    return

### Chapter 2: ###

# Chapter 3: Star trail, and Shooting Stars

### Chapter 4: At Dawn ###