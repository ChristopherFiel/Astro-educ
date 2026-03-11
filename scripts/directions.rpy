screen direction_menu():
    textbutton "Go Straight":
        xalign 0.5
        yalign 0.15
        text_size 40
        action Return("straight")

    textbutton "Go Left":
        xalign 0.1
        yalign 0.5
        text_size 40
        action Return("left")

    textbutton "Go Right":
        xalign 0.9
        yalign 0.5
        text_size 40
        action Return("right")

    textbutton "Go Back":
        xalign 0.5
        yalign 0.85
        text_size 40
        action Return("back")