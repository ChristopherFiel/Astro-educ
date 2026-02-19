# Transform for the eyelids
transform top_lid_close:
    yanchor 1.0 ypos 0.0
    linear 0.3 ypos 0.5

transform top_lid_open:
    yanchor 1.0 ypos 0.5
    linear 0.5 ypos 0.0

transform bottom_lid_close:
    yanchor 0.0 ypos 1.0
    linear 0.3 ypos 0.5

transform bottom_lid_open:
    yanchor 0.0 ypos 0.5
    linear 0.5 ypos 1.0


screen pov_blink(opening=True):
    zorder 100

    if opening:
        add Solid("#000"):
            at top_lid_open
        add Solid("#000"):
            at bottom_lid_open
    else:
        add Solid("#000"):
            at top_lid_close
        add Solid("#000"):
            at bottom_lid_close


## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "map_UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")


label call_mapUI:
    $ quick_menu = False
    window hide
    
    show screen pov_blink(opening=False)
    pause 0.4
    
    show image "map/bg map.png" 
    
    hide screen pov_blink
    show screen pov_blink(opening=True)
    pause 0.1
    
    call screen MapUI
    
    $ quick_menu = True 
    window show

screen MapUI:
    add "map/bg map.png"

    imagebutton:
        xpos 618
        ypos 570
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        
    imagebutton:
        xpos 596
        ypos 165
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"

        