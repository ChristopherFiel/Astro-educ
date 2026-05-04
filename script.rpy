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
    $ renpy.music.stop(channel="music", fadeout=1.0)
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
    p "Mt. Mayumi, it's so beautiful"
    p "This will be my first time climbing a mountain"
    p "It looks bigger than the pictures"
    p "Take a deep breathe"
    p "This is going to be hard..."
    $ quick_menu = False
    window hide

    show text "{font=HowdyLemon.otf}{size=80}You can do this{/size}{/font}" with Dissolve(1.0)
    pause (3.0)

    scene black with fade
    jump mountain_basecamp


label mountain_basecamp:
    scene bg mountain basecamp with dissolve
    # show screen show_poster
    $ poster_examined = False
    $ quick_menu = True
    window hide
    
    p "The weather's today perfect but..."
    p "Why is there no one climbing up this mountain today??"
    p "I hope I won't get lost"
    # p "Hmm... what's this?"
    # p "A missing poster..."
    # p "It's barely holding on but some text are still readable"
    # p "Age 17, wearing uniform, name: Da..."
    # p "Da- whattt???"
    # p "Whatever her name was, I hope she's already found"
    p "It's almost time, I need to leave soon"
    p "Otherwise, I'll get down the mountain after sunset"

    menu start_trail:
        p "What to do?"
        "Start trail":
            p "My feet's ready to go, it's time to move"
            hide screen show_poster with dissolve
            $ quick_menu = False
            jump mountain_climb_rainforest
        "Stay for a while":
            p "I still have time, no need to rush"
            p "I'll rest for a while"
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
    p "This forest feels so tranquil, and serene"
    p "I feel like I could just lay here forever"
    p "Going on an adventure alone is bizzarre but quite a freeing experience"
    p "I wonder why this mountain is not so polular"
    p "Its time to move, which path should I take?"

    $ quick_menu = False
    window hide
    $ choice = renpy.call_screen("direction_menu_horizontal")
    
    if choice == "left":
        $ quick_menu = True
        p "I think this way is easier"
        jump mountain_climb_grassyside_left

    elif choice == "right":
        $ quick_menu = True
        p "My gut feel says this"
        jump mountain_climb_grassyside_right


label mountain_climb_grassyside_left:
    scene black with arrow_wipe_right_slow
    scene bg mountain climb grassyside-left with arrow_wipe_right_slow
    $ quick_menu = True

    p "Just a little..."
    p "*huff...*"
    p "more..."
    p "*huff...*"
    p "That climb was harder than expected"
    p "*huff...*"
    p "I can already see the summit from here"
    p "*huff...*"

    default rest_count = 0

    label rest_before_the_summit:
        menu:
            p "What should I do?"
            "Reached for the summit":
                if rest_count >= 2:
                    p "Its time to go. The summit is waiting for me!"
                    jump mountain_summit
                else:
                    $ rand = renpy.random.randint(1, 3)
                    if rand == 1:
                        p "I could really use a break right now *huff...*"
                    elif rand == 2:
                        p "Just five more minutes please! *huff...*"
                    elif rand == 3:
                        p "Can I please get my well deserved break *huff...*"
                    jump rest_before_the_summit
            "Take a break":
                $ rest_count += 1
                if rest_count == 1:
                    p "Yeah, that feels better..."
                    p "This view is amazing, I should rest here a bit more"
                else:
                    p "Alright I feel better now I should keep going!"
                jump rest_before_the_summit


label mountain_climb_grassyside_right:
    scene black with arrow_wipe_left_slow
    scene bg mountain climb grassyside-right with arrow_wipe_left_slow
    $ quick_menu = True
    window auto

    p "The hike from here is easier than expected"
    p "It feels just like a light walk"
    p "I should've taken the other way for more challenge"
    p "The summit must be near now"
    menu to_the_summit:
        p "What to do?"
        "Reched for the summit":
            p "I should not keep the mountain summit waiting for me"
            p "It's time to go"
            jump mountain_summit
        "Take a rest":
            p "Maybe I could rest here for a while"
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

    p "*huff..*"
    p "Finally, I've reached the summit!!!"
    p "WAOOOOOOOOOOOWWW!!!"
    p "I did not now that it would be this beautiful"
    p "All that sweat I've poured on this hike was so worth it!"
    p "This sunset is just beautiful..."
    $ quick_menu = False
    window hide
    pause 1.0
    show screen press_to_continue with dissolve
    pause
    hide screen press_to_continue
    $ quick_menu = True
    window auto
    p "This was a wonderful sight to see, but I should keep going now"
    menu go_back_trail:
        "Where shall we go now?"
        "Go back down":
            p "I'll head down now. I need to get to the basecamp before it gets dark"
            p "I gotta hurry"
            jump to_basecamp_forest
        "Watch the sunset again":
            p "Hmm... maybe I got more time"
            p "I'll stay here a bit more, and enjoy the view"
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
        p "Climbing down is a lot easier than going up"
        p "Now which is the way to the camp again?"
    elif lost_count == 1:
        $ quick_menu = True
        window auto
        p "Huh...?"
        p "Am I lost?"
        p "But I just went here before"
        p "O-o-of course, I am in a forest everything looks the same"
        p "The basecamp must be near now"
    elif lost_count == 2:
        $ quick_menu = True
        window auto
        p "Wha-what's happening?"
        p "I've been this way before"
        p "I am not going in circles, Am I?"
        p "Is this a prank or something. You can stop now cuz it's not FUNNY!!"
        p "What the hell is wrong with this forest!"
    elif lost_count == 3:
        $ quick_menu = True
        window auto
        p "*huff...*"
        p "*gulp*"
        p "*puff...*"
        p "Get me out of this FOREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n
        EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        p "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        p"EEEEEEEEEEST!!!"
        p "please"
    elif lost_count == 4:
        $ quick_menu = True
        window auto
        p "Is there even a way out?"
        p "There's no way out is there"
        p "What do I even do?"
        p "It's getting dark, and I'm tired"
        p "What do I do? What do I do? What do I do?"
    else:
        $ quick_menu = True
        window auto
        p "I am really going in circles"
        p "I am really really tired"
        p "*huff...*"
        p "I should get some rest"
        jump dawn_first_meeting

    $ quick_menu = False
    window hide
    $ choice = renpy.call_screen("direction_menu_no_map")

    if choice == "straight":
        if lost_count == 0:
            p "This has to be it"
        $ lost_count += 1
        scene black with arrow_wipe_up
        jump lost_path_straight

    elif choice == "left":
        if lost_count == 0:
            p "I think it's this way"
        $ lost_count += 1
        scene black with arrow_wipe_right
        jump lost_path_left

    elif choice == "right":
        if lost_count == 0:
            p "It should be this way"
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
    scene black with fade
    scene bg forest starry sky with dissolve

    $ quick_menu = True
    window auto

    p "This should be a good place to rest"
    p "The sun's already out"
    p "The stars are so bright"
    p "I hope when I close my eyes I wake up from this nightmare"

    scene black with eyeclose
    pause 2.0
    d_unknown "psst... hey"
    d_unknown "Yohoooo, can you hear me? I'm talking to you"
    d_unknown "Are you still alive?"
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
    p "Oh yeah, my name is..."

    $ player_name = renpy.input("{size=40}Enter your name{/size}")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Podziemski is garbage"
    
    show Dawn smile
    d "%(player_name)s wow what a beautiful name"
    show Dawn normal
    d "Don't worry, I am not a monster. I'm not gonna eat you"
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

    jump forest_stargazing

label forest_stargazing:
    scene black with fade
    scene bg forest starry sky with dissolve
    pause 1.0
    $ quick_menu = True

    show Dawn normal with dissolve
    d "The stars are pretty, aren't they?"
    d "But they are not only pretty, we can use them to get out of this forest."
    d "Let me show you."

    player_name "But honestly, how can stars help you navigate? How does it serve as a map?"

    show Dawn smile
    d "Oh, I'll explain it to you. Stars kasi form images in the night sky, and that is what we call constellations."
    d "Common, let's look up. Did you see that star? That star is the North Star."
    
    show Dawn normal
    d "Wait, let me get my laser."
    player_name "Woah, a laser??"
    d "I use it to point things at the night sky and also this has a flashlight, so it's dual purpose. Very handy for night treks like this."
    player_name "Why do you need it though?"
    
    show Dawn smile  
    d "I always go here and I use this to point to stars accurately. Like for example..."
    # BIG DIPPER / NORTH SECTION
    scene black with eyeclose
    show map at pan_to(0.5, 0.0, 1.8, 0.8) with eyeopen
    
    pause 1.0
    d "Do you see this star here? This star is Polaris. It's a circumpolar star, which means it’s always visible and it points to this contellation."
    d "This is how you navigate using the Big Dipper. Look at the Dipper up here, those two stars at the edge? They point straight to Polaris."
    d "That constellation points and is located in the North part of the sky."

    # ORION / WEST SECTION
    show map at pan_to(1.0, 0.5, 1.8, 0.4)
    pause 1.0

    d "Now look over here. This is Orion."
    d "Orion is easy to spot because of his belt. It’s a great marker because Orion generally located in the East. If you need to head East, follow him."

    # CRUX / SOUTH SECTION
    $ quick_menu = False
    show map at pan_to(0.5, 1.0, 1.8, 0.4)
    pause 1.0

    d_top "And way down here, we have the Crux—or the Southern Cross."
    d_top "This constellation is what you look for to find South."

    # This line zooms the map out to show the full sky/map again
    show map at pan_to(0.5, 0.5, 1.0, 0.5)
    pause 0.5
    $ quick_menu = True

    d "Back when there were no maps or any navigating apps, our ancestors just used these. They looked at the same sky we're looking at now."
    d "And that's everything you need to know. Keep your eyes up the stars, and you won't get lost."

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
        d "If you get lost just remember to look up"
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
    

default forest_camp_visited = False
default no_count = 0

label forest_camp:
    scene bg forest camp with dissolve
    $ quick_menu = True
    window auto
    show screen gameUI

    if not forest_camp_visited:
        $ forest_camp_visited = True

        show Dawn surprised with dissolve
        d "Waooow!"
        d "You've actually got it"
        show Dawn smile
        d "Congrats! I'm very proud of you"
        d "You're now a certified celestial navigator"
        player_name "What does that even mean?"
        show Dawn normal
        d "Well, anyway I think we should rest and look around for now before get going"
        d "Tell me if you find anything interesting"
        hide Dawn with dissolve
        player_name "Is there even something interesting in a place like this?"

        $ quick_menu = False
        window hide
        pause 1.0
        show screen click_objects with dissolve
        pause
        hide screen click_objects
        $ quick_menu = True
        window auto

        show Dawn surprised with dissolve
        d "Look over here, I found a treasure map!"
        window hide
        $ quick_menu = False
        show screen show_treasure_map
        pause
        window show
        $ quick_menu = True

        show Dawn normal
        d "It looks ancient, but its still pretty much readable"
        d "Let's see where does this leads"
        d "East, South, North, West. Oh what's this?"
        d "Juano Piece?"
        show Dawn surprised
        d "!!!"
        d "So, it's real"
        d "The Juano Piece is real?!!"
        show Dawn lookaway
        d "I know you need to get back ASAP but please %(player_name)s we need to see where this goes"
        player_name "Huh? What's Juano Piece anyways?"
        player_name "Can we just leave this forest, and go home already"
        show Dawn normal
        d "No way, you dont know Juano Piece?"
        d "It's a treasure piece left by Don Juano"
        d "Legend says that asided from botomless gold, and jewels it has. It also has all the answers to question humanity have"
        d "It says that Don Juano got lost in this Mountain while trying to hide his treasure, and was never found again along with his treasure"
        d "I know it could be fake, but lets go anyways"
        d "It's not that everyday we get a chance to go to an adventure like this"

        menu start_adventure:
            "Should we follow the map?"
            "Yes":
                show Dawn smile
                player_name "Alright it's not like I would miss the chance to get rich"
                player_name "Plus I want to use my new navigation skills"
                d "Yay, let's hurry"
                d "Lead the way, I trust you we won't get lost"
                d "But first, let's take a final look at the map before going"
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map

            "No":
                $ no_count += 1
                if no_count == 1:
                    player_name "The map looks so fake, it's a waste of time, and energy"
                    player_name "Let's hurry up, and leave this forest"
                    show Dawn lookaway
                    d "But what if its real? we could've missed the chance to become billionaires"
                    d "Let's go Please"
                    jump start_adventure
                else:
                    $ please_text = " ".join(["Please"] * (2 ** (no_count - 1)))
                    show Dawn pout
                    d "[please_text]"
                    jump start_adventure

    else:
        show Dawn surprised with dissolve
        d "I think we've been here before"
        d "Did we get lost?"
        show Dawn normal
        d "Anyways, do you want to take another look at the map before heading out?"

        menu:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map

            "No, let's just go":
                player_name "I remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map
    

label to_treasure_step1:
    window show
    $ quick_menu = True

    scene bg treasure path 1
    show Dawn surprised with dissolve
    d "I've been on this mountain for quite some time, but this place looks unfamilliar"
    d "I think this is the point one on the map"
    show Dawn normal
    d "Well hey, do you have a dream?"
    d "Like what do you want to be when you grow up?"
    menu dream:
        "Do you have a dream"
        "Yes":
            player_name "Of course, I have one in minde"
            player_name "But I'm keeping it a secret so that no one can jinx it"
            show Dawn smile
            d "Oh, I hope your dreams come true"
            d "I'll be rooting for you"
            d "Well for me I want to become an Astrobiologist"
            d "I want to become the one that would make life in other planets possible"
            d "Or maybe even discover life in other planets as well"
        "Not yet":
            player_name "I'm still figuring it out"
            player_name "There's a ton of things to do out there I find it hard to decide"
            show Dawn smile
            d "I think you can be whatever you want to be"
            d "I believe in you"
            d "If one day you'll be able to decide please tell me immediately"
            d "I'll be rooting for you"
            d "Well for me I want to become an Astrobiologist"
            d "I want to become the one that would make life in other planets possible"
            d "Or maybe even discover life in other planets as well"
    show Dawn normal
    d "Do you believe in Aliens"
    menu aliens:
        "Do you believe in Aliens"
        "Yes":
            player_name "I have never seen one but I believe they exist"
            show Dawn surprised
            d "Oh really, I guess we're the same"
            show Dawn smile
            d "I think they exist"
            d "The Universe is so big, and mysterious yet nothing outside of our imagination
            seems impossible on it"
            d "And did you know the Drake equation by Frank Drake estimates that there
            are thousands of civilizations in the Universe"
            d "So whether I have seen them or not, I will keep believing they exist"
            d "Plus I think that it would be lonely if we're alone in this Universe"  
        "No":
            player_name "No, I haven't seen one so I don't think they exist"
            show Dawn surprised
            d "Oh really, I guess we're not the same"
            show Dawn smile
            d "I think they exist"
            d "The Universe is so big, and mysterious yet nothing outside of our imagination
            seems impossible on it"
            d "And did you know the Drake equation by Frank Drake estimates that there
            are thousands of civilizations in the Universe"
            d "So whether I have seen them or not, I will keep believing they exist"
            d "Plus I think that it would be lonely if we're alone in this Universe"
    show Dawn normal
    d "I think that's enough chatting"
    d "Let's keep moving"
    d "Do you want to look at the map before going?"
    menu map_review_1:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map_to_step2

            "No, let's just go":
                player_name "I remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step2


label to_treasure_step2:
    window show
    $ quick_menu = True

    scene bg treasure path 2
    show Dawn normal
    d "I think this is the point two on the map"

    d "Do you want to look at the map before going?"
    menu map_review_2:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map_to_step3

            "No, let's just go":
                player_name "I remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step3


label to_treasure_step3:
    window show
    $ quick_menu = True

    scene bg treasure path 3
    show Dawn normal
    d "I think this is the point three on the map"

    d "Do you want to look at the map before going?"
    menu map_review_3:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map_to_step4

            "No, let's just go":
                player_name "I remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step4


label to_treasure_step4:
    window show
    $ quick_menu = True

    scene bg treasure path 4
    show Dawn normal
    d "I think this is the point four on the map"

    d "Do you want to look at the map before going?"
    menu map_review_4:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call to_treasure_groove

            "No, let's just go":
                player_name "I remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call to_treasure_groove


label treasure_groove:
    window show
    $ quick_menu = True

    scene bg treasure groove
    show Dawn normal
    d "So this is where the treasure is"



### Chapter 2: Dawn at Midnight###


### Chapter 3: At Dawn ###