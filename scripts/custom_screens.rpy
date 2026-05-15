default tip_index = 0

init python:
    tips = [
        "Try Looking Up before picking a direction",
        "Pay attention to Dawn, she could give you clues to get out of the forest",
        "Follow the direction on the sky",
        "Orion points at East before midnight, and West after midnight",
        "Big Dipper always points at North",
        "Crux always points at South",
    ]


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


screen basic_controls():
    text """{font=cmunorm.ttf}{size=40} Basic Controls \n
    Left Click / Space / Enter — Advance dialogue \n
    Right Click / Escape — Open menu \n
    Middle Click — Hide textbox \n
    Scroll Up — Rollback \n{/size}{/font}""":
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
    text "{font=cmunorm.ttf}{size=40}Look around the forest{/font}":
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
                xysize=(int(config.screen_width * 0.75), int(config.screen_height * 0.75)),
                fit="contain",
                anchor=(0.5, 0.5),
                pos=(0.5, 0.5)):
        pass

    button:
        xfill True
        yfill True
        action [SetVariable("poster_examined", False), Hide("poster_close_up")]


screen got_lost():
    modal True

    add Solid("#000000"):
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

    text "{font=cmunorm.ttf}{size=55}You got lost in the dark forest...{/size}{/font}":
        xalign     0.5
        yalign     0.4
        text_align 0.5
        color      "#ffffff"
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

    text "{font=cmunorm.ttf}{size=35}Exploring the unknown path{/size}{/font}":
        xalign     0.5
        yalign     0.52
        text_align 0.5
        color      "#ffffff"
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

    text "{font=cmunorm.ttf}{size=40}Tip: [tips[tip_index]]{/font}":
        xalign     0.5
        yalign     0.90
        text_align 0.5
        color      "#ffffff"

    timer 5.0 action [
        SetVariable("tip_index", (tip_index + 1) % len(tips)),
        Hide("got_lost")
    ]

    button:
        xfill  True
        yfill  True
        action [
            SetVariable("tip_index", (tip_index + 1) % len(tips)),
            Hide("got_lost")
        ]


transform scene_blur:
    blur 20

screen meteorite_interaction():
    modal True 

    on "show" action [
        Function(renpy.show_layer_at, scene_blur, layer='master'),
        Function(renpy.show_layer_at, scene_blur, layer='layerfarback')
    ]
    
    on "hide" action [
        Function(renpy.show_layer_at, [reset], layer='master'),
        Function(renpy.show_layer_at, [reset], layer='layerfarback')
    ]

    button:
        action [Hide("meteorite_interaction"), Return()]
        xfill True 
        yfill True 
        background None 
        
        add "images/objects/meteorite.webp" align (0.5, 0.5)


screen show_treasure_map():
    modal True

    frame:
        xalign     0.5
        yalign     0.5
        xsize      int(config.screen_width)
        ysize      int(config.screen_height)
        background "#c8a96e"
        padding    (0, 0)

        add "images/objects/treasure_map.webp":
            align (0.5, 0.5)
            at transform:
                alpha  0.0
                linear 0.4 alpha 1.0

        add Transform("images/wipes/vignette.png",
                    xysize=(int(config.screen_width), int(config.screen_height)),
                    fit="fill"):
            align (0.5, 0.5)

    text "{font=cmunorm.ttf}{size=40}Press any button or click anywhere to continue{/font}":
        xalign     0.5
        yalign     0.90
        text_align 0.5

    button:
        xfill  True
        yfill  True
        action [Hide("show_treasure_map", transition=dissolve), Return()]


screen infinite_scream():
    zorder 50
    default a_str = ""

    # cps ≈ 10
    timer 0.10 repeat True action SetScreenVariable("a_str", a_str + "A")

    python:
        _full  = "WA" + a_str + "A"
        _cpl   = 16   # characters per line — increase if text wraps too early,
        _lines = [ _full[i : i + _cpl] for i in range(0, len(_full), _cpl) ]
        _wrapped = "\n".join(_lines)

    text "{font=Midnightconstellations-YLgo.ttf}{size=160}[_wrapped]{/size}{/font}":
        xalign 0.5
        yalign 0.5
        text_align 0.5