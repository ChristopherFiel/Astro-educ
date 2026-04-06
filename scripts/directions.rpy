default current_map = "map"

style navigation_button_text:
    size 60
    outlines [(2, "#000", 0, 0)]
    hover_color "#ff0"

screen direction_menu():
    textbutton "Go Straight":
        xalign 0.5 yalign 0.15
        text_style "navigation_button_text"
        selected False # <--- Add this line
        action [SetVariable("current_map", "map-north"), Return("straight")]

    textbutton "Go Left":
        xalign 0.1 yalign 0.5
        text_style "navigation_button_text"
        selected False # <--- Add this line
        action [SetVariable("current_map", "map-west"), Return("left")]

    textbutton "Go Right":
        xalign 0.9 yalign 0.5
        text_style "navigation_button_text"
        selected False # <--- Add this line
        action [SetVariable("current_map", "map-east"), Return("right")]

    textbutton "Go Back":
        xalign 0.5 yalign 0.85
        text_style "navigation_button_text"
        selected False # <--- Add this line
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


screen direction_menu_vertical():
    textbutton "Go Straight":
        xalign 0.5
        yalign 0.15
        text_style "navigation_button_text"
        action Return("straight") 

    textbutton "Go Back":
        xalign 0.5
        yalign 0.85
        text_style "navigation_button_text"
        action Return("back") 


screen direction_menu_no_map():
    textbutton "Go Straight":
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