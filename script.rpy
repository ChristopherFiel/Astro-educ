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
    window auto

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

    scene bg mountain background with dissolve
    $ quick_menu = True
    "Mt. Mayumi, it's so beautiful"
    "This will be my first time climbing a mountain"
    "It looks bigger than the pictures"
    "Take a deep breathe"
    "This is going to be hard but..."
    $ quick_menu = False
    window hide

    show text "{font=HowdyLemon.otf}{size=80}You can do this{/size}{/font}" with Dissolve(1.0)
    pause (3.0)

    scene black with fade
    jump mountain_basecamp


label mountain_basecamp:
    scene bg mountain basecamp with dissolve
    show screen show_poster
    $ poster_examined = False
    $ quick_menu = True
    window hide
    
    "The weather's today perfect but..."
    "Why is there no one climbing up this mountain today??"
    "I hope I won't get lost"
    "Hmm... what's this?"
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
            hide screen show_poster with dissolve
            $ quick_menu = False
            jump mountain_climb_rainforest
        "Stay for a while":
            "I still have time, no need to rush"
            "I'll rest for a while"
            $ quick_menu = False
            window hide
            pause 1.0
            show screen press_to_continue with dissolve
            pause
            $ quick_menu = True
            window show
            hide screen press_to_continue
            jump start_trail


label mountain_climb_rainforest:
    scene black with arrow_wipe_down_slow
    scene bg mountain climb rainforest with arrow_wipe_down_slow
    $ quick_menu = True
    "This forest feels so tranquil, and serene"
    "I feel like I could just lay here forever"
    "Going on an adventure alone is bizzarre but quite a freeing experience"
    "I wonder why this mountain is not so polular"
    "Its time to move, which path should I take?"

    $ quick_menu = False
    window hide
    $ choice = renpy.call_screen("direction_menu_horizontal")
    
    if choice == "left":
        $ quick_menu = True
        "I think this way is easier"
        jump mountain_climb_grassyside_left

    elif choice == "right":
        $ quick_menu = True
        "My gut feel says this"
        jump mountain_climb_grassyside_right


label mountain_climb_grassyside_left:
    scene black with arrow_wipe_right_slow
    scene bg mountain climb grassyside-left with arrow_wipe_right_slow
    $ quick_menu = True

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
    scene black with arrow_wipe_left_slow
    scene bg mountain climb grassyside-right with arrow_wipe_left_slow
    $ quick_menu = True
    window auto

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
            jump to_the_summit
        

label mountain_summit:
    scene black with arrow_wipe_down_slow
    scene bg mountain summit with arrow_wipe_down_slow
    $ quick_menu = True
    window auto

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
            pause 1.0
            show screen press_to_continue with dissolve
            pause
            hide screen press_to_continue
            $ quick_menu = True
            window auto
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
            pause 1.0
            show screen press_to_continue with dissolve
            pause
            hide screen press_to_continue
            $ quick_menu = True
            jump go_back_trail


label to_basecamp_forest:
    scene black with arrow_wipe_up_slow
    scene bg to basecamp forest with arrow_wipe_up_slow

    default lost_count = 0
    if lost_count == 0:
        $ quick_menu = True
        window auto
        "Climbing down is a lot easier than going up"
        "Now which is the way to the camp again?"
    elif lost_count == 1:
        $ quick_menu = True
        window auto
        "Huh...?"
        "Am I lost?"
        "But I just went here before"
        "O-o-of course, I am in a forest everything looks the same"
        "The basecamp must be near now"
    elif lost_count == 2:
        $ quick_menu = True
        window auto
        "Wha-what's happening?"
        "I've been this way before"
        "I am not going in circles, Am I?"
        "Is this a prank or something. You can stop now cuz it's not FUNNY!!"
        "What the hell is wrong with this forest!"
    elif lost_count == 3:
        $ quick_menu = True
        window auto
        "*huff...*"
        "*gulp*"
        "Can you please just let me out!"
        "I swear I'll join tree planting activity monthly, and never litter any paper again"
        "I promise I'll save energy, save water, go vegan, just please..."
    elif lost_count == 4:
        $ quick_menu = True
        window auto
        "Is there even a way out?"
        "There's no way out is there"
        "What do I even do?"
        "It's getting dark, and I'm tired"
        "What do I do? What do I do? What do I do?"
    elif lost_count == 5:
        $ quick_menu = True
        window auto
        "I am really going in circles"
        "I am really really tired"
        "*huff...*"
        "I should get some rest"
        scene black with fade
        jump dawn_first_meeting

    $ quick_menu = False
    window hide
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        if lost_count == 0:
            "This has to be it"
        $ lost_count += 1
        scene black with arrow_wipe_up
        jump lost_path_straight

    elif choice == "left":
        if lost_count == 0:
            "I think it's this way"
        $ lost_count += 1
        scene black with arrow_wipe_right
        jump lost_path_left

    elif choice == "right":
        if lost_count == 0:
            "It should be this way"
        $ lost_count += 1
        scene black with arrow_wipe_left
        jump lost_path_right


label lost_path_straight:
    scene bg lost forest straight with arrow_wipe_up
    $ quick_menu = False
    window hide
    pause 1.0

    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with arrow_wipe_up
    elif choice == "left":
        scene black with arrow_wipe_right
    elif choice == "right":
        scene black with arrow_wipe_left

    jump to_basecamp_forest


label lost_path_left:
    scene bg lost forest left with arrow_wipe_right
    $ quick_menu = False
    window hide
    pause 1.0

    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with arrow_wipe_up
    elif choice == "left":
        scene black with arrow_wipe_right
    elif choice == "right":
        scene black with arrow_wipe_left

    jump to_basecamp_forest


label lost_path_right:
    scene bg lost forest right with arrow_wipe_left
    $ quick_menu = False
    window hide
    pause 1.0

    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        scene black with arrow_wipe_up
    elif choice == "left":
        scene black with arrow_wipe_right
    elif choice == "right":
        scene black with arrow_wipe_left

    jump to_basecamp_forest


### Chapter 1 ###
label dawn_first_meeting:
    scene bg forest starry sky with dissolve

    $ quick_menu = True
    window auto

    "This should be a good place to rest"
    "The sun already set"
    "The stars are so bright"
    "I hope when I close my eyes I wake up from this nightmare"

    scene black with eyeclose
    pause 2.0
    d_unknown "psst... hey"
    d_unknown "Yohoooo, can you hear me? I'm talking to you"
    d_unknown "Are you still alive"
    d_unknown "Come on don't give up now, open your eyes"
    scene bg forest starry sky with eyeopen

    show Dawn surprised
    d_unknown "Woah! You're alive"
    d_unknown "I'm sorry I didn't mean to wake you up"
    d_unknown "But I get scared when you lay down I thought you were dying"
    show Dawn normal2
    d_unknown "Oppsss... I talked to much. I forget to tell you my name"
    show Dawn normal
    d_unknown "My name is Dawn"
    d "How about you, can you tell me your name?"

    $ player_name = renpy.input("{size=40}Enter your name{/size}")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Clementine"
    
    show Dawn smile
    d "%(player_name)s wow what a beautiful name"
    show Dawn normal
    d "Don't worry, I am not a monster. I'm not gonna eat you or something"
    show Dawn surprised
    d "I was just passing by and noticed you are running around in circles in the forest"
    d "Perhaps you are lost are you?"
    menu optional_name:
        "Yeah":
            pass
        "...":
            pass
    show Dawn normal2
    d "I see..."
    d "Well you are lucky! It might not look like it, but I'll tell you anyway"
    d "I am an seasoned mountaineer with years of experince"
    show Dawn normal
    d "You are not good at navigating directions aren't you?"
    d "Don't worry I know a way to navigate this forest without a compass"
    show Dawn smile
    d "{size=60}Just...{/size}"

    scene black with fade
    jump star_map

label star_map:
    $ quick_menu = False
    window hide
    show map at zoom_to(0.5, 0.4, 1.8)
    pause 1.0

    show text "{font=Midnightconstellations-YLgo.ttf}{size=240}Look Up{/size}{/font}"
    pause (3.0)
    hide text
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Chapter 1: \n Dawn at Sunset{/size}{/font}"
    pause (3.0)
    hide text 

    d "The stars are pretty aren't they?"
    d "But they are not only pretty, we can use them to get out of this forest"
    d "Let me show you"

    show map at pan_to(0.5, 0.0, 1.8, 0.2)
    pause 1.0
    d "This is how you navigate using big dipper"
    d "Look at the Big Dipper up here"

    show map at pan_to(1.0, 0.5, 1.8, 0.4)
    pause 1.0
    d "This is how you navigate using orion"

    show map at pan_to(0.5, 1.0, 1.8, 0.4)
    pause 1.0
    d_top "This is how you navigate using crux"
    d_top "And that's everything you need to know."

    jump to_basecamp_forest_with_dawn


label to_basecamp_forest_with_dawn:
    $ time_of_day = "NIGHT"
    scene black with eyeclose
    scene bg to_basecamp_forest with eyeopen

    if not forest_intro_seen:
        $ quick_menu = True
        window auto
        show screen gameUI
        show Dawn normal with dissolve
        d "I hope you learned something new"
        show Dawn normal2
        d "Now, I know a mountaineer camp near us"
        d "Let's head over there now I think it's about..."
        d "{size=60}North East{/size} from here"
        show Dawn normal
        d "Well, I'll be heading first"
        d "See Yah!"
        hide Dawn with dissolve
        "Dawn disappeared like a dust in the wind"
        player_name "Well, She seems trustworthy. I should follow her"
        $ forest_intro_seen = True
    else:
        $ forest_mistakes += 1
        call forest_wrong_dialogue
    
    $ quick_menu = False
    window hide

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with eyeclose
        jump forest_north
        player_name ""

    elif choice == "left":
        scene black with eyeclose
        jump forest_west

    elif choice == "right":
        scene black with eyeclose
        jump forest_east

    elif choice == "back":
        scene black with eyeclose
        jump forest_south


label forest_north:
    scene bg forest north with dissolve
    show screen gameUI

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "right":
        scene black with eyeclose
        jump forest_camp

    elif choice == "back":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn


label forest_south:
    scene bg forest south with dissolve
    show screen gameUI

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "back":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn


label forest_east:
    scene bg forest east with dissolve
    show screen gameUI

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "left":
        scene black with eyeclose
        jump forest_camp

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "back":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn


label forest_west:
    scene bg forest west with dissolve
    show screen gameUI

    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "left":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "right":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn

    elif choice == "back":
        scene black with eyeclose
        jump to_basecamp_forest_with_dawn
    

label forest_camp:
    scene bg forest camp with dissolve

    $ quick_menu = True
    window auto
    show screen gameUI

    d "Waowww"


### Chapter 2: ###

# Chapter 3: Star trail, and Shooting Stars

### Chapter 4: At Dawn ###