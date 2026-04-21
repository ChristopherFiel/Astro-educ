screen disclaimer_screen():
    text """{font=cmunorm.ttf}{size=40}The places, events, and characters
in this game are all works of fiction.
Any similarities to real life are
purely coincidental and do not have
any correlation with the game.{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10


screen press_to_continue():
    text "{font=cmunorm.ttf}{size=40}Press any button or click anywhere to continue{/font}":
        xalign 0.5
        yalign 0.90
        text_align 0.5


screen click_objects():
    text "{font=cmunorm.ttf}{size=40}Hover the mouse around, and click objects{/font}":
        xalign 0.5
        yalign 0.90
        text_align 0.5
    

default poster_examined = False

screen show_poster():
    if not poster_examined:
        imagebutton:
            xpos 400
            ypos 300
            idle  Transform("images/objects/missing poster back.png", zoom=0.15)
            hover Transform("images/objects/missing poster back.png", zoom=0.17)
            action [
                SetVariable("poster_examined", True),
                Show("poster_close_up"),
            ]

screen poster_close_up():
    modal True

    add "#0008"

    add Transform("images/objects/missing poster front.png",
                xysize=(int(config.screen_width * 0.75), int(config.screen_height * 0.95)),
                fit="contain",
                anchor=(0.5, 0.5),
                pos=(0.5, 0.5)):
        pass

    button:
        xfill True
        yfill True
        ## Reset poster_examined when closing so the back reappears
        action [SetVariable("poster_examined", False), Hide("poster_close_up")]