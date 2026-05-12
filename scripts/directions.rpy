default current_map = "map"

style navigation_button_text:
    size 60
    outlines [(2, "#000", 0, 0)]
    hover_color "#ff0"

screen direction_menu():
    textbutton "Go Forward":
        xalign 0.5 yalign 0.15
        text_style "navigation_button_text"
        selected False
        action [SetVariable("current_map", "map-north"), Return("straight")]

    textbutton "Go Left":
        xalign 0.1 yalign 0.5
        text_style "navigation_button_text"
        selected False
        action [SetVariable("current_map", "map-west"), Return("left")]

    textbutton "Go Right":
        xalign 0.9 yalign 0.5
        text_style "navigation_button_text"
        selected False
        action [SetVariable("current_map", "map-east"), Return("right")]

    textbutton "Go Backward":
        xalign 0.5 yalign 0.85
        text_style "navigation_button_text"
        selected False
        action [SetVariable("current_map", "map-south"), Return("back")]


screen direction_menu_horizontal():
    textbutton "Go Left":
        xalign 0.1
        yalign 0.5
        text_style "navigation_button_text"
        action Return("left")

    textbutton "Go Right":
        xalign 0.9
        yalign 0.5
        text_style "navigation_button_text"
        action Return("right") 


screen direction_menu_forward():
    textbutton "Go Forward":
        xalign 0.5
        yalign 0.15
        text_style "navigation_button_text"
        action Return("straight") 


screen direction_menu_no_map():
    textbutton "Go Forward":
        xalign 0.5
        yalign 0.15
        text_style "navigation_button_text"
        action Return("straight")

    textbutton "Go Left":
        xalign 0.1
        yalign 0.5
        text_style "navigation_button_text"
        action Return("left")

    textbutton "Go Right":
        xalign 0.9
        yalign 0.5
        text_style "navigation_button_text"
        action Return("right")
    

label navigate_from_map:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    # Set the wipe based on choice for wrong turns
    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_treasure_step1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-west":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_treasure_step1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-south":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_treasure_step1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-north":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_treasure_step1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost
        jump forest_camp


label navigate_from_map_to_step2:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_treasure_step2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-west":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_treasure_step2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-south":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_treasure_step2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-north":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_treasure_step2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump forest_camp


label navigate_from_map_to_step3:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_treasure_step3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-west":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_treasure_step3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-south":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_treasure_step3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-north":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_treasure_step3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump forest_camp


label navigate_from_map_to_step4:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_treasure_step4
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-west":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_treasure_step4
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-south":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_treasure_step4
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-north":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_treasure_step4
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump forest_camp


label to_treasure_groove:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "back":
            scene black with arrow_wipe_up
            jump treasure_groove
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-west":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump treasure_groove
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-south":
        if choice == "right":
            scene black with arrow_wipe_left
            jump treasure_groove
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    elif prev_map == "map-north":
        if choice == "left":
            scene black with arrow_wipe_right
            jump treasure_groove
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump forest_camp


label navigate_to_lyrid_1:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_lyrid_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-west":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_lyrid_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-south":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_lyrid_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-north":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_lyrid_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump forest_camp_2


label navigate_to_lyrid_2:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_lyrid_point_2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-west":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_lyrid_point_2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-south":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_lyrid_point_2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2

    elif prev_map == "map-north":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_lyrid_point_2
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump forest_camp_2


label navigate_to_lyrid_3:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_lyrid_point_3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_2

    elif prev_map == "map-west":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_lyrid_point_3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_2

    elif prev_map == "map-south":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_lyrid_point_3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_2

    elif prev_map == "map-north":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_lyrid_point_3
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_2


label navigate_to_lyrid_path:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-west":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-south":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-north":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump to_lyrid_point_3


label navigate_to_lyrid_meteor_shower:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "straight":
            scene black with arrow_wipe_up
            jump lyrid_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-west":
        if choice == "back":
            scene black with arrow_wipe_down
            jump lyrid_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-south":
        if choice == "left":
            scene black with arrow_wipe_right
            jump lyrid_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3

    elif prev_map == "map-north":
        if choice == "right":
            scene black with arrow_wipe_left
            jump lyrid_meteor_shower
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump to_lyrid_point_3


label navigate_to_road_1:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "right":
            scene black with arrow_wipe_left
            jump to_road_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-west":
        if choice == "left":
            scene black with arrow_wipe_right
            jump to_road_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-south":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump to_road_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-north":
        if choice == "back":
            scene black with arrow_wipe_up
            jump to_road_point_1
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump lyrid_meteor_shower


label navigate_to_dawn_goodbye:
    $ prev_map = current_map
    $ choice   = renpy.call_screen("direction_menu")

    if choice == "straight":
        $ wrong_wipe = arrow_wipe_down
    elif choice == "back":
        $ wrong_wipe = arrow_wipe_up
    elif choice == "left":
        $ wrong_wipe = arrow_wipe_right
    else:
        $ wrong_wipe = arrow_wipe_left

    if prev_map == "map-east":
        if choice == "right":
            scene black with arrow_wipe_left
            jump dawn_goodbye
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-west":
        if choice == "left":
            scene black with arrow_wipe_right
            jump dawn_goodbye
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-south":
        if choice == "straight":
            scene black with arrow_wipe_down
            jump dawn_goodbye
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    elif prev_map == "map-north":
        if choice == "back":
            scene black with arrow_wipe_up
            jump dawn_goodbye
        else:
            scene black with wrong_wipe
            show screen got_lost with dissolve
            pause 3.0
            hide screen got_lost with dissolve
            jump lyrid_meteor_shower

    else:
        scene black with dissolve
        show screen got_lost with dissolve
        pause 3.0
        hide screen got_lost with dissolve
        jump lyrid_meteor_shower