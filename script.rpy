default forest_intro_seen = False
default forest_mistakes = 0

default forest_camp_visited = False
default no_count = 0

default visited_step1_map = False
default visited_step2_map = False
default visited_step3_map = False

default visited_forest_camp_2 = False
default visited_lyrid_point_2 = False
default visited_lyrid_point_3 = False
default visited_lyrid_meteor_shower = False
default visited_road_point_1 = False


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
    $ time_of_day = 'DAY'
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

    show text "{font=cmunorm.ttf}{size=60}April 21\nMt. Mayumi Philippines{/size}{/font}" with dissolve
    pause (3.0)

    hide text with dissolve

    scene bg mountain background with dissolve
    play music "audio/ambience/bgm mountain background.mp3" fadein 1.0
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
    stop music fadeout 2.0
    $ time_of_day = 'DAY'
    scene bg mountain basecamp with dissolve
    play music "audio/ambience/bgm mountain camp.mp3" fadein 1.0
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
    $ time_of_day = 'DAY'
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

    stop music fadeout 2.0


label mountain_climb_grassyside_left:
    play music "audio/ambience/bgm left-right.mp3" fadein 1.0
    $ time_of_day = 'DAY'
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
                if rest_count >= 1:
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
    play music "audio/ambience/bgm left-right.mp3" fadein 1.0
    $ time_of_day = 'DAY'
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
    stop music fadeout 2.0
    play music "audio/ambience/bgm sunset.mp3" fadein 1.0
    scene black with arrow_wipe_down_slow
    $ time_of_day = "DUSK"
    scene bg mountain summit with arrow_wipe_down_slow
    $ quick_menu = True
    window auto

    p "*huff..*"
    p "Finally, I've reached the summit!!!"
    p "WOOOOOOOOOOOWWW!!!"
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
    
    stop music fadeout 2.0


label to_basecamp_forest:
    play music "audio/ambience/bgm night-1.mp3" if_changed fadein 1.0
    $ time_of_day = "NIGHT"
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
    $ time_of_day = "NIGHT"
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
    $ time_of_day = "NIGHT"
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
    $ time_of_day = "NIGHT"
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
    stop music fadeout 2.0
    play music "audio/ambience/bgm evening.mp3" fadein 1.0
    $ time_of_day = "NIGHT"
    scene black with fade
    scene bg forest starry sky with dissolve

    $ quick_menu = True
    window auto

    p "This should be a good place to rest"
    p "The sun's already out"
    p "The stars are so bright"
    p "I hope when I close my eyes I wake up from this nightmare"

    scene black with eyeclose
    stop music fadeout 2.0
    pause 2.0
    d_unknown "psst... hey"
    d_unknown "Yohoooo, can you hear me? I'm talking to you"
    d_unknown "Are you still alive?"
    d_unknown "Come on don't give up now, open your eyes"
    scene bg forest starry sky with eyeopen
    play music "audio/ambience/bgm evening.mp3"

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
            player_name "Kind of, it's litterally so dark I can't see anything"
        "...":
            player_name ".... yeah..."
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
    $ time_of_day = "NIGHT"
    $ quick_menu = False
    window hide
    show map at zoom_to(0.5, 0.4, 1.8) with dissolve
    pause 1.0

    play sound "audio/sfx/clank.mp3"
    show text "{font=Midnightconstellations-YLgo.ttf}{size=240}Look Up{/size}{/font}"
    pause (3.0)
    hide text
    play sound "audio/sfx/clank.mp3"
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Chapter 1: \n Dawn at Sunset{/size}{/font}"
    pause (3.0)
    hide text 

    jump forest_stargazing


label forest_stargazing:
    $ time_of_day = "NIGHT"
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

    # ORION / EAST SECTION
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
    scene black with dissolve
    scene bg forest starry sky with dissolve

    if not forest_intro_seen:
        $ quick_menu = True
        window auto
        show screen gameUI
        show Dawn normal with dissolve
        d "I hope you learned something new"
        show Dawn normal2
        d "Now, I know a mountaineer camp near us"
        d "Let's head over there now I think it's about..."
        d "North East from here"
        d "If you get lost just remember to look up"
        show Dawn normal
        d "Well, I'll be heading first"
        d "See Yah!"
        hide Dawn with dissolve
        "Dawn disappeared like dust in the wind"
        player_name "Well, she seems trustworthy. I should follow her."
        $ forest_intro_seen = True
    else:
        $ forest_mistakes += 1
        call forest_wrong_dialogue

    $ quick_menu = False
    window hide
    $ choice = renpy.call_screen("direction_menu")

    if choice == "straight":
        scene black with arrow_wipe_down
        jump forest_north
    elif choice == "left":
        scene black with arrow_wipe_right
        jump forest_west
    elif choice == "right":
        scene black with arrow_wipe_left
        jump forest_east
    elif choice == "back":
        scene black with arrow_wipe_up
        jump forest_south


label forest_north:
    $ time_of_day = "NIGHT"
    scene bg forest north with arrow_wipe_down
    show screen gameUI
    $ choice = renpy.call_screen("direction_menu")
    
    if choice == "straight":
        scene black with arrow_wipe_down
        jump to_basecamp_forest_with_dawn
    elif choice == "left":
        scene black with arrow_wipe_right
        jump to_basecamp_forest_with_dawn
    elif choice == "right":
        scene black with arrow_wipe_left
        jump forest_camp
    elif choice == "back":
        scene black with arrow_wipe_up
        jump to_basecamp_forest_with_dawn


label forest_south:
    $ time_of_day = "NIGHT"
    scene bg forest south with arrow_wipe_up
    show screen gameUI
    $ choice = renpy.call_screen("direction_menu")
    
    if choice == "straight":
        scene black with arrow_wipe_down
        jump to_basecamp_forest_with_dawn
    elif choice == "left":
        scene black with arrow_wipe_right
        jump to_basecamp_forest_with_dawn
    elif choice == "right":
        scene black with arrow_wipe_left
        jump to_basecamp_forest_with_dawn
    elif choice == "back":
        scene black with arrow_wipe_up
        jump to_basecamp_forest_with_dawn


label forest_east:
    $ time_of_day = "NIGHT"
    scene bg forest east with arrow_wipe_left
    show screen gameUI
    $ choice = renpy.call_screen("direction_menu")
    
    if choice == "straight":
        scene black with arrow_wipe_down
        jump to_basecamp_forest_with_dawn
    elif choice == "left":
        scene black with arrow_wipe_right
        jump forest_camp
    elif choice == "right":
        scene black with arrow_wipe_left
        jump to_basecamp_forest_with_dawn
    elif choice == "back":
        scene black with arrow_wipe_up
        jump to_basecamp_forest_with_dawn


label forest_west:
    $ time_of_day = "NIGHT"
    scene bg forest west with arrow_wipe_right
    show screen gameUI
    $ choice = renpy.call_screen("direction_menu")
    
    if choice == "straight":
        scene black with arrow_wipe_down
        jump to_basecamp_forest_with_dawn
    elif choice == "left":
        scene black with arrow_wipe_right
        jump to_basecamp_forest_with_dawn
    elif choice == "right":
        scene black with arrow_wipe_left
        jump to_basecamp_forest_with_dawn
    elif choice == "back":
        scene black with arrow_wipe_up
        jump to_basecamp_forest_with_dawn
    

label forest_camp:
    stop music fadeout 2.0
    play music "audio/ambience/bgm night-camp.mp3" if_changed fadein 1.0
    $ time_of_day = "NIGHT"
    scene black with dissolve
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
        show Dawn surprised
        d "No way, you dont know Juano Piece?"
        d "It's a treasure piece left by Don Juano"
        d "Legend says that it has everything a man wants, and needs. Wealth, Fame, Glory, it had everything"
        d "It says that Don Juano got lost in this Mountain while trying to hide his treasure,
        and was never found again along with his treasure"
        show Dawn lookaway
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
        scene bg forest camp with dissolve
        show Dawn surprised with dissolve
        d "I think we've been here before"
        d "Did we get lost?"
        d "Yeah right, we got lost hehe. But I think you got it this time"
        show Dawn normal
        d "Anyways, do you want to take another look at the map before heading out?"
        menu:
            "View the map again?"
            "Yes":
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call screen show_treasure_map
                call navigate_from_map

            "No, let's just go":
                player_name "I now remember the way, let's move."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map
    

label to_treasure_step1:
    $ time_of_day = "NIGHT"
    scene bg treasure path 1 with dissolve
    window show
    $ quick_menu = True

    if not visited_step1_map:
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
        $ visited_step1_map = True
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
                player_name "I get it now, I can get it right this time."
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step2
    
    else:
        show Dawn surprised with dissolve
        d "Back again at here I guess"
        d "This is the point one if I remember"
        d "Let's hurry, I know you got it this time"
        d "You can take another look at the map"
        menu map_review_1_repeat:
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
        hide Dawn with dissolve
        $ quick_menu = False
        window hide
        call navigate_from_map_to_step2


label to_treasure_step2:
    $ time_of_day = "NIGHT"
    scene bg treasure path 2 with dissolve
    $ quick_menu = True
    window auto

    if not visited_step2_map:
        $ visited_step2_map = True

        show Dawn normal with dissolve
        d "Hmm... by the looks of it we are at the second point on the map"
        player_name "Yeah, we've walked quite a lot in this dark forest"
        player_name "I wonder why it's so dark today, without the stars it's impossible to navigate around this forest"
        show Dawn lookaway
        d "Oh, it's because it's new moon today there's no light coming off from the moon"
        show Dawn normal
        d "The Moon is between Earth and the Sun, so the side facing us is dark. Its essentially invisible in the night sky."
        d "But don't worry it's not like Gru stole it again, the moon just goes to different phases"
        menu moonsplaining:
            "The moon phases"
            "Who's Gru":
                show Dawn lookaway
                d "Some sort of supervillain commanding a massive army"
                d "But he had a change of hearts recently so we are lucky"
                d "Well, anyways the moon, undergoes eight phases that causes it to grow brighter or darker"
            "The moon phases?":
                d "Yeah the moon, undergoes eight phases that causes it to grow brighter or darker"
        show Dawn normal2
        d "This process is called the Lunation and takes about 29.5 days"
        d "and by the way our moon's name is Luna, but if you want to still call it moon, make sure you capitalize the M, because it is not only our moon, it is THE Moon"
        show Dawn smile
        d "hehe"
        show Dawn normal2
        d "Anyways the phases in order are, New Moon, Waxing Crescent, First Quarter, Waxing Gibbous, Full Moon, Waning Gibbous, Third Quarter, Waning Crescent"
        d "The brightest phase is the Full Moon in where we can see the Moon at it's full form, and the darkest phase is the New Moon in where the Moon is not visible to us all"
        show Dawn smile
        d "before it reaches Full Moon it goes through waxing which means 'growing', on the other hand before it reached New moon it goes through waning which means 'shrinking'"
        d "And the Moon does not actually shine but only reflects light from the Sun"
        show Dawn normal
        d "You can actually tell by just looking at the moon whether it's waxing or waning"
        d "When the moon looks like a capital D it's waxing, while if it looks like capital C it's waning"
        player_name "I didn't really consider that when planning my hike"
        player_name "The Moon is certainly interesting"
        d "Anyways which one do you prefer New Moon, or Full Moon?"
        menu selenophile:
            "I prefer"
            "Full Moon":
                player_name "I love seeing the Moon at it's fullest form, it's beautiful, and mesmerizing"
                show Dawn smile
                d "I see you are a selenophile"
                player_name "Selenophile"
                d "Someone who loves the Moon"
            "New Moon":
                player_name "I love dark nights where I can appreciate the dark skies"
                show Dawn surprised
                d "I see, we're the same then"
        show Dawn smile
        d "Personally I love seeing the dark skies"
        d "The darker the night the brighter the stars"
        d "It reminds me that there's always something to look forward to no matter how dark the times becomes"
        player_name "You're right the Moon might be absent but the stars are literally here to guide us"
        show Dawn normal
        d "Let's head out now. I still have the map by the way if you want to take another look"
        d "We're currently at point 2"
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
                player_name "I think I've got it"
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step3

    else:
        show Dawn normal with dissolve
        d "Oh yeah I remember this path"
        d "Your'e not really good at this"
        d "But let's take the next step"
        show Dawn smile
        d "I know you got it this time"
        show Dawn normal
        d "Anyways, I still have the map if you want to take another look"
        menu map_review_2_revisit:
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
    $ time_of_day = "NIGHT"
    scene bg treasure path 3 with dissolve
    window show
    $ quick_menu = True

    if not visited_step3_map:
        $ visited_step3_map = True

        show Dawn surprised with dissolve
        d "*huff...* We're at... the... point three... on the map *huff...*"
        d "*huff...*"
        d "This is tiring me"
        d "At the very least"
        show Dawn smile
        d "We're finally halfway there"
        d "Let's move quick it is just a bit further now"
        show Dawn normal
        d "If I'm counting it right we're at point three"
        d "I still have the map if you want to take another look"
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
                player_name "I am a professional celestial navigator don't worry"
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step4

    else:
        show Dawn surprised with dissolve
        d "Even it's dark I still remember this"
        d "I am sure we've taken this way before"
        d "This is the point three"
        show Dawn smile
        d "But that only means we're getting closer to the treasure"
        show Dawn normal
        d "Anyways, do you want to take another look at the map before heading out?"
        menu map_review_3_revisit:
            "View the map again?"
            "Yes":
                show screen show_treasure_map
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                pause
                call navigate_from_map_to_step4
            "No, let's just go":
                player_name "I am a professional celestial navigator don't worry"
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_from_map_to_step4


label to_treasure_step4:
    $ time_of_day = "NIGHT"
    scene bg treasure path 4 with dissolve
    window show
    $ quick_menu = True
    
    show Dawn normal
    d "We're at the point four on the map, we're almost there"
    d "Do you want to look at the map before going?"
    d "We're at the point four on the map"
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


### Chapter 2: Sunrise at Dawn###
label treasure_groove:
    stop music fadeout 2.0
    play music "audio/ambience/bgm treasure groove.mp3" fadein 1.0
    $ time_of_day = "NIGHT"
    scene bg treasure groove with dissolve
    window show
    $ quick_menu = True

    show Dawn pout at dawn_pacing_left(2.5)
    pause 2.0

    show Dawn pout at center with ease
    d "Hmmm... Is this really the right place? I'm pretty sure we followed the map correctly."

    show Dawn pout at dawn_pacing_right(1.5)
    pause 1.5

    show Dawn pout at center with ease
    d "But I still haven't seen something like X mark on the ground, Troll Guardian, A hermit riddler..."
    show Dawn lookaway
    d "Well I guess, the map is fake all along hehehe..."
    show Dawn smile
    d "But anyways, I enjoyed talking with you and sharing all my random astronomical facts"
    d "Even if it might be overwhelming for you. Astronomy, the space, and the universe is
    such a captivating topic. I hoped you learned something new"
    player_name "..."
    player_name "I don't really think our journey here is all in vain"
    player_name "Maybe, the real treasure is the--"
    show Dawn surprised
    d "Wait did you hear that"
    show Dawn surprised
    player_name "Hear what?"
    player_name "Anyway It's already midnight"
    player_name "Let's now get out of this fore--"
    stop music
    $ quick_menu = False
    window hide
    play sound "audio/sfx/meteor impact.mp3"
    show screen meteor_impact_fx
    camera at meteor_shake
    hide Dawn with dissolve
    scene black with fade 
    play sound "audio/sfx/bass drop.ogg"
    pause 0.85
    camera 
    pause 0.15 
    hide screen meteor_impact_fx
    scene white with fade
    pause 2.0
    play sound "audio/sfx/clank.mp3"
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}{color=#000000}Chapter 2: \nSunrise at Dawn{/color}{/size}{/font}"    
    pause (3.0)
    hide text
    jump forest_camp_2

    
label forest_camp_2:
    $ time_of_day = "NIGHT"
    $ quick_menu = True
    window auto

    if not visited_forest_camp_2:
        play music "audio/sfx/dragging.mp3"
        hide screen gameUI
        scene black with fade
        $ visited_forest_camp_2 = True
        d "Hello can you hear me?"
        d "Are you still there?"
        d "Can you wake UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n
            UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
            UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
        d "p"
        d "*sigh*"
        d "What do I even do"
        d "Maybe I should just leave you here"
        scene bg forest camp 2 with eyeopen
        stop music
        play music "audio/ambience/bgm forest camp 2.mp3"
        show Dawn lookaway with dissolve
        show screen gameUI
        player_name "hey..."
        player_name "I'm still here. I'm just resting my eyes"
        player_name "What does even happened"
        show Dawn surprised
        d "Oh your'e still alive"
        d "A meteor fell near us, and cause an explosion"
        show Dawn smile
        d "Luckily we're just caught by it's shockwave, and didn't get vaporized"
        d "I've taken some fragment hehe. here take a look"
        show Dawn normal
        d "Did you know it's called Meteoroid when it's floating in space"
        d "Meteor when it's burning on our athmosphere"
        d "And Meteorite when it falls on the ground"
        player_name "Oh really? thanks but that did not really help our situation"
        player_name "I'm ready to go now, let's get out of here"
        show Dawn normal2
        d "I just remembered today is the peak of the Lyrid Meteor Shower"
        d "I know just a place in this forest where we can perfectly watch it"
        d "It's almost just about, the best time to see it let's hurry"
        d "And by the way since it's already past midnight Orion now points at west"
        hide Dawn with dissolve
        player_name "*sigh* Here we go again"
    else:
        scene bg forest camp 2 with dissolve
        show screen gameUI
        player_name "I'm certain that I've been here before"
        player_name "What does Dawn said again?"
        player_name "Right. Orion now points at West"

    menu follow_dawn:
        "What should I do?"
        "Follow Dawn":
            player_name "What is she up to again?"
            player_name "By the looks of it I think she went South then West"
            player_name "I've got to hurry"
            $ quick_menu = False
            window hide
            call navigate_to_lyrid_1
        "Get out of the forest":
            player_name "How do I even get out of this forest"
            player_name "Even if I know now how to navigate directions I still don't know which
                        direction is the way out"
            player_name "I don't think I have a choice but to follow her"
            jump follow_dawn
        "Stay still":
            player_name "I'll just rest some more here"
            player_name "I don't think she'll go anywhere far"
            player_name "Do I even have a choice but to follow her"
            $ quick_menu = False
            window hide
            pause 1.0
            show screen press_to_continue with dissolve
            pause
            $ quick_menu = True
            window show
            hide screen press_to_continue
            jump follow_dawn


label to_lyrid_point_1:
    $ time_of_day = "NIGHT"
    scene bg lyrid path 1 with dissolve
    $ quick_menu = True
    window hide

    player_name "She should be nearby now"
    player_name "Right... she went west from here"

    $ quick_menu = False
    window hide
    call navigate_to_lyrid_2
    

label to_lyrid_point_2:
    $ time_of_day = "NIGHT"
    scene bg lyrid path 2 with dissolve
    $ quick_menu = True
    window hide

    if not visited_lyrid_point_2:
        $ visited_lyrid_point_2 = True
        show Dawn surprised with dissolve
        d "Oh wow you found me, quite fast"
        d "I'm surprised you did not get confused with the position of Orion"
        show Dawn pout
        d "It might be already too late since you alread learned it on you own"
        d "But let me explain anyways"
        show Dawn normal2
        d "In the Northern Hemisphere, stars appear to rotate counter-clockwise around a point
            called the North Celestial Pole, which is marked almost exactly by the North Star, Polaris."
        d "But actually the stars do not move, it's just the Earth Spinning on it's axis"
        show Dawn smile
        d "Our favourite constellation Orion is an is an equatorial constellation,
            meaning it sits right above the Earth's equator."
        d "And because of that it takes a follows a wide arc across the sky, much like the Sun"
        show Dawn normal2
        d "It rises in the east and sets in the west, so by after midnight, its already heading going
            down the western horizon."
        d "On the other hand, Big Dipper is circumpolar its circle of rotation is very small.
            Instead of rising and setting, it simply circles Polaris like a hand on a clock."
        show Dawn normal
        d "And lastly Crux, can be called as the Big Dipper of the South."
        show Dawn normal2
        d "If you're near the tropics like us, it just barely peeks over the southern horizon and
            hugs that spot because it's circling the South Pole, which is hidden below your view."
        show Dawn smile
        d "Now with that let's head further down West"
        d "The place I knew to watch the Lyrid Meteor shower is near now"
        hide Dawn with dissolve
        player_name "She disappeared like a wind again"
        player_name "There's something myterious about her"
        player_name "We've been running on some sidequest I literally dont know where I am at"
        player_name "Whatever, when I finally know how to get out of this forest I'll drag her out"
        player_name "First I just need to head down West"
        $ quick_menu = False
        window hide
        call navigate_to_lyrid_3
    else:
        player_name "Did I get lost?"
        player_name "again?"
        player_name "Oh... right it's ok I just need to head down West"
        $ quick_menu = False
        window hide
        call navigate_to_lyrid_3


label to_lyrid_point_3:
    $ time_of_day = "NIGHT"
    scene bg lyrid path 3 with dissolve
    $ quick_menu = True
    window hide

    if not visited_lyrid_point_3:
        $ visited_lyrid_point_3 = True
        show Dawn normal with dissolve
        d "Hey, have you watched meteor shower before?"
        menu meteor_shower_experience:
            "Have you watched meteor shower before?"
            "I have":
                player_name "Yes, I've watched a meteor shower before, in my garden"
                show Dawn surprised
                d "Waow, it's beautiful isn't it"
            "Not yet":
                player_name "No, this would be my first time"
                player_name "Isn't that the one where a bunch of ganster get into some drama
                            because their leader fell inlove with an ordinary college girl."
                show Dawn pout
                d "What are you talking about"
                player_name "Nothing"
        show Dawn normal2
        d "Well, a meteor shower is essentially Earth passing through a cloud of space debris
            left behind by a comet or an asteroid."
        d "When a comet nears the sun, it sheds a trail of dust and rock fragments in its wake."
        d "As Earth orbits through this debris, the particles slam into our atmosphere and burn up,
            creating the bright streaks we see as meteor showers."
        show Dawn normal
        d "And tonight is the peak of the Lyrid Meteor shower, one of the oldest known meteor showers"
        d "These meteors appear to come from the constellation Lyra,
            specifically near the bright star Vega."
        show Dawn smile
        d "I know perfect spot to watch it just go North, then West from here"
        d "Let's go"
        hide Dawn with dissolve
        $ quick_menu = False
        window hide
        call navigate_to_lyrid_path
    else:
        player_name "Hmmm... I'm back here"
        player_name "Did I get my directions wrong?"
        player_name "It's ok I just need to go North and then West"
        $ quick_menu = False
        window hide
        call navigate_to_lyrid_path


label to_meteor_shower:
    $ time_of_day = "NIGHT"
    scene bg meteor shower path with dissolve
    $ quick_menu = True
    window hide

    player_name "It's west now from here"

    $ quick_menu = False
    window hide
    call navigate_to_lyrid_meteor_shower


label lyrid_meteor_shower:
    $ time_of_day = "NIGHT"
    scene bg lyrid meteor shower at resizer
    $ quick_menu = True
    window hide

    if not visited_lyrid_meteor_shower:
        $ visited_lyrid_meteor_shower = True
        show Dawn smile
        d "We're here"
        d "This place sits at the right elevation, with an onobstructed view of the night sky"
        d "The perfect place to watch the Lyrid Meteor shower"
        d "And we've just arrive at the perfect time where the meteor shower it's at it's peak"
        d "Yayy!"
        show Dawn lookaway
        d "This is actually my secret spot, so I'm trusting you to keep this place a secret"
        show Dawn pout
        d "You know your'e so lucky"
        d "When I watched the Lyrid Meteor shower before all of a sudden it always gets cloudy"
        d "And I barely see any shooting stars"
        d "But tonight the sky is clear as day"
        d "It's unfair"
        player_name "..."
        player_name "I'm sorry, I guess?"
        show Dawn lookaway
        d "Nevermind, anyways let's sit somewhere and watch the Lyrid Meteor shower"
        show Dawn smile
        d "Here should fine, are you ready?"
        menu watch_meteor_shower:
            "Are you ready?"
            "Watch the Meteor shower":
                $ quick_menu = False
                hide screen gameUI
                scene black with fade
                stop music fadeout 2.0
                play music "audio/ambience/bgm meteor shower.mp3"
                show meteor_shower with dissolve
                pause 30.0
                stop music fadeout 2.0
                hide meteor_shower with fade
                scene bg lyrid meteor shower with dissolve
                $ quick_menu = True
                show screen gameUI
                show Dawn smile
                d "The shooting stars are always so beautiful I think I've seen 23"
                d "They never failed to impress me even though I've seen them countless of times"
                d "Have you make your wish?"
                menu wishes:
                    "Have you make your wish?"
                    "Yes":
                        player_name "Yes' I've wish to pas--"
                        show Dawn surprised
                        d "SHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!"
                        d "Your'e supposed to not say your wish otherwise it won't come true"
                    "No":
                        player_name "No, I think I've doze off but I dont really believe in wishing on a star"
                        show Dawn pout
                        d "Oh really? I think there's nothing wrong on putting your faith onto something"
                        d ""
                show Dawn normal
                d "Don't worry I've wished for both of us in all the shooting stars I've seen"
                show Dawn lookaway
                d "Anyways dont worry I didn't forgot I'll get you out of here from this forest"
                d "It's actually really easy now we're at this place"
                show Dawn normal2
                d "All you gotta do from here is head down South"
                d "And you'll see a road there and a bus stop"
                player_name "Oh finally it's about time"
                player_name "I'm tired from all this, I actually wished to have the ability to float"
                show Dawn smile
                d "Hahahahahaha. I guess you could say that it's impossible to come true anyways"
                player_name "Alright, let's goooooooooo!!!"
                hide Dawn with dissolve
                $ quick_menu = False
                window hide
                call navigate_to_road_1
    else:
        show Dawn normal with dissolve
        player_name "Wait, this place again?"
        show Dawn surprised
        d "How did you end up back here?"
        player_name "I have no idea"
        show Dawn smile
        d "Head South from here, you'll hit the road"
        hide Dawn
        $ quick_menu = False
        window hide
        call navigate_to_road_1


label to_road_point_1:
    stop music fadeout 2.0
    play music "audio/ambience/bgm to road.mp3" if_changed
    $ time_of_day = "NIGHT"
    $ quick_menu = True
    window hide
    scene bg to road path 1 with dissolve

    if not visited_road_point_1:
        $ visited_road_point_1 = True
        show Dawn pout with dissolve
        d "This will be the last time we'll be able to look at the stars for direction"
        d "but don't worry after our next stop it'll be a straight path now"
        d "Let's head south again now"
        player_name "Is there something wrong?"
        show Dawn lookaway
        d "Nothing, let's go"
        hide Dawn with dissolve
        $ quick_menu = False
        window hide
        call navigate_to_dawn_goodbye
    else:
        show Dawn surprised with dissolve
        d "You went the wrong way again?"
        player_name "Don't ask"
        show Dawn smile
        d "It's ok Just keep heading South"
        hide Dawn with dissolve
        $ quick_menu = False
        window hide
        call navigate_to_dawn_goodbye


label dawn_goodbye:
    $ time_of_day = "NIGHT"
    scene bg Goodbye Dawn with dissolve
    $ quick_menu = True
    window hide
    hide screen gameUI
    
    show Dawn lookaway with dissolve
    d "It's almost sunrise"
    d "You can go straight forward from here"
    player_name "Yeah, lets go"
    show Dawn pout
    d "I'm sorry but I can't come with you"
    show Dawn lookaway
    d "I'll be staying here at this forest for some more time"
    player_name "Are you serious?"
    player_name "We've been through this journey together"
    player_name "Let's finish it together"
    show Dawn surprised
    d "I'm sorry but I have something more do"
    show Dawn lookaway
    player_name "Come on"
    menu goodbye_dawn:
        "What should I do?"
        "Give up":
            player_name "Alright, I guess I really can't convince you"
            player_name "I hope you stay safe, drink a lot of water"
            player_name "I am so grateful that I've met you"
            player_name "You literally saved my life"
            player_name "I promise when we meet again I'll pay it all back"
            show Dawn smile
            d "I'm so happy to hear that but dont worry"
            d "I am sure we'll meet again somewhere"
            player_name "Really? Where?"
            d "Yeah, Just Look Up"
            hide Dawn with dissolve
            $ time_of_day = "DAWN"
            scene black with eyeclose
            scene sunrise_scene with eyeopen
            player_name "Huh???"
            player_name "At the sky?"
            player_name "But how can we--"
            d "Goodbye"
            scene black with eyeclose
            scene bg Goodbye Dawn with eyeopen
            player_name "Where did she we--??"
            player_name "Well I guess that's it then I have to keep moving"
            $ quick_menu = False
            window hide
            call screen direction_menu_forward
            jump to_road_point_2
        "Convince":
            player_name "I won't leave here without you"
            player_name "What is it that why you can't leave this place"
            player_name "It's not that you can never come here again"
            show Dawn pout
            d "I'm sorry I can't tell you but I must stay here for now"
            jump goodbye_dawn
        

label to_road_point_2:
    $ time_of_day = "DAWN"
    scene black with arrow_wipe_down_slow
    scene bg to road path 2 at resizer with arrow_wipe_down_slow
    $ quick_menu = True
    window hide
    player_name "It's been a long journey too bad I'll finish it alone"
    $ quick_menu = False
    window hide
    call screen direction_menu_forward
    jump to_road_point_3


label to_road_point_3:
    $ time_of_day = "DAWN"
    scene black with arrow_wipe_down_slow
    scene bg to road path 3 with arrow_wipe_down_slow
    $ quick_menu = True
    window hide
    player_name "I wonder what she's really up to"
    player_name "...."
    $ quick_menu = False
    window hide
    call screen direction_menu_forward
    jump roadside


label roadside:
    stop music fadeout 2.0
    scene black with arrow_wipe_down_slow
    scene black with fade
    $ time_of_day = "DAY"
    scene bg roadside with dissolve
    $ quick_menu = True
    window hide
    player_name "*huff...* *huff...* *huff...*"
    player_name "Finally the road it's over"
    player_name "I can finally go home"
    player_name "I'll rest for an eternity after this"

    play sound "audio/sfx/paper crumple.mp3" 
    player_name "Wait what's this a poster?"
    window hide
    $ quick_menu = False
    show missing_poster_back:
        "images/objects/missing poster back.webp"
        zoom 0.25
        truecenter
    with dissolve
    pause
    hide missing_poster_back
    show missing_poster_front:
        "images/objects/missing poster front.webp"
        zoom 0.5
        truecenter
    with dissolve
    pause
    hide missing_poster_front with dissolve
    window show
    $ quick_menu = True
    play sound "audio/sfx/paper crumple.mp3"
    
    player_name "Missing Dawn Last seen April 16, 2003"
    player_name "This is exactly her in this poster"
    player_name "Wait this is more than two decades ago?"
    player_name "But???"
    player_name "What about???"
    player_name "Hmmmm.... so Dawn the one I met is"
    player_name "Dea--"
    # SFX chilling touch wind
    player_name "WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"
    # SFX Running
    $ quick_menu = False
    window hide
    play sound "audio/ambience/ending theme.mp3" fadein 1.0
    pause 1.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Directed by \n Christopher Fiel Jr.{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Written by \n  Christopher Fiel Jr.{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Backgrounds by \n Marie Elyze Sarmiento{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Gameplay by \n Marie Elyze Sarmiento{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Programmed by \n Christopher Fiel Jr.{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Maps by \n Marie Elyze Sarmiento{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Audios by \n Christopher Fiel Jr.{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Character sprites by \n Koto \n https://kotocoffee.itch.io/{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}UI by \n Chiara \n https://tenshi-yoru.itch.io/{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=120}Bgs from \n Unsplasm \n forest2sea{/size}{/font}"
    pause 3.0
    show text "{font=Midnightconstellations-YLgo.ttf}{size=160}Thank you for Playing :3{/size}{/font}"
    pause 5.0
    scene black with fade
    $ renpy.full_restart()


### END ###