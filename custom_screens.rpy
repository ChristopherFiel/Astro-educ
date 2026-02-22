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


# Blinking Transition
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


screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "map_UI/map_%s.png"
        action Function(renpy.call_in_new_context, "call_mapUI")


label call_mapUI:
    $ quick_menu = False
    window hide
    
    # Eyes Close
    show screen pov_blink(opening=False)
    pause 0.4
    
    # 1. Show the map.
    show image "map/bg map.png" as map_bg zorder 0
    
    # Eyes Open
    hide screen pov_blink
    show screen pov_blink(opening=True)
    pause 0.4
    
    call screen MapUI
    
    # --- CLOSING SEQUENCE (When you click the button) ---
    show screen pov_blink(opening=False)
    pause 0.6
    
    hide map_bg
        
    hide screen pov_blink
    show screen pov_blink(opening=True)
    pause 0.5
    
    $ quick_menu = True 
    window show
    return

screen MapUI:
    # Use 'modal True' so the player can't click things behind the map
    modal True

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "map_UI/map_%s.png"
        action Return()

    imagebutton:
        xpos 618
        ypos 570
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action NullAction() 
        focus_mask True
        
    imagebutton:
        xpos 596
        ypos 165
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action NullAction()
        focus_mask True