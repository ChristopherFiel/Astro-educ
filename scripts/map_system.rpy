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
    
    scene black with eyeclose
    
    show image "map/map.png" as map_bg zorder 0
    
    with eyeopen
    
    call screen MapUI
    
    # Close eyes on the map
    scene black with eyeclose
    
    # Remove map elements while black
    hide map_bg
    
    # Open eyes back to the game world
    
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