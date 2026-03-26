# label splashscreen:
#     scene black
#     with Pause(1)

#     show text "{size=60}A game by \n\nChristopher, & Elyze" with dissolve
#     with Pause(2)

#     hide text with dissolve
#     with Pause(1)

#     return

# The game starts here.


### Prologue ###
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
    pause (3.0)

    jump mountain_basecamp


label mountain_basecamp:
    scene bg mountain basecamp with dissolve
    $ renpy.notify("Mt. Mayumi Basecamp")
    $ quick_menu = True
    window show

    "The weather's today perfect but"
    "..."
    "Why am the only one climbing up this mountain today"
    "I hope I won't get lost"
    # A worn out poster of a missing girl suddenly get swept by the wind to you
    "Hmm... what's this?"
    # Add a menu as well to pick it and read it
    "A missing poster..."
    "It's barely holding on but some text are still readable"
    "Age 17, wearing uniform, name: Da..."
    "Da- whattt???"
    "Whatever her name was, I hope she's already found"
    "It's almost time, I need to leave soon"
    "Otherwise, I'll get down the mountain after sunset"

    menu start_trail:
        "What to do?"
        "Start trail":
            "My feet's ready to go, it's time to move"
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
    "This forest feels so tranquil, and serene"
    "I feel like I could just lay here forever"
    "Going on an adventure alone is bizzarre but quite a freeing experience"
    "I wonder why this mountain is not so polular"
    "Its time to move, which path should I take?"

    $ quick_menu = False
    window hide dissolve
    $ choice = renpy.call_screen("direction_menu_horizontal")
    
    if choice == "left":
        "I think this way is easier"
        scene black with eyeclose
        jump mountain_climb_grassyside_left

    elif choice == "right":
        "My gut feel says this"
        scene black with eyeclose
        jump mountain_climb_grassyside_right


label mountain_climb_grassyside_left:
    scene bg mountain climb grassyside-left with dissolve
    $ quick_menu = True
    window show

    "Just a little..."
    "*huff...*"
    "more..."
    "*huff...*"
    "That climb was harder than expected"
    "*huff...*"
    "I can already see the summit from here"
    "*huff...*"

    default rest_count = 0

    label rest_before_the_summit:
        menu:
            "What should I do?"
            "Reached for the summit":
                if rest_count >= 2:
                    "Its time to go. The summit is waiting for me!"
                    jump mountain_summit
                else:
                    $ rand = renpy.random.randint(1, 3)
                    if rand == 1:
                        "I could really use a break right now *huff...*"
                    elif rand == 2:
                        "Just five more minutes please! *huff...*"
                    elif rand == 3:
                        "Can I please get my well deserved break *huff...*"
                    jump rest_before_the_summit
            "Take a break":
                $ rest_count += 1
                if rest_count == 1:
                    "Yeah, that feels better..."
                    "This view is amazing, I should rest here a bit more"
                else:
                    "Alright I feel better now I should keep going!"
                jump rest_before_the_summit


label mountain_climb_grassyside_right:
    scene bg mountain climb grassyside-right with dissolve
    $ quick_menu = True
    window show

    "The hike from here is easier than expected"
    "It feels just like a light walk"
    "I should've taken the other way for more challenge"
    "The summit is near I should keep going"
    menu to_the_summit:
        "What to do?"
        "Reched for the summit":
            "I should not keep the mountain summit waiting"
            "It's time to go"
            jump mountain_summit
        "Admire the view for a while":
            "Resting is never a bad idea"
            "This view is stunning"
            $ quick_menu = False
            window hide
            pause
            $ quick_menu = True
            window show
            jump to_the_summit
        

label mountain_summit:
    scene bg mountain summit with dissolve
    "*huff..*"
    "Finally, I've reached the summit!!!"
    "I thought it would be bad if I reached the summit at sunset"
    "But seeing it like this, makes me feel that all that sweat I've poured on this hike was worth it"
    menu watch_the_sunset:
        "Look around"
        "Watch the sunset":
            "This is nothing but beautiful"
            "I'm glad to be able to see this"
            $ quick_menu = False
            window hide
            pause
            $ quick_menu = True
            window show
    "This was a beautiful sight to see"
    "I'm glad I did all this even I was alone"
    menu go_back_trail:
        "Where shall we go now?"
        "Go back down":
            "It was beautiful but it's time to go now"
            "I need to get to the basecamp before it gets dark. I gotta hurry"
            jump to_basecamp_forest
        "Watch the sunset again":
            "This view only comes once in a lifetime"
            "I'll stay here a bit more"
            $ quick_menu = False
            window hide
            pause
            $ quick_menu = True
            window show
            jump go_back_trail


label to_basecamp_forest:
    scene bg to basecamp forest

    default lost_count = 0

    if lost_count == 0:
        "Climbing down is a lot easier than going up"
        "Now which way is the path to camp again?"
    
    elif lost_count == 1:
        "Huh...?"
        "I've been this way before"
        "Whats happening?"
        "Wha-what do I do?"

    elif lost_count == 2:
        "Am I lost?"
        "Bu-but I just went here before"
        "Of course, I am in a forest everything looks the same"
        "The basecamp must be near now"

    elif lost_count == 3:
        "What the hell is wrong with this forest!"
        "Can you please just let me out!"
        "I am not going in cirles, Am I?"

    elif lost_count == 4:
        "*huff...*"
        "*gulp*"
        "Please let me out"
        "I swear I'll join tree planting activity monthly, and never litter any paper again"
        "This must be a dream"
    
    elif lost_count == 5:
        "There's no way out is there"
        "The sun already set"
        "It's so dark, I can barely see anything"
        "I am tired"
    
    elif lost_count == 6:
        "I am really going in circles"
        "I am really really tired"
        "*huff...*"
        "I should get some rest"
        jump dawn_first_meeting

    $ quick_menu = False
    window hide dissolve
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        if lost_count == 0:
            "This has to be it"
        $ lost_count += 1
        scene black with eyeclose
        jump lost_path_straight
    
    elif choice == "left":
        if lost_count == 0:
            "I think it's this way"
        $ lost_count += 1
        scene black with eyeclose
        jump lost_path_left

    elif choice == "right":
        if lost_count == 0:
            "It should be this way"
        $ lost_count += 1
        scene black with eyeclose
        jump lost_path_right
    

label lost_path_straight:
    scene bg lost forest straight with dissolve

    $ quick_menu = False
    window hide dissolve
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest
    
    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest


label lost_path_left:
    scene bg lost forest left

    $ quick_menu = False
    window hide dissolve
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest
    
    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest


label lost_path_right:
    scene bg lost forest right

    $ quick_menu = False
    window hide dissolve
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest
    
    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest


### Chapter 1 ###
label dawn_first_meeting:
    scene bg forest starry sky
    "This should be a good place to rest"
    "The stars are so bright, it's beautiful"
    ""


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