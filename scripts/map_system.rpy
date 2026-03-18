init python:
    def _parallax_logic(trans, st, at, factor):
        m_x, m_y = renpy.get_mouse_pos()
        
        offset_x = (m_x - (config.screen_width / 2)) * factor
        offset_y = (m_y - (config.screen_height / 2)) * factor
        
        trans.xoffset = int(offset_x)
        trans.yoffset = int(offset_y)
        return 0

transform mouse_parallax(factor=-0.05):
    subpixel True
    function renpy.curry(_parallax_logic)(factor=factor)

screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "map_UI/lookup_%s.png" 
        action Function(renpy.call_in_new_context, "call_mapUI")

label call_mapUI:
    $ old_quick_menu = quick_menu
    $ old_window = _window 
    
    $ quick_menu = False
    window hide
    
    scene black with eyeclose
    
    show expression current_map as map_bg at mouse_parallax(-0.05):
        zoom 1.05
        anchor (0.5, 0.5) pos (0.5, 0.5)    
    with eyeopen
    
    call screen MapUI
    
    call screen MapUI
    
    scene black with eyeclose
    hide map_bg
    
    $ quick_menu = old_quick_menu
    
    if old_window:
        window show
    else:
        window hide
        
    $ renpy.transition(eyeopen)
    return

screen MapUI:
    modal True
    
    fixed at mouse_parallax(-0.05):
        imagebutton:
            xalign 1.0 
            yalign 0.0
            xoffset -30 
            yoffset 30
            auto "map_UI/lookdown_%s.png" 
            action Return()

        imagebutton:
            xpos 618 ypos 570
            idle "#0000" hover "#0000"
            action NullAction() 
            focus_mask True
            
        imagebutton:
            xpos 596 ypos 165
            idle "#0000" hover "#0000"
            action NullAction()
            focus_mask True